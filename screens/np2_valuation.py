"""Valuation for the 12 Nov 2026 finalists. P/E band from daily prices and reported non-GAAP EPS (year-end releases),
two-stage reverse DCF, TTM cash flow from companyfacts. Reuses nextpos_valuation.py (band method and DCF solver).
Forward P/E on past dates uses subsequently REPORTED EPS as a stand-in for consensus then; today uses Yahoo consensus."""
import json, os, sys, pandas as pd, numpy as np, yfinance as yf
os.environ.setdefault("SEC_CACHE", "/tmp/sec_cache")
import nextpos_valuation as v, secutil as s
# Non-GAAP diluted EPS by fiscal year, from each year-end release (8-K 2.02 ex. 99.1), cross-checked against the next year's prior-year column.
v.EPS.update({
 'KBR':  dict(fye=12, eps={2019:1.69,2020:1.73,2021:2.42,2022:2.71,2023:2.91,2024:3.34,2025:3.93}, est={2026:4.06,2027:4.02}),   # adjusted EPS; pre-2019 KBR was a different business and is left out
 'LDOS': dict(fye=12, eps={2015:2.89,2016:3.51,2017:3.72,2018:4.38,2019:5.17,2020:5.83,2021:6.62,2022:6.60,2023:7.30,2024:10.21,2025:11.99}, est={2026:12.68,2027:11.80}),
 'AMTM': dict(fye=9,  eps={2025:2.22}, est={2026:2.46,2027:2.64}),
})
def run(tk, band=True, start='2015-06-01'):
    r = {'ticker': tk}
    if band:
        b = v.band(tk, start=start)
        for col in ('fwd', 'trail'):
            x = b[col].dropna()
            r[col+'_now'] = round(x.iloc[-1], 1); r[col+'_med'] = round(x.median(), 1); r[col+'_p10'] = round(x.quantile(.1), 1); r[col+'_p90'] = round(x.quantile(.9), 1)
            r[col+'_min'] = round(x.min(), 1); r[col+'_pctile'] = round((x < x.iloc[-1]).mean()*100); r['from'] = str(b.index[0].date())
        r['fwd_by_year'] = {int(k): float(x) for k, x in b.fwd.groupby(b.index.year).median().round(1).items()}
    try: cf = v.ttm_cf(tk); r['cf'] = {k: round(x, 1) for k, x in cf.items()}
    except Exception as e: r['cf_err'] = str(e)[:80]; cf = None
    i = yf.Ticker(tk).info
    mc = i['marketCap']/1e6; nd = ((i.get('totalDebt') or 0) - (i.get('totalCash') or 0))/1e6
    r.update(px=i.get('currentPrice'), mcap=round(mc), netdebt=round(nd), ev=round(mc+nd))
    if cf:
        fcf = cf['ocf'] - cf['capex']; r['fcf_ttm'] = round(fcf, 1); r['fcf_yield'] = round(fcf/mc*100, 1); r['fcf_less_sbc'] = round(fcf - (cf.get('sbc') or 0), 1)
        for rr in (0.085, 0.10):
            r[f'g_{rr}'] = round(v.implied_growth(mc+nd, fcf, rr)*100, 1)
            if fcf - (cf.get('sbc') or 0) > 0: r[f'g_exSBC_{rr}'] = round(v.implied_growth(mc+nd, fcf-(cf.get('sbc') or 0), rr)*100, 1)
    return r
if __name__ == "__main__":
    res = {}
    for tk, bd in [('KBR', True), ('LDOS', True), ('AMTM', False), ('HESM', False), ('PODD', False), ('INTU', False), ('ITRI', True), ('LNG', False), ('ADBE', False)]:
        try: res[tk] = run(tk, bd); print(json.dumps(res[tk]))
        except Exception as e: print(tk, 'ERR', e)
    json.dump(res, open('data/np2_valuation_2026-11-12.json', 'w'), indent=1)

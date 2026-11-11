"""Valuation for the finalists: P/E band from daily prices and reported non-GAAP EPS (year-end releases),
two-stage reverse DCF, and TTM cash flow from companyfacts. Run: python3 nextpos_valuation.py
Forward P/E on a past date uses subsequently REPORTED EPS as a stand-in for consensus at the time
(same method as osis/16-number-audit.md). Today's forward P/E uses Yahoo consensus (10 Nov 2026 close)."""
import yfinance as yf, pandas as pd, numpy as np, json
from datetime import date
import secutil as s

# fiscal-year non-GAAP diluted EPS. Source: fiscal year-end earnings releases (8-K item 2.02, ex. 99.1).
# key = (fiscal year-end month), values {FY end year: EPS}. E = Yahoo consensus mean, 10 Nov 2026.
EPS = {
 'TRMB': dict(fye=12, eps={2013:1.58,2014:1.46,2015:1.13,2016:1.19,2017:1.48,2018:1.94,2019:1.99,2020:2.23,2021:2.66,2022:2.64,2023:2.66,2024:2.85,2025:3.13}, est={2026:3.67,2027:4.03}),
 'NSSC': dict(fye=6,  eps={2014:0.09,2015:0.125,2016:0.155,2017:0.15,2018:0.205,2019:0.33,2020:0.23,2021:0.405,2022:0.53,2023:0.73,2024:1.34,2025:1.19,2026:1.60}, est={2027:1.53,2028:1.76}),  # GAAP diluted, split-adjusted (2:1, Jan 2022); FY26 non-GAAP (ex $0.40 litigation)
 'DGII': dict(fye=9,  eps={2020:0.98,2021:1.08,2022:1.66,2023:1.99,2024:1.99,2025:2.10}, est={2026:2.69,2027:3.13}),
 'VNT':  dict(fye=12, eps={2021:2.88,2022:3.08,2023:2.89,2024:2.89,2025:3.20}, est={2026:3.62,2027:3.89}),
 'ARLO': dict(fye=12, eps={2023:0.28,2024:0.40,2025:0.70}, est={2026:1.01,2027:1.13}),
 'ITRI': dict(fye=12, eps={2013:1.90,2014:1.60,2015:0.73,2016:2.54,2017:3.06,2018:2.65,2019:3.32,2020:1.85,2021:1.75,2022:1.13,2023:3.36,2024:5.62,2025:7.13}, est={2026:6.77,2027:6.95}),
}

def band(tk, start='2014-01-01'):
    d = EPS[tk]; e = {**d['eps'], **d['est']}
    h = yf.Ticker(tk).history(period='max', auto_adjust=False)['Close'].dropna()
    h.index = h.index.tz_localize(None); h = h[h.index >= start]
    rows = []
    for dt, px in h.items():
        fy = dt.year if dt.month <= d['fye'] else dt.year + 1        # fiscal year in progress
        fye = pd.Timestamp(year=fy, month=d['fye'], day=28)
        frac = 1 - max(0, (fye - dt).days) / 365.0                   # share of current FY elapsed
        if fy in e and fy + 1 in e and fy - 1 in e:
            ntm = (1 - frac) * e[fy] + frac * e[fy + 1]
            ttm = (1 - frac) * e[fy - 1] + frac * e[fy]
            rows.append((dt, px, px / ntm if ntm > 0 else np.nan, px / ttm if ttm > 0 else np.nan))
    b = pd.DataFrame(rows, columns=['date', 'px', 'fwd', 'trail']).set_index('date')
    return b

def summarize(tk):
    b = band(tk)
    out = {'ticker': tk, 'from': str(b.index[0].date()), 'px': round(b.px.iloc[-1], 2)}
    for col in ('fwd', 'trail'):
        x = b[col].dropna(); t10 = x[x.index >= x.index[-1] - pd.DateOffset(years=10)]
        out[col + '_now'] = round(x.iloc[-1], 1); out[col + '_med'] = round(t10.median(), 1)
        out[col + '_p10'] = round(t10.quantile(.1), 1); out[col + '_p90'] = round(t10.quantile(.9), 1)
        out[col + '_pctile'] = round((t10 < x.iloc[-1]).mean() * 100)
    yr = b.fwd.groupby(b.index.year).median().round(1)
    out['fwd_by_year'] = {int(k): float(v) for k, v in yr.items()}
    return out

def ttm_cf(tk):
    """TTM operating cash flow, capex, SBC, buybacks from companyfacts (FY + latest YTD - prior-year YTD)."""
    f = s.facts(tk)['facts']['us-gaap']
    def ttm(tags):
        for tag in tags:
            if tag not in f: continue
            arr = [x for x in list(f[tag]['units'].values())[0] if 'start' in x]
            if not arr: continue
            last = max(arr, key=lambda x: (x['end'], x['filed']))
            d0, d1 = date.fromisoformat(last['start']), date.fromisoformat(last['end'])
            days = (d1 - d0).days
            if days > 350: return last['val']
            fy = [x for x in arr if 350 <= (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days <= 380 and x['end'] < last['end']]
            if not fy: continue
            fyv = max(fy, key=lambda x: (x['end'], x['filed']))
            py = [x for x in arr if abs((date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days - days) <= 10
                  and 350 <= (d1 - date.fromisoformat(x['end'])).days <= 380]
            if not py: continue
            return fyv['val'] + last['val'] - max(py, key=lambda x: x['filed'])['val']
        return float('nan')
    import nextpos_facts as nf
    return {k: ttm(v) / 1e6 for k, v in nf.TAGS.items() if k in ('rev', 'ocf', 'capex', 'sbc', 'buyback', 'ni')}

def implied_growth(ev, fcf0, r, gt=0.03, years=5):
    """Two-stage: FCF grows g for `years`, then gt forever. Solve g so PV = EV."""
    def pv(g):
        v = 0; f = fcf0
        for t in range(1, years + 1):
            f *= 1 + g; v += f / (1 + r) ** t
        return v + f * (1 + gt) / (r - gt) / (1 + r) ** years
    lo, hi = -0.5, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if pv(mid) > ev: hi = mid
        else: lo = mid
    return mid

if __name__ == "__main__":
    res = {}
    for tk in ['TRMB', 'NSSC', 'DGII', 'VNT', 'ARLO', 'ITRI']:
        r = summarize(tk); r['cf'] = {k: round(v, 1) for k, v in ttm_cf(tk).items()}
        i = yf.Ticker(tk).info
        mc = i['marketCap'] / 1e6; nd = ((i.get('totalDebt') or 0) - (i.get('totalCash') or 0)) / 1e6
        fcf = r['cf']['ocf'] - r['cf']['capex']
        r.update(mcap=round(mc), netdebt=round(nd), ev=round(mc + nd), fcf_ttm=round(fcf, 1), fcf_less_sbc=round(fcf - r['cf']['sbc'], 1),
                 fcf_yield=round(fcf / mc * 100, 1))
        for rr in (0.085, 0.10):
            r[f'g_implied_{rr}'] = round(implied_growth(mc + nd, fcf, rr) * 100, 1)
            r[f'g_implied_exSBC_{rr}'] = round(implied_growth(mc + nd, fcf - r['cf']['sbc'], rr) * 100, 1) if fcf - r['cf']['sbc'] > 0 else None
        res[tk] = r
        print(json.dumps(r))
    json.dump(res, open('data/nextpos_valuation_2026-11-11.json', 'w'), indent=1)

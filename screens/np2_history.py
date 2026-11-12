"""Own-history valuation proxy for a ticker list (screen only): 10-year trailing P/E and P/S bands from
SEC companyfacts (annual GAAP net income, revenue, diluted shares; shares split-adjusted with Yahoo split
history) and Yahoo weekly closes. Usage: python3 np2_history.py TICK1 TICK2 ... -> prints + data/np2_history_2026-11-12.csv
GAAP earnings include one-offs, so the P/E percentile is a screen. Finalists get a non-GAAP band by hand."""
import sys, json, pandas as pd, numpy as np, yfinance as yf, os
from datetime import date
os.environ.setdefault("SEC_CACHE", "/tmp/sec_cache")
import secutil as s
REV = ['RevenueFromContractWithCustomerExcludingAssessedTax','Revenues','SalesRevenueNet','RevenueFromContractWithCustomerIncludingAssessedTax','RevenuesNetOfInterestExpense']
NI = ['NetIncomeLoss','NetIncomeLossAvailableToCommonStockholdersBasic','ProfitLoss']
SH = ['WeightedAverageNumberOfDilutedSharesOutstanding','WeightedAverageNumberOfSharesOutstandingBasic']

def annual(f, tags, unit=None):
    out = {}
    for tag in tags:
        if tag not in f: continue
        for u, arr in f[tag]['units'].items():
            for x in arr:
                if 'start' not in x or x.get('form') not in ('10-K','10-K/A','20-F','40-F'): continue
                d = (date.fromisoformat(x['end']) - date.fromisoformat(x['start'])).days
                if 350 <= d <= 380:
                    k = x['end']
                    if k not in out or x['filed'] > out[k][1]: out[k] = (x['val'], x['filed'], tag)
    # keep, per fiscal year end, the first tag that has it (priority order)
    return {k: v[0] for k, v in out.items()}

def one(tk):
    try:
        f = s.facts(tk)['facts']
    except Exception as e:
        return {'ticker': tk, 'err': 'nofacts'}
    g = f.get('us-gaap') or f.get('ifrs-full') or {}
    rev, ni, sh = annual(g, REV + ['Revenue']), annual(g, NI + ['ProfitLossAttributableToOwnersOfParent']), annual(g, SH + ['AdjustedWeightedAverageShares'])
    t = yf.Ticker(tk)
    h = t.history(period='12y', interval='1wk', auto_adjust=False)['Close'].dropna(); h.index = h.index.tz_localize(None)
    sp = t.splits; sp.index = sp.index.tz_localize(None) if len(sp) else sp.index
    ends = sorted(set(rev) & set(ni) & set(sh))
    if len(ends) < 5: return {'ticker': tk, 'err': 'short', 'n': len(ends)}
    def adjsh(e):
        fac = float(np.prod([v for d, v in sp.items() if d > pd.Timestamp(e)])) if len(sp) else 1.0
        return sh[e] * fac
    E = [pd.Timestamp(e) for e in ends]
    rows = []
    for dt, px in h.items():
        prev = [i for i, e in enumerate(E) if e <= dt]
        if not prev: continue
        i = prev[-1]
        if i + 1 < len(E):
            frac = (dt - E[i]).days / max(1, (E[i+1] - E[i]).days)
            n = (1-frac)*ni[ends[i]] + frac*ni[ends[i+1]]; r = (1-frac)*rev[ends[i]] + frac*rev[ends[i+1]]; shs = (1-frac)*adjsh(ends[i]) + frac*adjsh(ends[i+1])
        else:
            if (dt - E[i]).days > 430: continue
            n, r, shs = ni[ends[i]], rev[ends[i]], adjsh(ends[i])
        mc = px * shs
        rows.append((dt, mc/n if n > 0 else np.nan, mc/r if r > 0 else np.nan))
    b = pd.DataFrame(rows, columns=['d','pe','ps']).set_index('d'); b = b[b.index >= b.index[-1] - pd.DateOffset(years=10)]
    out = {'ticker': tk, 'yrs': round((b.index[-1]-b.index[0]).days/365, 1), 'lastFY': ends[-1]}
    for c in ('pe','ps'):
        x = b[c].dropna()
        if len(x) < 100: continue
        out[c+'_now'] = round(x.iloc[-1], 2); out[c+'_med'] = round(x.median(), 2); out[c+'_p10'] = round(x.quantile(.1), 2)
        out[c+'_pct'] = round((x < x.iloc[-1]).mean()*100)
    yrs = ends[-6:]
    out['rev5'] = "|".join(f"{rev[e]/1e6:.0f}" for e in yrs); out['ni5'] = "|".join(f"{ni[e]/1e6:.0f}" for e in yrs); out['sh5'] = "|".join(f"{adjsh(e)/1e6:.1f}" for e in yrs)
    return out

if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    tks = sys.argv[1:]
    def safe(tk):
        try: return one(tk)
        except Exception as e: return {'ticker': tk, 'err': str(e)[:60]}
    with ThreadPoolExecutor(4) as ex: res = list(ex.map(safe, tks))
    df = pd.DataFrame(res); pd.set_option('display.width', 250); pd.set_option('display.max_rows', 500)
    df.to_csv('data/np2_history_2026-11-12.csv', index=False)
    print(df.drop(columns=[c for c in ('sh5',) if c in df]).to_string())

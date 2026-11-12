"""Mechanism D scan: remaining performance obligations (contracted, unrecognized revenue) from SEC companyfacts,
latest vs one year earlier, against annual revenue. A book growing much faster than revenue is the
award-to-recognition gap. Usage: python3 np2_rpo.py TICK... -> data/np2_rpo_2026-11-12.csv"""
import sys, os, pandas as pd, numpy as np
from datetime import date
os.environ.setdefault("SEC_CACHE", "/tmp/sec_cache")
import secutil as s, np2_history as hst
from concurrent.futures import ThreadPoolExecutor

def one_(tk):
    try: g = s.facts(tk)['facts'].get('us-gaap', {})
    except Exception: return {'ticker': tk, 'err': 1}
    out = {'ticker': tk}
    if 'RevenueRemainingPerformanceObligation' in g:
        arr = [x for x in g['RevenueRemainingPerformanceObligation']['units'].get('USD', [])]
        # total RPO is usually the largest value tagged at each period end (dimensional slices are not in companyfacts)
        by = {}
        for x in arr: by[x['end']] = max(by.get(x['end'], 0), x['val'])
        ends = sorted(by)
        if ends:
            e = ends[-1]; out['rpo_end'] = e; out['rpo'] = by[e] / 1e6
            d1 = date.fromisoformat(e)
            pri = [k for k in ends if 350 <= (d1 - date.fromisoformat(k)).days <= 380]
            if pri: out['rpo_1y'] = by[pri[-1]] / 1e6; out['rpo_gro'] = by[e] / by[pri[-1]] - 1 if by[pri[-1]] else np.nan
            pri2 = [k for k in ends if 715 <= (d1 - date.fromisoformat(k)).days <= 745]
            if pri2: out['rpo_2y'] = by[pri2[-1]] / 1e6
    rev = hst.annual(g, hst.REV)
    if rev:
        ks = sorted(rev); out['rev_fy'] = rev[ks[-1]] / 1e6; out['fy'] = ks[-1]
        if len(ks) > 1 and rev[ks[-2]]: out['rev_gro'] = rev[ks[-1]] / rev[ks[-2]] - 1
        if 'rpo' in out and out['rev_fy']: out['rpo_x_rev'] = out['rpo'] / out['rev_fy']
    return out

def one(tk):
    try: return one_(tk)
    except Exception as e: return {"ticker": tk, "err": str(e)[:40]}

if __name__ == "__main__":
    with ThreadPoolExecutor(4) as ex: res = list(ex.map(one, sys.argv[1:]))
    df = pd.DataFrame(res); df.to_csv('data/np2_rpo_2026-11-12.csv', index=False)
    print(len(df), df.get('rpo', pd.Series()).notna().sum())

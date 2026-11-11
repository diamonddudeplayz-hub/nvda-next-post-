"""Scan every in-range ticker's latest 10-Q for a product vs service split on the income statement.
One filing gives the current and prior-year quarter, so it yields YoY change in service share,
service GM, product GM and product revenue. Output: data/nextpos_splitscan_2026-11-11.csv"""
import pandas as pd, sys, json
import secutil as s, nextpos_split as ns
u = pd.read_csv("data/nextpos_universe_raw_2026-11-11.csv")
u = u[(u.mcap_B >= 0.8) & (u.mcap_B <= 18)]
rows = []
for i, tk in enumerate(u.ticker):
    try:
        if not s.cik(tk.replace('-', '')) and not s.cik(tk): continue
        fl = s.filings(tk, forms=("10-Q",), n=1)
        if not fl: continue
        p = ns.parse(fl[0])
        if not p: continue
        a = {}
        for r in p['rows']:
            if r['cat'] in ('prod', 'svc'):
                v = r['vals']
                if len(v) < 2 or v[0] is None or v[1] is None: continue
                k = (r['kind'], r['cat']); x = a.setdefault(k, [0, 0]); x[0] += abs(v[0]); x[1] += abs(v[1])
        need = [('rev', 'prod'), ('rev', 'svc'), ('cost', 'prod'), ('cost', 'svc')]
        if not all(k in a and a[k][0] > 0 and a[k][1] > 0 for k in need): continue
        pr, sr, pc, sc = [a[k] for k in need]
        rows.append(dict(ticker=tk, period=fl[0]['period'],
            svc_share=sr[0] / (pr[0] + sr[0]), svc_share_py=sr[1] / (pr[1] + sr[1]),
            svc_gm=1 - sc[0] / sr[0], svc_gm_py=1 - sc[1] / sr[1],
            prod_gm=1 - pc[0] / pr[0], prod_gm_py=1 - pc[1] / pr[1],
            svc_gro=sr[0] / sr[1] - 1, prod_gro=pr[0] / pr[1] - 1))
    except Exception as e:
        print(tk, "ERR", repr(e)[:80])
    if i % 50 == 0: print(i, tk, len(rows), flush=True)
df = pd.DataFrame(rows); df.to_csv("data/nextpos_splitscan_2026-11-11.csv", index=False); print(len(df))

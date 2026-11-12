"""Resume np2_universe after Yahoo rate-limiting: refetch rows with no price, 2 threads, backoff, incremental save."""
import pandas as pd, time, sys, numpy as np
import np2_universe as u
from concurrent.futures import ThreadPoolExecutor
F = "data/np2_universe_raw_2026-11-12.csv"
df = pd.read_csv(F)
u_src = dict(zip(df.ticker, df.src))
todo = df.loc[df.px.isna(), 'ticker'].tolist()
print("todo", len(todo), flush=True)
done = {}
def safe(tk):
    for k in range(4):
        try:
            r = u.metrics(tk)
            if r.get("px") or (r.get("mcap_B") == r.get("mcap_B") and r.get("mcap_B") < 0.8): r["src"] = u_src[tk]; return r
        except Exception: pass
        time.sleep(4 * (k + 1))
    return {"ticker": tk, "src": u_src[tk]}
for i in range(0, len(todo), 60):
    with ThreadPoolExecutor(2) as ex: rows = list(ex.map(safe, todo[i:i+60]))
    for r in rows: done[r["ticker"]] = r
    keep = df[~df.ticker.isin(done)]
    out = pd.concat([keep, pd.DataFrame(list(done.values()))], ignore_index=True)
    out.to_csv(F, index=False)
    print(i, out.px.notna().sum(), flush=True)
print("saved", flush=True)

import yfinance as yf, pandas as pd, numpy as np
tickers = {"OSIS":"OSIS","ITRI":"ITRI","LDOS":"LDOS","AXON":"AXON","MLAB":"MLAB","SMIN":"SMIN.L"}
series={}
for k,t in tickers.items():
    h=yf.Ticker(t).history(period="3y",auto_adjust=True)["Close"].dropna()
    h.index=pd.to_datetime(h.index.date)  # strip tz -> date
    series[k]=h[~h.index.duplicated()]
df=pd.concat(series,axis=1).sort_index()
df=df.ffill().dropna()
rets=df.pct_change().dropna()
print(f"rows after align: {len(df)}  from {df.index[0].date()} to {df.index[-1].date()}")
print("\n=== Daily return CORRELATION vs OSIS (3y) ===")
print(rets.corr()["OSIS"].round(2).drop("OSIS").to_string())
print("\n=== Beta of OSIS to each ===")
for c in rets.columns:
    if c=="OSIS": continue
    b=np.polyfit(rets[c].values,rets["OSIS"].values,1)[0]
    print(f"  OSIS vs {c}: beta {b:.2f}")
print("\n=== Relative-value ratio z-score (2y): neg = OSIS cheap vs peer ===")
r2=df[df.index>=df.index[-1]-pd.Timedelta(days=730)]
for c in df.columns:
    if c=="OSIS": continue
    ratio=(r2["OSIS"]/r2[c]).dropna()
    z=(ratio.iloc[-1]-ratio.mean())/ratio.std()
    print(f"  OSIS/{c}: now {ratio.iloc[-1]:.3f}  2y-mean {ratio.mean():.3f}  z={z:+.2f}")
o=df["OSIS"]; o2=o[o.index>=o.index[-1]-pd.Timedelta(days=730)]
print(f"\nOSIS px {o.iloc[-1]:.2f}  2y-mean {o2.mean():.2f}  z={(o.iloc[-1]-o2.mean())/o2.std():+.2f}")

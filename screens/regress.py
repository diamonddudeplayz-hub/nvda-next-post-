import yfinance as yf, pandas as pd, numpy as np
tickers = {"OSIS":"OSIS","ITRI":"ITRI","LDOS":"LDOS","AXON":"AXON","MLAB":"MLAB","SMIN":"SMIN.L"}
px={}
for k,t in tickers.items():
    try:
        h=yf.Ticker(t).history(period="3y",auto_adjust=True)["Close"].dropna()
        px[k]=h
    except Exception as e:
        print(k,"err",e)
df=pd.DataFrame(px).dropna()
df.index=df.index.tz_localize(None)
rets=df.pct_change().dropna()
print("=== Daily return CORRELATION vs OSIS (3y) ===")
print(rets.corr()["OSIS"].round(2).to_string())
print("\n=== Beta of OSIS to each (slope) ===")
for c in rets.columns:
    if c=="OSIS": continue
    b=np.polyfit(rets[c],rets["OSIS"],1)[0]
    print(f"  OSIS vs {c}: beta {b:.2f}")
# Relative value: OSIS / peer ratio z-score (is OSIS cheap vs its own history relative to peer)
print("\n=== Relative-value ratio z-score (2y) : OSIS/peer, neg z = OSIS cheap vs peer ===")
r2=df.last("730D")
for c in df.columns:
    if c=="OSIS": continue
    ratio=(r2["OSIS"]/r2[c]).dropna()
    z=(ratio.iloc[-1]-ratio.mean())/ratio.std()
    print(f"  OSIS/{c}: current {ratio.iloc[-1]:.3f}  mean {ratio.mean():.3f}  z={z:+.2f}")
# OSIS own price z-score and drawdown
o=df["OSIS"]
print(f"\n=== OSIS price: last {o.iloc[-1]:.2f}  2y-mean {o.last('730D').mean():.2f}  z={(o.iloc[-1]-o.last('730D').mean())/o.last('730D').std():+.2f}")
print(f"    off 1y-high: {(o.iloc[-1]/o.last('365D').max()-1)*100:.1f}%   off 1y-low: {(o.iloc[-1]/o.last('365D').min()-1)*100:+.1f}%")

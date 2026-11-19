"""Regime-break chart for the gold post, house style (navy + orange, clean grid).
Run: python3 -I charts/make_regime_chart.py
Reads the two source workbooks, writes charts/gold-vs-fedfunds-regime.png.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import openpyxl, datetime as dt
import pandas as pd, numpy as np

# --- house palette (from Post 1/2 make_charts.py) ---
NAVY="#1b3a5b"; ORANGE="#d8732a"; SLATE="#8a9bb0"; INK="#1a1a1a"; GRID="#d9dee6"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,
    "axes.edgecolor":"#cfd6df","axes.linewidth":1.0,"figure.dpi":160})

GOLD="/root/.claude/uploads/c3b4cb41-5c57-50fe-9c30-4ede4011645b/1e654842-gold_max.xlsx"
FED="/root/.claude/uploads/c3b4cb41-5c57-50fe-9c30-4ede4011645b/47a29518-fed_fund_rates.xlsx"

def load(path):
    wb=openpyxl.load_workbook(path,read_only=True,data_only=True)
    ws=wb[wb.sheetnames[0]]; rows=[]
    for r in ws.iter_rows(min_row=3,values_only=True):
        d,v=r[0],r[1]
        if isinstance(d,dt.datetime) and isinstance(v,(int,float)): rows.append((d.date(),float(v)))
    wb.close()
    s=pd.Series({d:v for d,v in rows}).sort_index(); s.index=pd.to_datetime(s.index); return s

gold=load(GOLD); fed=load(FED)
fed_d=fed.reindex(gold.index.union(fed.index)).sort_index().ffill().reindex(gold.index)
df=pd.DataFrame({"gold":gold,"fed":fed_d}).dropna().loc["2004-01-01":]
m=df.resample("ME").last()
x=m.index

def corr(a,b): return np.corrcoef(a,b)[0,1]
c_old=corr(*[df.loc["2004-01-01":"2021-12-31"][k] for k in ("gold","fed")])
c_new=corr(*[df.loc["2022-01-01":][k] for k in ("gold","fed")])

fig,ax=plt.subplots(figsize=(9.6,5.6))
ax2=ax.twinx()
split=pd.Timestamp("2022-01-01")
# shade the post-2022 regime faintly
ax.axvspan(split,x[-1],color="#f3b98e",alpha=0.14,zorder=0)
ax.axvline(split,color="#9aa6b4",lw=1.2,ls=(0,(4,3)),zorder=2)

ln1=ax.plot(x,m["gold"],color=NAVY,lw=2.6,zorder=4,label="Gold ($/oz, left)")
ln2=ax2.plot(x,m["fed"],color=ORANGE,lw=2.2,zorder=3,label="Fed funds target (%, right)")

ax.set_ylabel("Gold, $/oz",color=NAVY,fontsize=10.5)
ax2.set_ylabel("Fed funds target rate, %",color=ORANGE,fontsize=10.5)
ax.tick_params(axis="y",colors=NAVY,labelsize=10)
ax2.tick_params(axis="y",colors=ORANGE,labelsize=10)
ax.set_ylim(0,5800); ax2.set_ylim(0,6.2)
ax.tick_params(axis="x",labelsize=9.5,colors="#555")
for s in ["top"]:
    ax.spines[s].set_visible(False); ax2.spines[s].set_visible(False)
ax.grid(axis="y",color=GRID,lw=0.8,zorder=0)

# regime annotations
ax.annotate(f"2004–2021\nmove inversely  (corr {c_old:+.2f})",
            xy=(pd.Timestamp("2012-06-01"),4950),fontsize=10.5,color="#5b6b7d",
            ha="center",va="center",fontweight="bold")
ax.annotate(f"2022–2026\ndecoupled  (corr {c_new:+.2f})\ngold +109% as the Fed hiked +375bp",
            xy=(pd.Timestamp("2024-02-01"),5450),fontsize=10.5,color=ORANGE,
            ha="center",va="center",fontweight="bold")

fig.suptitle("Gold stopped trading against the Fed in 2022",
             fontsize=15.5,fontweight="bold",color=INK,x=0.075,ha="left",y=0.965)
fig.text(0.075,0.875,
    "For 17 years gold fell when the funds rate rose. Then the Fed hiked 375bp and gold rose anyway.",
    fontsize=10.6,color="#666",va="bottom")
fig.text(0.075,0.015,
    "Monthly, Jan 2004–Nov 2026. Gold: LSEG XAU spot. Fed funds: US target rate. Author's calculations.",
    fontsize=9,color="#888",style="italic")
fig.subplots_adjust(left=0.085,right=0.9,top=0.80,bottom=0.10)
out="charts/gold-vs-fedfunds-regime.png"
fig.savefig(out,facecolor="white")
print("wrote",out,"| corr old",round(c_old,3),"new",round(c_new,3))

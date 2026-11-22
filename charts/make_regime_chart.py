"""Gold vs fed funds, honest three-phase version. House style.
Run: python3 -I charts/make_regime_chart.py"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import openpyxl, datetime as dt, pandas as pd, numpy as np
NAVY="#1b3a5b"; ORANGE="#d8732a"; SLATE="#8a9bb0"; INK="#1a1a1a"; GRID="#d9dee6"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.edgecolor":"#cfd6df","axes.linewidth":1.0,"figure.dpi":160})
GOLD="/root/.claude/uploads/c3b4cb41-5c57-50fe-9c30-4ede4011645b/1e654842-gold_max.xlsx"
FED="/root/.claude/uploads/c3b4cb41-5c57-50fe-9c30-4ede4011645b/47a29518-fed_fund_rates.xlsx"
def load(p):
    wb=openpyxl.load_workbook(p,read_only=True,data_only=True); ws=wb[wb.sheetnames[0]]; rows=[]
    for r in ws.iter_rows(min_row=3,values_only=True):
        d,v=r[0],r[1]
        if isinstance(d,dt.datetime) and isinstance(v,(int,float)): rows.append((d.date(),float(v)))
    wb.close(); s=pd.Series({d:v for d,v in rows}).sort_index(); s.index=pd.to_datetime(s.index); return s
gold=load(GOLD); fed=load(FED)
fed_d=fed.reindex(gold.index.union(fed.index)).sort_index().ffill().reindex(gold.index)
df=pd.DataFrame({"gold":gold,"fed":fed_d}).dropna().loc["2020-06-01":]
m=df.resample("ME").last(); x=m.index
fig,ax=plt.subplots(figsize=(9.6,5.6)); ax2=ax.twinx()
p_hike=pd.Timestamp("2022-03-01"); p_peak=pd.Timestamp("2023-07-27"); p_cut=pd.Timestamp("2024-09-18"); p_rehike=pd.Timestamp("2025-12-11")
ax.axvspan(p_peak,p_cut,color="#d8732a",alpha=0.12); ax.axvspan(p_rehike,x[-1],color="#1b3a5b",alpha=0.06)
for d in (p_hike,p_peak,p_cut,p_rehike): ax.axvline(d,color="#aeb7c2",lw=1.0,ls=(0,(4,3)))
ax.plot(x,m["gold"],color=NAVY,lw=2.7,zorder=4)
ax2.plot(x,m["fed"],color=ORANGE,lw=2.1,zorder=3)
ax.set_ylabel("Gold, $/oz",color=NAVY,fontsize=10.5); ax2.set_ylabel("Fed funds target, %",color=ORANGE,fontsize=10.5)
ax.tick_params(axis="y",colors=NAVY,labelsize=10); ax2.tick_params(axis="y",colors=ORANGE,labelsize=10)
ax.set_ylim(0,5900); ax2.set_ylim(0,6.3); ax.tick_params(axis="x",labelsize=9.5,colors="#555")
ax.spines["top"].set_visible(False); ax2.spines["top"].set_visible(False)
ax.grid(axis="y",color=GRID,lw=0.8,zorder=0)
ax.annotate("Hiking:\n-21% then recovers",xy=(pd.Timestamp("2022-09-10"),3150),ha="center",va="center",fontsize=9.3,color="#5b6b7d",fontweight="bold")
ax.annotate("Held at 5.25-5.50%\ngold +32%",xy=(pd.Timestamp("2024-02-20"),3900),ha="center",va="center",fontsize=9.6,color="#8a5a2a",fontweight="bold")
ax.annotate("Hikes resume\n-32% from peak",xy=(pd.Timestamp("2026-05-20"),4800),ha="center",va="center",fontsize=9.3,color="#5b6b7d",fontweight="bold")
fig.suptitle("Gold rose while rates sat at a two-decade high",fontsize=15.5,fontweight="bold",color=INK,x=0.075,ha="left",y=0.965)
fig.text(0.075,0.875,"The old rule caps gold when rates are high. Through the 2023-24 hold at 5.25-5.50%, gold rose 32% before a single cut.",fontsize=10.2,color="#666",va="bottom")
fig.text(0.075,0.015,"Monthly, 2020-2026. Gold: LSEG XAU spot. Fed funds: US target rate. Author's calculations.",fontsize=9,color="#888",style="italic")
fig.subplots_adjust(left=0.085,right=0.9,top=0.80,bottom=0.10)
fig.savefig("charts/gold-vs-fedfunds-regime.png",facecolor="white"); print("wrote regime chart")

# --- central-bank demand flow chart (the floor) ---
fig,ax=plt.subplots(figsize=(8.8,5.3))
q=["Q3'25","Q4'25","Q1'26","Q2'26","Q3'26"]; v=[226.3,209.9,57.7,296.3,321.2]
lab=["226t","210t","57t","296t","321t"]
cols=[SLATE,SLATE,"#c9a06a",NAVY,ORANGE]
ax.axhline(227,color="#9aa6b4",lw=1.3,ls=(0,(4,3)),zorder=2)
ax.annotate("5-year quarterly average, 227t",xy=(0.0,355),fontsize=9.3,color="#6b7785",ha="left")
ax.bar(range(5),v,color=cols,width=0.64,zorder=3)
for i,val in enumerate(v):
    ax.annotate(lab[i],(i,val),xytext=(0,6),textcoords="offset points",ha="center",fontweight="bold",color=INK,fontsize=12)
ax.annotate("Q1 scare\n(revised down\nfrom 244t)",xy=(2,57.7),xytext=(2,150),ha="center",fontsize=8.8,color="#8a6a3a",
            arrowprops=dict(arrowstyle="-",color="#c9a06a",lw=1))
ax.annotate("+42% y/y",xy=(4,321),xytext=(4,360),ha="center",fontsize=9.6,color=ORANGE,fontweight="bold")
ax.set_xticks(range(5)); ax.set_xticklabels(q,fontsize=11,color="#444")
ax.set_ylim(0,400); ax.set_yticks([0,100,200,300,400]); ax.set_yticklabels(["0","100","200","300","400t"],color="#555")
ax.set_ylabel("Central bank net purchases, tonnes/qtr",fontsize=10,color="#555")
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.grid(axis="y",color=GRID,lw=0.8,zorder=0)
fig.suptitle("The floor is a flow: central banks never stopped buying",fontsize=14.8,fontweight="bold",color=INK,x=0.085,ha="left",y=0.965)
fig.text(0.085,0.875,"Quarterly central-bank net purchases. After a soft Q1, buying ran at 296t and 321t, above the 5-year average.",fontsize=10.0,color="#666",va="bottom")
fig.text(0.085,0.02,"Source: World Gold Council, Gold Demand Trends Q3 2026 (3 Nov 2026). 5-yr avg per WGC.",fontsize=9,color="#888",style="italic")
fig.subplots_adjust(left=0.10,right=0.96,top=0.80,bottom=0.10)
fig.savefig("charts/central-bank-flow.png",facecolor="white"); print("wrote flow chart")

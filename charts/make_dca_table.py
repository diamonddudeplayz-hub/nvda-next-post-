"""Clean DCA example table as a PNG, house style (navy header, no gridlines)."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
NAVY="#1b3a5b"; ORANGE="#d8732a"; INK="#1a1a1a"; SOFT="#eef1f5"; TINT="#fbeadd"
plt.rcParams.update({"font.family":"DejaVu Sans"})

D=r"\$"  # escaped dollar so matplotlib never enters math mode
rows=[["1",f"{D}130","7.69"],["2",f"{D}110","9.09"],["3",f"{D}100","10.00"],["4",f"{D}120","8.33"]]
cols=["Month","WPM price",f"Shares {D}1,000 buys"]

fig,ax=plt.subplots(figsize=(7.6,4.7)); ax.axis("off")
ax.set_xlim(0,1); ax.set_ylim(0,1)
xc=[0.14,0.46,0.80]
top=0.70; rh=0.102

fig.text(0.06,0.935,f"Dollar-cost averaging {D}1,000 a month into WPM",fontsize=14,fontweight="bold",color=INK,ha="left")
fig.text(0.06,0.865,"Fixed dollars buy more shares when the price is down.",fontsize=10,color="#666",ha="left")

ax.add_patch(plt.Rectangle((0.05,top),0.90,rh,color=NAVY,zorder=1))
for x,c in zip(xc,cols):
    ax.text(x,top+rh/2,c,color="white",fontweight="bold",fontsize=11,ha="center",va="center",zorder=2)

for i,r in enumerate(rows):
    y=top-(i+1)*rh
    if i%2==0: ax.add_patch(plt.Rectangle((0.05,y),0.90,rh,color=SOFT,zorder=0))
    for x,val in zip(xc,r):
        ax.text(x,y+rh/2,val,color=INK,fontsize=11,ha="center",va="center")

ys=top-4*rh-0.17; bh=0.155
ax.add_patch(plt.Rectangle((0.05,ys),0.90,bh,color=TINT,zorder=0))
ax.text(0.5,ys+bh*0.66,f"{D}4,000 invested  →  35.12 shares",color=INK,fontsize=11.5,fontweight="bold",ha="center",va="center")
ax.text(0.5,ys+bh*0.28,f"average cost {D}113.91, under the {D}115.00 simple average",color=ORANGE,fontsize=10.5,fontweight="bold",ha="center",va="center")

fig.text(0.06,0.05,"Illustrative. Average cost = total invested ÷ shares bought.",fontsize=8.6,color="#999",style="italic",ha="left")
fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
fig.savefig("charts/dca-example.png",dpi=200,facecolor="white")
print("ok")

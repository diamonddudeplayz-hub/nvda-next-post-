"""Post 2 cover image, 1200x630 px (social / email card size).
Order-of-damage chart, scaled up for a wide cover. Run: python3 charts/make_cover.py"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

NAVY = "#1b3a5b"
ORANGE = "#d8732a"
SLATE = "#8a9bb0"
INK = "#1a1a1a"
GRID = "#d9dee6"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.edgecolor": "#cfd6df",
    "axes.linewidth": 1.0,
})

dates = ["Oct 1","Oct 2","Oct 5","Oct 6","Oct 7","Oct 8","Oct 9",
         "Oct 12","Oct 13","Oct 14","Oct 15","Oct 16"]
nvda = [230.86,233.95,238.90,239.24,237.47,230.48,229.28,226.32,228.52,221.30,217.23,214.13]
crwv = [88.57,89.62,87.39,91.72,88.45,81.58,82.08,80.26,77.81,65.78,69.69,61.39]
nbis = [232.28,242.81,232.57,249.87,237.15,219.71,221.07,210.06,206.86,186.01,188.41,165.47]

base = 4  # Oct 7 = 100
def idx(s):
    b = s[base]
    return [100.0 * v / b for v in s]

ni, ci, bi = idx(nvda), idx(crwv), idx(nbis)
x = list(range(len(dates)))

# 1200 x 630 px = 12 x 6.3 in at dpi 100
fig, ax = plt.subplots(figsize=(12, 6.3), dpi=100)

ax.axhline(100, color=GRID, lw=1, zorder=1)
ax.plot(x, ci, color=ORANGE, lw=3.0, zorder=3)
ax.plot(x, bi, color=SLATE, lw=3.0, zorder=3)
ax.plot(x, ni, color=NAVY, lw=3.4, zorder=4)

ax.axvline(base, color=GRID, lw=1, ls=(0, (3, 3)), zorder=1)
ax.annotate("Oct 7 = 100", xy=(base, 108.5), xytext=(base + 0.1, 108.5),
            fontsize=13, color="#7a7a7a", va="center")

def endlabel(s, name, color, dy=0):
    ax.scatter([x[-1]], [s[-1]], color=color, s=40, zorder=5)
    pct = s[-1] - 100
    ax.annotate(f"{name}  {pct:+.0f}%", xy=(x[-1], s[-1]),
                xytext=(x[-1] + 0.18, s[-1] + dy),
                color=color, fontsize=15.5, fontweight="bold", va="center")

endlabel(ni, "NVIDIA", NAVY, dy=2.0)
endlabel(ci, "CoreWeave", ORANGE, dy=-0.5)
endlabel(bi, "Nebius", SLATE, dy=1.4)

ax.set_xticks(x)
ax.set_xticklabels(dates, fontsize=12.5, color="#555")
ax.set_ylim(66, 110)
ax.set_yticks([70, 80, 90, 100, 110])
ax.set_yticklabels(["70", "80", "90", "100", "110"], color="#555", fontsize=12)
ax.set_ylabel("Indexed to Oct 7, 2026 = 100", fontsize=13, color="#555")

for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
ax.set_xlim(-0.3, len(dates) + 2.6)

fig.suptitle("The order of damage: NVIDIA fell last, and least",
             fontsize=23, fontweight="bold", color=INK, x=0.065, ha="left", y=0.965)
fig.text(0.065, 0.875,
         "Share prices since the October 8 selloff. The lessors fell about three times as far as the chipmaker.",
         fontsize=14.5, color="#666", va="bottom")
fig.text(0.065, 0.02,
         "Daily closing prices, October 1–16, 2026. Source: Yahoo Finance.",
         fontsize=11.5, color="#888", style="italic")

fig.subplots_adjust(left=0.065, right=0.9, top=0.80, bottom=0.12)
out = "charts/cover-1200x630.png"
fig.savefig(out, facecolor="white")
print("wrote", out)

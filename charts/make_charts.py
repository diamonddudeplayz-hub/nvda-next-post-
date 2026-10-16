"""House-style charts for Post 2. Run: python3 charts/make_charts.py
Outputs PNGs into charts/. Matches Post 1 look: navy + orange, clean grid."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

# --- house palette ---
NAVY = "#1b3a5b"
ORANGE = "#d8732a"
SLATE = "#8a9bb0"
INK = "#1a1a1a"
GRID = "#d9dee6"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.edgecolor": "#cfd6df",
    "axes.linewidth": 1.0,
    "figure.dpi": 160,
})

# --- data: daily closes, Oct 2026 (Yahoo Finance) ---
dates = ["Oct 1","Oct 2","Oct 5","Oct 6","Oct 7","Oct 8","Oct 9",
         "Oct 12","Oct 13","Oct 14","Oct 15","Oct 16"]
nvda = [230.86,233.95,238.90,239.24,237.47,230.48,229.28,226.32,228.52,221.30,217.23,215.20]
crwv = [88.57,89.62,87.39,91.72,88.45,81.58,82.08,80.26,77.81,65.78,69.69,61.58]
nbis = [232.28,242.81,232.57,249.87,237.15,219.71,221.07,210.06,206.86,186.01,188.41,167.85]

base = 4  # index to Oct 7 = 100
def idx(series):
    b = series[base]
    return [100.0 * v / b for v in series]

ni, ci, bi = idx(nvda), idx(crwv), idx(nbis)
x = list(range(len(dates)))

fig, ax = plt.subplots(figsize=(8.6, 5.2))

ax.axhline(100, color=GRID, lw=1, zorder=1)
ax.plot(x, ci, color=ORANGE, lw=2.4, zorder=3)
ax.plot(x, bi, color=SLATE, lw=2.4, zorder=3)
ax.plot(x, ni, color=NAVY, lw=2.8, zorder=4)

# Oct 7 reference marker
ax.axvline(base, color=GRID, lw=1, ls=(0, (3, 3)), zorder=1)
ax.annotate("Oct 7 = 100", xy=(base, 108.5), xytext=(base + 0.1, 108.5),
            fontsize=10, color="#7a7a7a", va="center")

# direct end labels
def endlabel(series_idx, name, color, dy=0):
    ax.scatter([x[-1]], [series_idx[-1]], color=color, s=26, zorder=5)
    pct = series_idx[-1] - 100
    ax.annotate(f"{name}  {pct:+.0f}%", xy=(x[-1], series_idx[-1]),
                xytext=(x[-1] + 0.18, series_idx[-1] + dy),
                color=color, fontsize=11.5, fontweight="bold", va="center")

endlabel(ni, "NVIDIA", NAVY, dy=1.8)
endlabel(ci, "CoreWeave", ORANGE, dy=-0.4)
endlabel(bi, "Nebius", SLATE, dy=1.2)

ax.set_xticks(x)
ax.set_xticklabels(dates, fontsize=9.5, color="#555")
ax.set_ylim(66, 110)
ax.set_yticks([70, 80, 90, 100, 110])
ax.set_yticklabels(["70", "80", "90", "100", "110"], color="#555")
ax.set_ylabel("Indexed to Oct 7, 2026 = 100", fontsize=10.5, color="#555")

for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
ax.grid(axis="y", color=GRID, lw=0.8, zorder=0)
ax.set_xlim(-0.3, len(dates) + 2.6)

fig.suptitle("The order of damage: NVIDIA fell last, and least",
             fontsize=15.5, fontweight="bold", color=INK, x=0.085, ha="left", y=0.975)
fig.text(0.085, 0.905,
         "Share prices since the October 8 selloff. The lessors fell about three times as far as the chipmaker.",
         fontsize=10.8, color="#666", va="bottom")

fig.text(0.085, 0.015,
         "Daily closing prices, October 1–16, 2026. Source: Yahoo Finance.",
         fontsize=9, color="#888", style="italic")

fig.subplots_adjust(left=0.085, right=0.9, top=0.84, bottom=0.11)
out = "charts/order-of-damage.png"
fig.savefig(out, facecolor="white")
print("wrote", out)

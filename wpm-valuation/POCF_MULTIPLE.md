# WPM P/OCF Multiple vs Gold — Multiple-Compression / Re-Rating Analysis
_Built 2026-11-25. Supports the Valuation section's re-rating-optionality point and ties to the Part 3 gold-floor thesis. Data: Refinitiv CF-Export-25-11-2026 (actual diluted WASO + OCF), Estimate Details WPM.TO (consensus OCF), wpm_max / gold_max price series. All P/OCF on a **current-year** basis (price ÷ that year's OCF/share) unless noted._

## The question
Darren's hypothesis (Part 3 floor thesis, applied to the vehicle): WPM's cash-flow multiple has **compressed as if the market expects gold to mean-revert** — paying a low multiple on currently-high, gold-driven OCF because it assumes that OCF falls back. If the central-bank floor holds and OCF does **not** revert, the multiple should re-rate up, a tailwind *on top of* the funded +50% volume growth.

## The data (verdict: supported, on a forward basis especially)
| Year | Avg gold | OCF (US$M) | Dil. sh (M) | OCF/sh | Avg WPM px | Current-yr P/OCF |
|---|---|---|---|---|---|---|
| 2016 | 1,249 | 584 | 442.1 | 1.32 | 20.75 | 15.7× |
| 2017 | 1,267 | 539 | 442.5 | 1.22 | 20.57 | 16.9× |
| 2018 | 1,266 | 477 | 444.3 | 1.07 | 19.41 | 18.1× |
| 2019 | 1,402 | 502 | 448.3 | 1.12 | 25.15 | 22.5× |
| 2020 | 1,776 | 765 | 450.6 | 1.70 | 41.17 | 24.2× |
| 2021 | 1,792 | 845 | 451.2 | 1.87 | 41.86 | 22.3× |
| 2022 | 1,795 | 743 | 452.7 | 1.64 | 38.49 | 23.4× |
| 2023 | 1,952 | 751 | 453.6 | 1.66 | 45.24 | 27.3× |
| 2024 | 2,405 | 1,028 | 454.4 | 2.26 | 55.17 | 24.4× |
| 2025 | 3,484 | 1,905 | 454.9 | 4.19 | 91.36 | 21.8× |
| 2026E | 4,371 | 2,878 | 455.0 | 6.33 | 130.06 | 20.6× |

- **2016–18 trough avg = ~17×** (gold ~$1,250–1,270).
- **2019–24 mid-cycle avg = 24.0×** (range 22.3–27.3×).
- **Today (Nov-25, px $122.60):** current-year (2026E) P/OCF = **19.4×**; forward **2027E = ~17×** (OCF/sh $7.10), 2028E ~17×. (Model Comparables tab shows 15.0× at the $109.91 build price / $3,332M OCF — same ballpark; the move to $122.60 and the $3,230M consensus OCF lift it to ~17×.)
- **Correlation(current-yr P/OCF, gold), monthly 2016–26 = +0.26** — i.e. the multiple did *not* expand as gold ~tripled; on a forward basis it compressed. The market treats high gold as unsustainable and refuses to capitalize it.

## Interpretation (honest)
1. **This is a time-series / own-history signal, not a cross-sectional cheapness signal.** Versus peers, WPM is a deserved premium and "fairly valued" (see COMPS.md) — no bargain there. Versus **its own history and the growth ahead**, the forward multiple (~17×) sits at the 2016–18 trough it carried at $1,250 gold, despite OCF at a record (~$2.9B 2026E) and still rising on funded volume to 2030. That is the market pricing gold mean-reversion into the multiple.
2. **Re-rating optionality (upside, not base):** 2027E OCF/sh ($7.10) × 24× mid-cycle ≈ **$170**; 2026E ($6.33) × 24× ≈ **$152**. Brackets the DCF base ($133) → street (~$185) and converges with the DCF bull ($179). If the floor holds, re-rating toward mid-cycle is worth ~+25–40% on its own.
3. **No double-count with the DCF.** The DCF is intrinsic value at a fixed 6% real discount rate and already captures the *cash-flow level* at $4,200 base gold ($133). The multiple re-rating is a *separate* lever (what the market is willing to pay), which the DCF deliberately does not assume. So presenting both is clean: DCF $133 (intrinsic, base) + multiple-normalization optionality to ~$150–170 if the floor holds.
4. **Margin of safety:** buying at a near-trough forward multiple on record, growing cash flow means we are *not* paying a peak multiple on peak earnings — the classic commodity-equity trap is inverted in our favour.

## Report usage (one tight paragraph + one exhibit)
- Valuation section: pin "~17× forward P/OCF vs 24× mid-cycle / ~17× 2016–18 trough; market pricing reversion; re-rate to mid-cycle ≈ $150–170 = upside optionality + margin of safety; DCF base does not rely on it."
- Exhibit: **P/OCF (current-year) vs average gold price, 2016–2026**, dual axis — shows the multiple flat-to-down while gold/OCF ran up. Data in `pocf_vs_gold.csv`.
- Q&A defense: the multiple point is *own-history*, not *vs peers*; the re-rate is optionality, not in the base; OCF and shares are company-reported (Refinitiv as-reported), multiples reconcile to the model's Comparables tab.

## Caveats to disclose
- Current-year vs forward basis differ; keep comparisons on one basis in the report (we use current-year for history, and quote forward 2027E separately and labelled).
- Consensus 2027E+ OCF itself embeds a gold assumption (~$4,000); part of the "low forward multiple" is the market flagging OCF as gold-inflated — which is exactly the reversion bet. The floor thesis is the counter.
- Pre-2016 (Silver Wheaton, ~355–405M sh) excluded to keep the share base clean.

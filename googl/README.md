# GOOGL / Alphabet deep-dive — "cleanest AI-ROI play" thesis

The deep-dive the AI-complex handover committed to: own the **implementer that captures the ROI
and self-funds (GOOGL)**, not the cyclical supplier (Micron) or the circular-financed shovel
(NVDA). Built off the Q3'26 call + refreshed Nov 21, 2026 with the full source set.

**Price anchor: $265.29 (Nov 20, 2026 close)** — at the 52-week low, ~35% off the $408 high.
Figures are copied from source material (TIKR, call transcripts, the 10-Q from EDGAR, sell-side).
Point-in-time, not a live feed. Confirm quotes on a terminal — Claude-pulled prices aren't trusted.

## Read in this order
1. **`00-verdict-and-edge.md`** — the answer. Verdict, where the price is underestimating, where
   the edge is, scenario frame, what to own and what to watch. **Start here.**
2. `estimates-consensus.md` — 20-yr history + consensus to 2030 for EPS, EBITDA, CFO, FCF, and
   segment revenue/EBITDA. Parsed from the 10 TIKR estimate files. The data backbone.
3. `10q-q3-2026.md` — Alphabet's actual Q3'26 10-Q (income stmt, balance sheet, cash flow,
   segments, the $924B commitments). Pulled from EDGAR.
4. `analyst-notes-nov-2026.md` — sell-side synthesis (Oct 29 cuts + Nov 12–18 alt-data).
5. Transcript notes: `q4-2025-…`, `q1-2026-…`, `q2-2026-…`, `q3-2026-earnings-call-notes.md`
   (the 4-quarter set) + `conferences-2026-notes.md` (Jun special, Sep Goldman/Kurian, May YouTube).
6. `valuation-and-analyst-targets.md` — TIKR/TipRanks snapshot + post-Q3 target cuts (Nov 5–6).
7. `analysis-at-these-prices.md` — the prior (Nov 6, $283) synthesis. Superseded by #1 but kept
   as the record of how the read evolved as the price fell $283 → $265.

## The thesis in one line
De-rate to the 52-wk low is a "AI is eating Search" fear the hard data contradicts (Google search
share **91%, +100bps y/y**; ChatGPT ~7% of Google US and flat). At **17.8x FY27 EPS / ~10x FY27
EV/EBITDA** with net cash and free TPU optionality, it's the cleanest AI-ROI long — **core
ballast, not torque**. The whole call is Search *monetization* (not demand). One number to track.

## Data notes / caveats
- `_estimates_raw.json` — raw parsed values from the TIKR files (annual + interim).
- GAAP EPS is distorted by equity-stake marks (OI&E); value on FY27 clean EPS + EBITDA + op income.
- Cloud revenue growth is partly low-margin TPU hardware gross-up — judge on operating margin.
- The repo's `2027 q2 10-q.pdf` is **NVIDIA's**, not Alphabet's — Alphabet's 10-Q was fetched from
  EDGAR for `10q-q3-2026.md`. (If you still want the PDF in the repo, grab Alphabet's Q3'26 10-Q.)

## Binary sources in the repo (parent dir)
- `Estimate Details GOOGL.O (1..10).xlsx` — the TIKR estimate detail (styles.xml is malformed;
  parsed via raw-XML extraction, see `_estimates_raw.json`).
- Sell-side PDFs: 5 × Oct 29 (Q3 reaction) + 5 × Nov 12–18 (alt-data/agentic).

# AMZN / Amazon deep-dive — hyperscaler bake-off vs GOOGL

Same framework as the `googl/` folder, built Nov 22, 2026 to weigh Amazon against Google for the
"cleanest AI-ROI, lowest-idiosyncratic-risk" portfolio slot. Price anchor **$246.82 (Nov 20 close)**,
−14% off the $287 high. Figures from TIKR, the Q3'26 10-Q (EDGAR), call transcripts, and sell-side.

## Read in this order
1. **`../GOOGL-vs-AMZN-head-to-head.md`** — the bake-off. **Start here.** (At repo root.)
2. **`00-amzn-verdict-and-edge.md`** — AMZN standalone verdict, edge, bear, scenarios.
3. `estimates-consensus.md` — 20-yr history → 2030 (revenue, EBITDA, EPS, CFO, FCF, **capex**, AWS, ads).
4. `10q-q3-2026.md` — the actual Q3'26 10-Q (segments, AWS margin, capex, the equity-mark distortion).
5. `earnings-calls-2026-notes.md` — the 4-quarter call set (Q4'25→Q3'26).
6. `analyst-notes-oct-2026.md` — the 4 Oct-30 sell-side notes.
7. `amzn-price-vs-multiple.png` — 22-yr price + trailing P/E (note: AMZN P/E runs structurally high).

## The thesis in one line
**AWS is arguably the best AI-ROI business in the complex** (+39% & accelerating, 38.7% margin, $578B
backlog, >40% guided both years), and **Trainium means own-silicon is NOT a Google-only edge** — but at
**23x FY27, −14% off the high, net debt ~$191B, β 1.50**, the margin of safety is thinner than GOOGL
(17.8x, −35%, net cash). **Best business, mediocre entry.** Own both; start bigger in GOOGL, add AMZN on a dip.

## Key data notes
- GAAP FY26 EPS ($12.82) distorted by equity marks (Rivian/Anthropic, +$68.4B 9mo non-op) — use FY27 $10.75.
- AWS EBITDA file is single-analyst (n=1) — use the 38.7% segment op margin instead.
- 15 TIKR estimate files; styles.xml malformed → parsed via raw XML (`_amzn_estimates_raw.json`).
- The repo's AMZN 10-Q was fetched from EDGAR (the only 10-Q PDFs in the repo were NVDA's/GOOGL's).

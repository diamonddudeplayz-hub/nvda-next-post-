# OSIS — Exhaustive Reading List for a Substack Post ("Primary Source Arbitrage")

*Everything a fresh Claude session needs to write the post. Hand it THIS file first; it maps every
source, the narrative arcs, the original data work, and the voice. Published blog: Primary Source
Arbitrage (darrenleung1.substack.com).*

---

## 0. READ FIRST (orientation, in this order)
1. **`README.md`** — the index + one-paragraph thesis + the "START HERE" pointer.
2. **`FINAL-DECISION.md`** — the whole thesis distilled: decision, **steelmanned bear case (8 pts)**,
   point-by-point bull rebuttal, the April-print resolver. *This is the spine of any post.*
3. **`MASTER-review-doc.md`** — self-contained thesis written for a cold outside reader (business →
   financials → thesis → targets → bear → risks → open questions). The closest thing to a draft.
4. **`12-historical-multiple.md`** — the ORIGINAL data work (29-yr P/E band). The most
   "primary-source-arbitrage" artifact in the file. *Lead candidate for the post's spine.*

## 1. THE FULL DOCUMENT SET (osis/) — what each holds
| File | Contains | Post use |
|---|---|---|
| `01-business-overview.md` | plain-English what-they-do; 3 segments; moat; the margin correction | background / "what is it" |
| `02-financials.md` | FY26 actuals, Q1 FY27, guidance, balance sheet, valuation | numbers/exhibits |
| `03-thesis-and-catalysts.md` | checklist scorecard, catalyst-hardness debate, **May-5/Aug-21 sell-off autopsy**, break conditions | the "why it fell" narrative |
| `04-consensus-and-segments.md` | LSEG consensus rev/EPS/EBITDA/FCF/shares; segment data; the **valuation correction (17x FY27, not 15x)** | consensus exhibits |
| `05-fact-check.md` | scrape-vs-LSEG reconciliation; what to verify | methodology/honesty |
| `06-peer-comps-and-verdict.md` | peer table + **Smiths Detection sold-to-CVC correction + 12.5x EBITDA transaction comp** | the private-market-anchor angle |
| `07-FAQ-and-deep-answers.md` | 16 deep Q&As: airports #2-3 not #1, moat, **gross-margin round-trip + operating-leverage bridge**, why it boomed/fell, verbatim 2H quotes, Nuctech, DCF/WC, buyback-vs-FCF | the richest single source of material |
| `08-backlog-coverage-seasonality.md` | coverage ratio (1.16x), **85% Security beat rate**, Q4-heavy seasonality, forward-quarter bars, external funding verification | the backlog/beat/seasonality exhibits |
| `09-valuation-model-and-targets.md` | SOTP, bull/base/bear P/E targets, reverse-DCF (market prices ~4% growth), Secure America Act | the valuation section |
| `10-catalyst-tracker.md` | prob-weighted targets, catalyst calendar, **position log (entered 10 Nov, 9 sh ~$199-200)** | the "where I sit" disclosure |
| `11-final-questions-and-risks.md` | 6 DD gaps, risk table, bull/bear one-paragraphs, **ownership (BlackRock/Fidelity/Janus added into the de-rate; founder+CFO ~3.3%)** | risks + ownership |
| `12-historical-multiple.md` | **trailing + forward P/E band, 2010-2026**, built from 29-yr prices + 20-yr EPS; median ~18x fwd; 27x was the peak | ⭐ the original quant centerpiece |
| `analyst-notes.md` | Oppenheimer x2, Roth, JPM-bear summaries; the "+11% FY2H27 organic inflection" call | sell-side framing |
| `transcripts/` | structured notes on 4 calls: **Q3 FY26 (the May-5 crash), Q4 FY26 (Aug-21 capitulation), Q1 FY27 (latest), BofA fireside (best plain-English)** | verbatim management quotes |

## 2. PRIMARY SOURCES (root + uploads referenced in the docs)
- **Filings (repo root):** `251248071.pdf` = OSI 10-K FY2025; `261502952.pdf` = OSI 10-Q Q1 FY27
  (Sep-30-2026, has the **RPO disclosure: $2.0B, 64% <12mo**). (FY26 10-K `261305871.pdf` was on `main`;
  re-checkout if needed: `git checkout origin/main -- 261305871.pdf`.)
- **LSEG estimate files** (user's TIKR/LSEG pulls, parsed into the docs): segment revenue (Security/
  Opto/Healthcare/Elim), consolidated rev/EPS/EBITDA/EBITDA-margin/FCF/shares, quarterly + annual
  back to FY2007; the **Shareholders Report** (ownership); **osio_max.xlsx** (29 yrs daily price).
- **Analyst PDFs:** Oppenheimer (Oct-30 + Sep-23), Roth (Oct-30), JPMorgan (Aug-28).
- **Screens (`screens/`):** `smallcap_screen.py` + CSV (the yfinance screen that surfaced OSIS);
  `osis_peer_regression.py` (correlation/z-score work showing OSIS is idiosyncratic).
- **External, web-verified:** CBP Jan-2026 NII testimony (>$1B OBBBA); Secure America Act ($3.45B CBP
  NII / $26B CBP through FY2029); Smiths Detection → CVC sale (12.5x EBITDA, 30-Jun-2026).

## 3. THE NARRATIVE ARCS (candidate angles — pick one spine)
1. **"The detection monopoly the market priced as a box-seller."** #1 in cargo, de-rated 37%, funded
   demand, reverse-DCF says the market prices ~4% growth for a 6-9% grower. The core long thesis.
2. **⭐ "Backlog isn't enough: conversion vs recognition."** The counterintuitive standalone essay —
   backlog set records all FY26 *while the stock fell 40%*, because the market pays for converted
   earnings, not booked backlog. An owner-vs-market-timing meditation. Very on-brand.
3. **⭐ "The P/E band nobody builds."** The 29-year empirical multiple study — the purest
   primary-source-arbitrage artifact. Kills the "it's cheap" narrative (17x ≈ the forward median),
   *and* kills the bear's "deserves 13-15x" (that's the trough). Lead with the data.
4. **"It all collapses to one variable."** Operating leverage = the revenue bet; the leverage amplifies
   EPS and the multiple together, both ways; the backlog skews it positive. A mechanics piece.
5. **"What CVC paid for Smiths Detection."** The private-market anchor (12.5x EBITDA) + the scarcity/
   takeout angle now that the only public pure-play is OSI.
6. **"Steelman your own idea."** The meta/honesty arc — how the thesis got *tightened* under pressure
   ("legally locked"→"visibility"; "cheap"→"median multiple"; the Smiths comp error corrected). Fits
   the self-correcting voice of the blog.
7. **Duration-framework application** — ties directly to the existing "When to Buy Is a Duration
   Question" post: OSIS as an Itron-shaped re-rate-with-a-floor; entry matters; buy decent at $199,
   clean at $177.

## 4. THE ORIGINAL / DEFENSIBLE DATA WORK (what makes it "arbitrage," not a summary)
- The **29-yr trailing + forward P/E band** (`12-`) — built from raw price + 20-yr EPS; sell-side
  doesn't publish this.
- The **coverage-ratio time series** (backlog ÷ LTM rev → 1.16x multi-yr high) (`08-`).
- The **85% Security beat-rate** history + the forward-bar decomposition (Q2 sandbagged, Q3/Q4 = the
  real test) (`08-`).
- The **reverse-DCF** (market pricing ~4% perpetual growth) (`09-`).
- The **operating-leverage bridge** (GM round-trip 36→33 while *operating* margin doubled 8.3→12.6 on
  SG&A+R&D leverage; raw opex +51% vs revenue +86%) (`07-` §15).
- The **idiosyncratic-correlation regression** (OSIS 0.17-0.31 corr w/ peers → pairs-timing won't work)
  (`screens/`).
- The **private-market comp** (CVC/Smiths Detection 12.5x vs OSI 12.2x) (`06-`).

## 5. THE HONEST CORRECTIONS (include these — they ARE the credibility)
A post that only sells the long is weak. The file's value is the *corrections made under pressure* —
show them:
- "#1 in airports" → **#1 in cargo, #2-3 in airports** (behind the now-private Smiths Detection).
- "Margin-expansion flywheel" → **margins modeled FLAT; it's a revenue + operating-leverage story.**
- "Legally locked $26B funding for OSI" → **strong multi-year visibility; appropriations are agency-
  level, IDIQ ceilings ≠ spend.**
- "Cheap at 17x" → **17x ≈ the forward median; fair, not cheap; margin of safety is the business, not
  the multiple.**
- "Cheaper than Smiths (22x P/E)" → **wrong comp; Smiths Detection went private; use the 12.5x deal.**
- EV walked from a too-rosy +16% to a **defensible ~+6-10%** with a real −32% left tail.

## 6. VOICE / STYLE (match the blog)
- **Primary-source-driven**, framework-first, **intellectually honest / self-correcting**, data-backed,
  conversational-but-rigorous. Not promotional. States the bear at full strength.
- Recurring devices: the **duration lens**, the **"catalyst = removes the reason the market resisted"**
  idea, **standard-deviation / drawdown empirics**, **"what would change my mind"** sections.
- **Disclosure:** author holds a starter (9 sh, entered ~$199 on 10 Nov 2026), plans to add on a leg
  down toward the 200-week (~$177). Not investment advice. (See `10-catalyst-tracker.md`.)
- End with a concrete **"what would change my mind"** = the April Q3 FY27 print (revenue vs +10% bar,
  operating-margin leverage, service growth, Middle East conversion).

## 7. ONE-LINE THESIS (the post's through-line)
**A regulation-moated #1 cargo-detection business, de-rated 37% to its forward-median multiple, with
funded, contracted, non-discretionary demand (RPO $2.0B / 64% <12mo) the market is pricing at ~4%
growth — where the return is EPS growth + a re-rate the market has a decade-long habit of granting,
the margin of safety is the business not the price, and the whole thing resolves at the April print.**

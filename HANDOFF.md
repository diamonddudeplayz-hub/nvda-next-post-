# Handoff — GOOGL / hyperscaler thesis (for a fresh reviewer)

Pick-up doc for another Claude (or human) reviewing this work. **Your job is to red-team it, not agree
with it.** The author (Darren) built a bull thesis on GOOGL with AI assistance and is aware AI leans
agreeable — so the valuable contribution is finding what's *wrong*, not restating what's right. Hunt for
the holes. Price context: **GOOGL $265.29, AMZN $246.82, MSFT $484.52 (Nov 20, 2026 close).**

## What was done
Three full hyperscaler deep-dives (GOOGL, AMZN, MSFT) from primary sources — 4 earnings calls each, the
Q3-2026 10-Qs (pulled from EDGAR), 20-yr LSEG estimate files (parsed from TIKR exports via raw XML),
sell-side notes — plus a thesis spine, a 3-way scorecard, and two reverse-DCFs.

## The conclusion (what to attack)
**GOOGL as the core long**, taken as a *small starter* at ~10x FY27 EV/EBITDA / 17.8x FY27 EPS. Thesis:
priced for a stall (reverse-DCF ≈ 0–3% perpetual growth); demand is proven not hoped ($561B Cloud
backlog → capacity not demand); Search (the one risk) is being monetized + margin-defended by a falling
TPU-driven cost-to-serve; free optionality (TPU merchant business, Waymo ~$126B, 1B unmonetized Gemini
users). AMZN = business-momentum add-on-dips; MSFT = quality-on-a-flush; small NVDA stub.

## Read in this order
1. `00-THESIS-why-hyperscalers.md` — the spine (risk ladder: labs → neoclouds → hyperscalers; rent-to-whom).
2. `HYPERSCALER-SCORECARD.md` — the 3-way comparison + rankings.
3. `googl/05-DECISION-capstone.md` — the decision, EV/EBITDA re-rate table, dashboard, kill-switch.
4. `googl/00-verdict-and-edge.md` → `01` → `02` → `03` (2nd-opinion response) → `04-reverse-dcf.md` — the GOOGL chain.
5. `amzn/` and `msft/` folders — the comparables.

## Open holes to pressure-test (start here — these are where it's weakest)
1. **The DCF is terminal-dominated and inconclusive.** Fair value swings $182 (FCF-file path) to $408
   (direct-capex path) on the capex assumption. The bull case leans on the *direct-capex* file (capex
   peaks 2028, declines) — is that analyst optimism? Management hasn't guided a 2028 peak. Rebuild it.
2. **Search monetization (RPM) is unprovable today.** The whole thesis rests on AI-Mode commercial-query
   RPM holding/recovering. Google doesn't disclose RPM. Is the "cost-to-serve defends the margin" argument
   actually enough if RPM falls faster than cost? Model it.
3. **It's partly a rates/duration bet.** Discount rate is the biggest DCF swing (9% → +54%, 11% → +9%).
   Fed is priced to hike more. Does the thesis survive higher-for-longer?
4. **Crowded-but-cheap.** Consensus-loved (Street Strong Buy, r/ValueInvesting darling), passive-dominated
   holder base, at a 52-wk low. Less edge than it feels; harder unwind if wrong.
5. **TPU uniqueness was overstated and corrected** — AMZN's Trainium matches it. Verify the own-silicon
   edge is real vs talked-up.
6. **EPS is GAAP/lumpy** (equity marks + D&A optics). Confirm EBITDA/FCF are the right lenses and the
   numbers tie.
7. **META is undone** — the 4th name, no cloud, single-threaded ads. Not required for the core call but
   completes the map.

## Instruction to the reviewer
Don't validate. **Find the strongest version of the bear case** — especially on (a) whether capex
actually rolls over, (b) whether Search RPM can structurally free-fall despite the cost defense, and (c)
whether the rate environment breaks the valuation. If after genuinely trying to break it the thesis still
stands, *that's* the useful signal. Rebuild at least one number yourself (the reverse-DCF or a Search-
bear EPS model) rather than trusting the ones here.

_Branch: `claude/intelligent-euler-em3g9a`. All source files (xlsx, 10-Q text, PDFs) are in the repo._

# GOOGL: Cloud-margin drivers, the TPU business, the Feb-3 capex setup, and the unmodeled levers

Addendum #2. Answers: why Cloud margin keeps climbing (and what caps it), what the TPU business
actually *is* and whether they're selling now, what the Feb-3 2027 capex guide likely implies, and
how much the "other" AI levers could be worth. Price anchor **$265.29**.

---

## 1. Cloud operating margin — the thesis for "it keeps climbing," and what caps it
Trajectory: **23.7% (Q3'25) → 32.9% (Q1'26) → 35.6% (Q2) → 36.2% (Q3'26).** Nearly doubled in a year.
Directional segment EBITDA margin (n=1, thin): ~55% ('26) → ~53% ('27) → ~58% ('28).

**Drivers that push it higher:**
1. **Operating leverage.** Revenue +103% on a largely fixed base (data centers, core R&D, platform).
   Cloud is past the fixed-cost hump — incremental revenue drops through at high margin. This is the
   biggest driver and the most durable.
2. **Own-silicon economics (TPU + Axion).** Google's cost per unit of compute is structurally below
   renting NVIDIA GPUs. Kurian: payback on AI servers **<2 yrs, own silicon ~half that**. Every
   workload Google serves on its own TPU instead of a bought GPU is margin it keeps instead of paying
   to NVIDIA. Vertical integration = the margin moat.
3. **Mix shift to software/solutions.** Gemini Enterprise, Vertex, BigQuery AI, Wiz security are
   higher-margin than raw infrastructure, and AI-using customers buy **1.8x more products**. As the
   mix tilts to software, blended margin rises.
4. **Pricing power.** "Demand exceeds supply" all year → they don't have to discount.
5. **Utilization.** Capacity built ahead of demand fills up → fixed costs amortize over more revenue.

**What caps it (the honest caveat — why margin could plateau even as profit grows):**
1. **TPU *hardware* system sales are lower margin.** Selling TPU systems into customers' own data
   centers books gross hardware revenue at a thinner margin than cloud subscription. As this ramps in
   2027, it **dilutes the segment margin %** even while adding absolute profit. (This is why the
   directional 2027 EBITDA margin dips to ~53% before recovering.)
2. **3rd-party "bridging capacity."** Renting outside compute to meet overflow demand is expensive —
   management explicitly flagged this as a **near-term margin headwind for Q4'26 / H1'27**.
3. **Depreciation.** The ~$217B→$337B capex flows into D&A, which hits the Cloud P&L on a lag.

**Net read:** **absolute Cloud profit almost certainly rises a lot** (operating leverage + own-silicon
win). **Cloud margin *%* is the thing to watch** — it may plateau in 2027 as TPU hardware + bridging
dilute, then re-expand. So in the model, lean on Cloud *dollars of operating income*, not the margin
percentage, and treat a 2027 margin wobble as expected, not a thesis break.

---

## 2. The TPU business — what it is, and yes, they're already selling
Three distinct things get called "TPU," only one of which is new:

| Mode | What it is | New? | Status |
|---|---|---|---|
| **Internal** | Google trains/serves Gemini, Search, YouTube on its own TPUs | 10 yrs old | mature, the cost moat |
| **Cloud rental** | customers rent TPU compute via GCP/Vertex | years old | ~100 TPU customers, growing |
| **TPU *system* sales** | Google sells the **hardware system** (chips + networking + software) into customers' **own data centers** | **new in 2026** | **actively selling — first revenue Q2'26, ramping, bulk in 2027** |

**Are they already selling? Yes.** From the calls: Google "began to recognize revenue from TPU system
sales, delivered to customer data centers for the first time in Q2 2026," ramping through H2'26 with
"the vast majority of revenue in 2027." The mechanics show up in the 10-Q: **inventory jumped $2.4B →
$13.3B** (building systems ahead of delivery), and the **$560.8B Cloud backlog** includes these
multi-year commitments. Cash cycle: sign contract → backlog → build inventory (cash out) → deliver +
bill (revenue + cash in) — different from renting, which is why it distorts near-term FCF.

**Who's buying:** Anthropic (direct + via Broadcom), **Apple (pretraining its foundation models on
TPU)**, Citadel, Jump, Physical Intelligence, Mirendil — plus **distribution partners** Oracle, Crux
AI (the Blackstone JV, $16.8B commitment in backlog), and Broadcom. TorchTPU (built with Meta) lets
PyTorch run on TPU, lowering the switching cost.

**Why it matters to the thesis:** this is the leg that doubles as the **structural NVDA short** —
every TPU system shipped is AI compute demand that doesn't pay NVIDIA's ~75% gross margin. Apple and
Anthropic choosing TPU is the real tell that the merchant-silicon business is credible, not a science
project. It's lower-margin than cloud rental (see §1) but it **expands the addressable market** to
customers who want hardware on-prem and **offsets Google's own capex** (customer pays for the power/
space). It's early-innings and mostly a 2027 revenue event.

---

## 3. Feb 3, 2027 (Q4/FY26 print) — the capex guide is the headline risk
**Capex trajectory (actual → consensus-implied):**
| | 2024 | 2025 | 2026E | 2027E | 2028E |
|---|---|---|---|---|---|
| Capex ($B) | 52.5 | 91.4 | **~205–217** (guide $195–205) | **~337** | **~396** |

Consensus already implies **2027 capex ~$337B, +56% over 2026 (~+64% over the $205B guide midpoint).**

**What management has signaled:** they **raised the 2026 capex guide three times** this year
($175–185B → $180–190B → $195–205B) and have repeated "supply-constrained / demand exceeds supply"
every quarter. For 2027 they've only said **"increase significantly"** — detail comes **Feb 3.**

**Likely above or below?** The honest answer:
- **The base case is a big number, and the risk is skewed HIGH, not low.** The upward-revision pattern
  + supply constraints + the backlog ($568B) + "2027 significantly increase" all point to a 2027 guide
  in roughly the **$300–375B** range. Consensus ~$337B is a reasonable anchor; I'd bias the *risk* to
  the upside of that (they've out-guided every quarter).
- **The stock reaction is not about the level — it's about the framing.** A $330–350B guide *with*
  backlog/ROIC visibility = in-line, digestible. A guide **above ~$375B**, or one without matching
  demand signals, deepens the **3-year FCF desert** ($20B→$61B→$32B negative) and is the near-term
  negative catalyst. A guide **below ~$300B** would be read as capex discipline → relief rally (less
  likely given the setup).
- **Key nuance:** a high capex guide is *itself a demand signal* — Google only spends if ROIC clears
  (they say so every call). So "capex shock" cuts both ways: bad for near-term FCF optics, bullish for
  the revenue that spend implies. The market's mood (VIX ~36) decides which it trades on first.

**Q4 EPS consensus $3.13** (range $2.20–3.48 — the wide range is OI&E/equity-mark uncertainty, not
operational). Revenue should be fine (Cloud momentum + seasonal Services strength); **Services growth
+ Cloud operating margin + the 2027 capex number are the three things that move the stock on Feb 3.**
Net: **expect a large capex guide; the question is whether it's framed with demand. That's the risk,
and it's partly already in the ~$337B consensus.**

---

## 4. The unmodeled levers — how much could the "other" AI businesses add?
Most of the six legs are *partly* in consensus (Workspace sits in Services subs; Vertex/Enterprise in
Cloud). The genuinely **under-modeled** upside is mostly **optionality / asset value**, not near-term
EPS. Rough, illustrative sizing (assumptions stated — directional, not a model):

| Lever | Why it's under-modeled | Illustrative value/revenue potential |
|---|---|---|
| **Gemini app consumer monetization** | 1B MAU, **almost no ads yet** ("free tier + subs; ads when the time is right") | Meta ARPU ~$50/user/yr globally. Even **$10–20/user on 1B+ = $10–25B** high-margin revenue not in estimates |
| **Google One AI subscriptions** | fastest-growing sub; early | 50–100M paid AI subs × ~$120–240/yr = **$6–24B** |
| **Gemini Enterprise** (Copilot slot) | 100M+ seats, many bundled/trial today | monetized at ~$10–30/seat/mo eventually → **$10–30B+ ARR** (partly in Cloud already) |
| **Waymo** | loss-making in Other Bets; not in earnings | private val **~$126B (Feb'26)**; at scale (20+ cities) plausibly **$100–350B** asset value |
| **Isomorphic Labs** | AI drug discovery; raised $2B+ | lottery-ticket optionality; milestone/royalty upside |
| **Agentic commerce (UCP)** | new; take-rate not modeled | optionality on the entire shopping funnel |

**How to think about it for *us*:** the core thesis (Cloud compounding + Search holding) **does not
need any of these** — they're **free call options**. Sum the under-modeled pieces and you're plausibly
looking at **$200–500B of equity value** (Waymo + consumer Gemini monetization + enterprise AI ramp)
that a **17.8x FY27 multiple isn't paying for**. The way this helps the trade isn't "+X to FY27 EPS" —
it's that **the downside is cushioned** (you own a portfolio of AI call options for free) and the
*long-tail upside* is real if any one of them (most likely consumer Gemini ads, then Waymo) inflects.
That's the structural answer to the bear's "$1T of commitments" — Google has the widest set of ways to
turn that spend into revenue of any name in the complex.

---

## 5. Entry point & final verdict
- **Is $265 a good entry? Yes — to *start* a scale-in.** 17.8x FY27 (below the 2022 trough), 52-week
  low, de-rate driven by a Search fear the share data contradicts, six monetization legs, net cash
  ~$115B, Cloud compounding ~90%/yr. The risk/reward skews ~2:1 favorable with a cushioned left tail.
- **But scale, don't lump.** It's high-beta (β 1.23); a broad VIX flush (VIX ~36 now) can take it to
  **$230–240** (~15–16x FY27), where the skew gets fat. **Buy a starter here, keep powder for the
  flush, add on the Feb-3 capex reaction if it over-reacts to a big number.** Unlevered — size so a
  move to $230 is a "add," not a "forced sell."
- **Role:** core **ballast** in the barbell (self-funding ROI-capturer + alternative silicon) against
  a small **NVDA torque stub**. It won't 2–3x like the levered neoclouds in a V-recovery; it's the
  best **Sharpe** in the derated-AI group — biggest drawdown relative to least fundamental damage.
- **The one number that decides it:** AI-Mode monetization of commercial queries (watch Services
  growth re-accel in H1'27 + global search share in the alt-data). Everything else is secondary.

**Final verdict: GOOGL at $265 is the cleanest, lowest-idiosyncratic-risk way to own "AI ROI is real,"
and the de-rate to the 52-week low is the market handing it to you on a Search fear the data doesn't
support. Start the position here, scale into weakness, hold as core.**

---

## 6. If you want an external/second opinion — what to hand them
- **The one doc to send: `00-verdict-and-edge.md`.** It's self-contained — thesis, the bull edge, an
  honest bear, the scenario frame, and the verdict — written so someone with no context can engage.
- **Pair it with the evidence** if they want to dig: `estimates-consensus.md` (the numbers),
  `10q-q3-2026.md` (the balance-sheet/commitments reality), and this doc + `01-followups…` (margin,
  TPU, Search mechanism). The chart `googl-price-vs-multiple.png` is the one-glance de-rate picture.
- **My thoughts on soliciting the external view:** do it, and point them at the **two things a smart
  bear will attack** so you pressure-test the real risks, not strawmen:
  1. **"AI-Mode monetization is hope, not proof."** The bear will say CTR/ad-load on AI answers is
     unproven and management is talking its book ("already similar," "incremental"). This is the only
     thesis-killer — make them argue the *commercial-query* monetization specifically, not publisher
     CTR (which is a red herring, per `01-followups`).
  2. **">$1T of commitments + 3 years of negative FCF."** The bear will say ROIC is unproven and the
     commitments are a trap if AI demand softens. Fair — the rebuttal is OCF is accelerating, backlog
     is $568B, and the levers in §4. Also push them on **Cloud revenue quality** (the TPU hardware
     gross-up) — a good bear will note the top line flatters the story; your answer is "judge it on
     operating income, which is also compounding."
  - A genuinely useful second opinion will either (a) give you conviction the Search-monetization bear
    is overblown, or (b) find a data point that says AI-Mode commercial monetization is structurally
    worse — which is the one thing that would make you *not* own it. Everything else is noise around a
    cheap, high-quality, net-cash compounder.

_Want a polished standalone 1–2 page investor memo (no internal shorthand) to actually send someone?
Say the word and I'll generate it from `00-verdict-and-edge.md`._

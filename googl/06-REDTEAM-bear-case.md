# GOOGL red-team — the strongest bear case (Nov 22, 2026)

Commissioned pushback on the long. The brief was explicit: *don't agree, try to break it.* I rebuilt the
reverse-DCF from the raw LSEG files (`_redteam_dcf_rebuild.py`), built a Search-RPM model
(`_redteam_search_bear.py`), and read the bear sell-side (JPM "Structural Search Slowdown", Wells Fargo
"Search Concerns Intensify"). Price anchor **$265.29**. This is the adversarial doc; the bull chain is `00`–`05`.

---

## Verdict first (so it's not buried)
**The thesis does not fully survive in the form it's written.** It survives as a *name* — GOOGL is the
cleanest, lowest-idiosyncratic-risk hyperscaler, net cash, real optionality, and the franchise is not
broken. It does **not** survive as a *valuation* claim. The "priced for a stall, 2:1 reward/risk, fair
value $300–340" framing rests on two optimistic choices that, when corrected, collapse the margin of
safety to roughly nil:

1. **The capex that "rolls over"** is the single most optimistic LSEG file, contradicted by the other
   LSEG file by ~$80B/yr and by management's own behavior.
2. **The discount rate** the base case leans on (10%) is *below* the ~11% cost of equity the thesis
   itself computes from CAPM.

Correct both and my rebuilt fair value centers **~$250–285 — i.e. the stock is roughly fairly valued,
not cheap.** You are being paid a *small* premium to take a *real, already-materializing* structural
risk on the single biggest profit pool. That can still be an OK starter at small size — but it is not
the asymmetric setup the capstone describes.

**And one thing you're outright wrong about — important enough to lead with:**

---

## The thing you're most wrong about: the kill-switch watches the wrong gauge
Your kill-switch (`05-DECISION-capstone.md`) is **"Search decelerates again *with global share rolling
over*."** Global search share is a **volume/demand** metric. But your own documents concede the whole
call is **monetization per query (RPM)**, not volume. These two can — and right now *do* — move in
opposite directions:

- **Q3 reported:** search **sessions +36% y/y**, but **paid clicks only +9–10% y/y** (Wells Fargo, off
  the 10-Q). That ~26-point gap *is* RPM-per-session falling, **inside Google's own funnel** — not
  publisher CTR, not third-party sites. It is the exact variable you said decides the thesis, and it is
  already deteriorating.
- Global share can sit at 91% for years while RPM-per-session craters. **Your kill-switch would not
  fire on the thing that is actually happening.** You'd hold all the way down because the gauge you're
  watching (share) stays green while the gauge that matters (monetization) bleeds.

This is the core red-team finding: **the bull chain repeatedly reassures on the variable it admits
doesn't matter (query volume, 91% share, "query growth at a 5-year high") and treats the variable it
admits is "the whole call" (commercial-query RPM) as *future optionality* — when Q3 shows it's a
*present* headwind.** Fix the dashboard: the tell is the **sessions-vs-paid-clicks spread** and **Google
Services operating margin**, not share. On both, the needle is already moving the wrong way (Services
margin printed **40.7% vs ~43.5% expected** in Q3).

---

## Attack 1 — Does capex actually roll over? (the biggest DCF lever)
**Short answer: the "capex peaks 2028 then declines" fact is the weakest load-bearing assumption in the
whole model, and it's doing most of the valuation work.**

What the raw files actually say (pulled from `Estimate Details GOOGL.O (11) capex.xlsx`, Mean row):

| | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| **Direct-capex file** (the bull primary) | 201 | 327 | **376** | 313 | 298 |
| **# analysts** | 29 | 29 | 26 | **8** | **7** |
| High / Low (2029) | | | | **461 / 117** | |
| **Capex implied by the LSEG FCF file** (OCF − FCF) | — | 337 | 396 | **380** | **384** |

Three problems, each independently damaging:

1. **The two LSEG files disagree by ~$80–86B/yr in 2029–30.** One says capex *declines* to ~$298–313B;
   the other says it *stays elevated* at ~$380–384B. You picked the lower one as "primary" and called it
   "the cleaner number." That single choice is worth **~$97/share** (see the rebuild below). It is a
   coin-flip between two files from the *same vendor*, resolved in the bull's favor.
2. **The "decline" is a 7–8-analyst artifact with a 4x dispersion.** FY29 estimates range $117B→$461B.
   The *median* FY29/30 capex is actually **~$320B / ~$311B — higher than the mean you used** ($313/$298),
   because two outlier analysts modeling a capex *cliff* ($117B, $121B) drag the mean down. Strip the
   outliers and capex **plateaus ~$310–320B, it doesn't roll over.**
3. **It contradicts management.** Alphabet *raised* 2026 capex guidance three times and guided 2027
   "significantly higher." Your own `02-…` doc says the near-term risk is **skewed high**. So the model
   assumes a far-out decline that only a handful of analysts forecast, while conceding the near-term
   surprises are to the upside. That's internally inconsistent — you can't lean on "capex discipline =
   FCF inflection" for the terminal value while saying the Feb-3 guide risk is to the upside.

**The deeper issue: the DCF is terminal-dominated.** In my rebuild, **60–71% of the entire EV is the
terminal value** (FCF a decade out), and FCF doesn't turn meaningfully positive until 2029 — a number
supported by **3–4 analysts**. You are not valuing proven cash flow; you're valuing an extrapolation off
the thinnest, least-reliable corner of the estimate set, and the extrapolation's starting point is the
more-optimistic of two contradictory files.

---

## Attack 2 — Can Search RPM structurally free-fall despite the cost defense? (yes)
**The "falling TPU-driven cost-to-serve defends the Search margin" argument is structurally weak, because
it defends the small side (cost) against a risk on the big side (revenue).** Model in
`_redteam_search_bear.py`:

- Search ad pool ~**$220B**; the serving/compute cost that TPU efficiency can actually bend is ~**$18B**
  (generous). **Revenue-per-query is ~12x cost-per-query.**
- So a **1% RPM decline** (~$2.2B revenue, ~80% incremental margin) requires a **~12% cut in *all* Search
  serving cost** just to break even. A heroic 50% TPU-driven cost cut saves ~**$9B** — against revenue
  hits that run to **$20–60B** once RPM falls on a meaningful share of commercial queries. **Cost
  efficiency is an order of magnitude too small to be a "defense."**

Operating-income impact (after a *generous* $9B cost offset), by share of commercial queries moving to
AI answers (X) × RPM haircut (r):

| | r = 15% | r = 30% | r = 45% |
|---|---|---|---|
| **X = 30%** | ≈ flat | −$7B (−4% EPS) | −$14B (−8%) |
| **X = 50%** | −$4B (−2%) | −$17B (−9%) | −$30B (−17%) |
| **X = 70%** | −$9B (−5%) | −$27B (−15%) | −$46B (−25%) |

And this is **not hypothetical** — it's in the Q3 print and the bull sell-side concedes it:
- **JPMorgan (Overweight, PT cut $425→$375):** "AI Mode lags traditional search in **both coverage & ad
  load**, resulting in **lower overall monetization**… Search shortfall (high-margin revenue) likely
  contributed to lower Google Services margin — **40.7% vs. our 43.5% estimate**."
- **Wells Fargo (Overweight, PT cut $417→$371):** sessions **+36%** vs paid clicks **+9–10%**, "driven
  by **decreasing ad coverage and falling click-through rates**"; **AI Overviews penetration of US
  results doubled to 79%** (from 35% in Q2).

Your `01-followups` doc argued the scary CTR data (Pew/Seer) is "publisher pain, not Google pain." That
rebuttal is real for *publisher* clicks — but it **does not touch the sessions-vs-paid-clicks gap, which
is Google's own metric.** The decoupling is happening one level up, inside Google's funnel, exactly where
it hurts revenue. The bull chain answered the weaker version of the bear and left the stronger version
standing.

**The uncomfortable cross-check:** a structural RPM break is roughly what $265 *already embeds* (the
de-rate ≈ a ~19% FY27 EPS haircut ≈ ~$40B OI ≈ X≈50%/r≈45%). So the bear isn't "unpriced" — it's
approximately *in* the price. That cuts both ways: the downside may be partly discounted, **but it also
means the upside requires RPM to *hold/recover*, which is the one thing nobody can prove and which the
Q3 data is currently contradicting.** You're not buying a mispriced fear; you're buying a correctly-
identified, actively-worsening risk at a price that reflects it.

---

## Attack 3 — Does higher-for-longer break the valuation? (largely, yes)
The base case leans on a **10% discount rate**. But the thesis's own CAPM math is **rf 4.9% + β1.23 ×
5% ERP ≈ 11.05%.** The 9–10% used in the headline grid is a *below-CAPM* "quality mega-cap deserves it"
nudge. In a higher-for-longer world (the Fed priced to hike, per the handoff), the honest rate is **11%+**.

My rebuild at an **11% discount rate**:
- Direct-capex (optimistic) path: **$265–288** — i.e. roughly *fair value to +9%*.
- FCF-file (capex-stays-elevated) path: **$185–201** — i.e. **−24% to −30%.**

So the "cheap" conclusion is substantially a **duration bet**. Every piece of the bull valuation that
looks like margin of safety evaporates if you (a) use the CAPM rate the thesis itself derived and (b)
blend the two capex files instead of picking the favorable one. Net cash makes GOOGL the *most* rate-
defensive of the three hyperscalers — but "most rate-defensive" is not "rate-immune," and a terminal-
value-dominated DCF is *maximally* sensitive to the discount rate (71% of value in the TV at 9%).

---

## The rebuilt DCF (my numbers, reproducible in `_redteam_dcf_rebuild.py`)
Same framework as your `04`, same source data, TV decomposed. Fair value per share:

| Capex path → | **Direct-capex file** (bull primary) | **FCF file** (capex stays ~$380B) |
|---|---|---|
| **9% WACC** | $390 | $274 |
| **10% WACC** | $324 | $227 |
| **11% WACC** (CAPM) | **$275** | **$192** |
| **12% WACC** | $238 | $166 |
| *terminal value as % of EV* | *60–71%* | *~69%* |

- **Your reported $339 base** sits at the intersection of the two most favorable choices (optimistic
  capex file + sub-CAPM 10% rate). It is a *corner*, not a *center*.
- **The honest center** (blend the capex files ≈ "capex plateaus, doesn't roll over"; CAPM ~11% rate) is
  **~$250–285.** The stock at $265 is inside that range. **Fairly valued, not cheap.**
- **The reverse read still holds directionally** — the market is pricing low/no long-term growth — but
  "the price embeds ≈0% perpetual growth" was computed on the *optimistic capex path*. On the blended
  path the implied terminal growth at $265 is **~+1.5–3%**, i.e. GDP-ish, not "slow decline." The
  "paying for a shrinking business" claim is overstated by one capex-file choice.

---

## What genuinely survives the attack (steelman, because fairness cuts both ways)
1. **GOOGL is the right *relative* pick** of the hyperscalers — net cash, cheapest, most-derated, owns
   frontier model + silicon. Nothing here argues for AMZN/MSFT over it.
2. **The franchise is not impaired.** Operating income +30%, Cloud +103%, op margin rising. This is a
   *monetization-transition* risk, not a *demand-collapse* or solvency risk. The left tail is a slow
   de-rate you'd see coming — categorically better than NVDA/neocloud tails.
3. **The optionality is real and mostly free** (Waymo, TPU merchant, 1B Gemini users, YouTube). It
   cushions the downside even if it's not in the EPS.
4. **The sizing discipline is correct.** "Small starter, scale into weakness, unlevered, cut on
   confirmation" is exactly right for a thesis whose central variable is unprovable today. The *process*
   is sound even where the *valuation framing* is too generous.

---

## Net: what to change
- **Downgrade the valuation claim** from "2:1, fair value $300–340, priced for a stall" to **"roughly
  fairly valued (~$250–285), being paid a thin premium for real, already-materializing RPM risk."** The
  asymmetry is closer to **~1.2:1**, not 2:1 — which your `03` second-opinion response already half-
  conceded (1.4:1) and which the capex/rate corrections push further toward parity.
- **Fix the kill-switch.** Replace "global share rolls over" with **"sessions-vs-paid-clicks spread keeps
  widening"** + **"Google Services operating margin keeps falling."** Those are already triggering. Decide
  now whether that's your line — because your current line (share) will stay green through the whole bear
  case.
- **Don't anchor the DCF on the favorable capex file.** Use the blend, or at minimum show the blended
  center as the base and the direct-capex path as the *bull*, not the primary.
- **Respect the rate.** Underwrite at 11%, not 10%. If you need a sub-CAPM rate to make it cheap, it
  isn't cheap.
- **Keep it small, and let it fall.** Everything above argues for exactly the sizing you chose — just not
  the conviction. The honest one-liner is: *"cleanest name in a hard neighborhood, bought mid-transition
  at roughly fair value, where the thing that decides it is already going the wrong way."* That's a
  defensible *starter* — it is not the mispriced bargain the capstone implies.

_Built from the same primary sources (LSEG capex/OCF/FCF files, Q3 10-Q, JPM + Wells Fargo bear notes).
Models: `_redteam_dcf_rebuild.py`, `_redteam_search_bear.py`. Adversarial by assignment — weight it
against the bull chain, don't take it as the last word._

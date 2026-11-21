# GOOGL follow-ups: historical multiple, TPU calibration, the Search mechanism, AI product stack, and "best derated name?"

Addendum to `00-verdict-and-edge.md`, answering Darren's Nov 21 follow-ups. Chart:
`googl-price-vs-multiple.png`. Price anchor still **$265.29 (Nov 20 close)**.

---

## 1. Historical multiple — where the de-rate actually sits (the chart)
Year-end **trailing** P/E, 2006–2025 (price ÷ that year's actual EPS):

| | '16 | '17 | '18 | '19 | '20 | '21 | '22 | '23 | '24 | '25 |
|---|---|---|---|---|---|---|---|---|---|---|
| Trailing P/E | 23 | 33 | 24 | 27 | 30 | 26 | **19** | 24 | 24 | **29** |

- **10-yr average trailing P/E ≈ 26x.** The stock has only been below ~20x **twice** in the modern
  era: the **2008 GFC (16x)** and the **2022 rate-shock bear (19x)**.
- Today: **17.8x forward** (FY27 clean EPS $14.88); ~24.5x trailing on 2025's $10.81. So the
  *forward* multiple is **below the 2022 trough**, and it's on **higher, Cloud-driven growth** than
  2022. That's the quantified "de-rate to historical cheap": you're paying a crisis-trough multiple
  for a non-crisis business.
- **Price-vs-estimates match (top panel):** price tracked earnings up and to the right for 20 years;
  it ran *ahead* of earnings into the Dec-25/May-26 top (29x → $402), then the multiple — not the
  earnings — collapsed. Estimates have held/risen while the price fell 34%. **Classic de-rate:
  multiple compression, not estimate cuts.** That's the single most important picture in the folder.

**Caveat:** trailing P/E is noisy here because GAAP EPS swings on equity marks (OI&E). The *clean*
way to see it is forward EV/EBITDA: **10.3x FY27 / 7.9x FY28** vs a stock that traded 15–18x
EV/EBITDA for most of 2024–25. Same conclusion.

---

## 2. TPU / Cloud "on top" — what the estimates already embed, and how calibrated
You called TPU "free optionality." Be precise: **it's not free anymore — consensus already bakes in
a massive Cloud/TPU ramp.** That changes what the edge actually is.

**Cloud revenue, quarter by quarter (actuals → consensus):**
| | Q4'25 | Q1'26 | Q2'26 | Q3'26 | Q4'26E | Q1'27E | Q2'27E | Q3'27E | Q4'27E |
|---|---|---|---|---|---|---|---|---|---|
| Cloud rev ($B) | 17.7 | 20.0 | 24.8 | **30.7** | 36.8 | 42.8 | 47.2 | 53.9 | 59.3 |

- Annual Cloud: **$58.7B ('25) → $112B ('26E, +91%) → $209B ('27E, +87%) → $323B ('28E)**.
- Cloud goes from **~15% of revenue ('25) to ~33% ('27E)**. Directional segment EBITDA (n=1, thin):
  Cloud **$62B ('26E) → $111B ('27E) → $186B ('28E)** — i.e. Cloud becomes **~half of consolidated
  EBITDA by '28** if roughly right.
- **So the estimates ALREADY "go there."** The $209B FY27 Cloud number *is* the TPU-system ramp
  (mgmt: TPU system revenue "mostly a 2027 event"; Anthropic/Apple/Oracle/Crux deliveries). The
  market has it in the model — it's just discounting it at a low multiple because it's trapped inside
  a "Search is dying" stock.

**What's genuinely still underpriced (the real TPU edge):**
1. **Margin/mix surprise** — if TPU + Cloud operating margin keeps climbing (36.2% in Q3'26, from
   23.7%), the profit flow-through beats the revenue-heavy model.
2. **Merchant-silicon TAM** — selling *systems* to Anthropic, Apple, Oracle, Crux, Broadcom is a
   business the market barely capitalizes and that **structurally shorts NVDA scarcity**. That strategic
   value isn't in a 10x EV/EBITDA.
3. **It's the hedge leg** — every TPU deployed is AI demand that doesn't pay NVDA's margin. Owning
   GOOGL Cloud/TPU is the cleanest listed "un-scarce the shovel" position.

**How calibrated is consensus near-term? (next print: Feb 3, 2027 — Q4/FY26)**
| Metric | Q4'26 consensus | Read |
|---|---|---|
| EPS | **$3.13** (n=39, range 2.20–3.48) | wide range = OI&E/mark uncertainty |
| Cloud rev | **$36.8B** (+20% QoQ) | **achievable-to-beatable** — Cloud has beaten + accelerated 4 straight Qs |
| Services rev | **$104.6B** (seasonal) | **the at-risk line** — FX headwind + lapping 2025 Search accel (mgmt flagged) |
| EBITDA | **$64.0B** | smooth low-teens sequential; the reliable series |
| FCF | **−$15.2B** | negative every quarter through '27 — the desert is in the model |

**Calibration verdict:** consensus looks **beatable on Cloud/TPU** (momentum + the Q4 TPU ramp),
**at-risk on Services** (Search/FX/comps), with the real swing factors being **(a) Cloud operating
margin** (3rd-party "bridging capacity" is a flagged near-term drag) and **(b) the 2027 capex number**
mgmt gives on Feb 3 — consensus implies **~$337B (+60%+ over '26)**. If capex blows past that with no
incremental backlog, the FCF trough deepens. Net: the setup into Q4 is "Cloud carries, Search is the
variable, capex guide is the headline risk."

---

## 3. The Search question, stated plainly — "is it all about whether AI Mode keeps the ad revenue?"
**Yes. That's the whole call, and the mechanism is advertising per query.** Here's the chain:

- Search monetizes as **ad impressions × click-through rate (CTR) × price per click.** Traditional
  search = query → ads + 10 blue links → user clicks an ad. AI Mode/AI Overviews = the AI *answers
  the question*, so there are fewer slots and fewer reasons to click. **If Google can't put equally-
  monetizing ads inside the AI answer, revenue per query falls** even if usage rises.
- **The bull mechanism (why it may hold):** Google is now inserting ads *into* AI Overviews + AI Mode
  (sponsored links, Direct Offers, multiturn ads), says sponsored-vs-organic CTR in AI Mode is
  **"already similar,"** AI Mode queries are **incremental** (new, not cannibalized) and **3x longer**
  (more commercial intent). If AI Mode monetizes toward parity, revenue holds/grows.

**The two articles you sent — read carefully, they cut less bearish than they look:**
- **Ars Technica (Nov 20):** Google dropped the search *button*, added an AI-chat sidebar + history.
  This is Google **pushing users deeper into AI Mode** — bearish only if AI Mode monetizes worse;
  *bullish* if Google monetizes it at parity (it keeps the user inside Google either way).
- **Search Engine Land (Nov 20) / Pew / Seer:** the hard bear data — AI Overviews cut **external**
  click-through (Pew: 8% CTR with an AI summary vs 15% without; 1% click a cited source; Seer: −61%
  organic CTR for informational queries). **BUT — critical distinction — those studies measure clicks
  to *third-party websites* (the SEO/publisher complaint), NOT Google's ad revenue.** Google doesn't
  earn when you click a publisher; it earns when you click an **ad** or complete a **commercial
  action**. Fewer clicks *out* to publishers can mean Google is **keeping more of the journey on its
  own properties** (exactly the SEO critic's complaint: "all 12 touchpoints now happen on Google-owned
  properties"). **Publisher pain ≠ Google ad-revenue pain — it may be the opposite.**
- **So what would actually hurt Google?** (a) AI answers so complete that users don't engage with
  *any* commercial content (no ad clicks, no shopping) — a real risk on informational queries, less so
  on commercial ones; or (b) users taking **commercial** queries to a non-Google AI (ChatGPT). The
  share data says (b) isn't happening — **ChatGPT ≈ 7% of Google in the US and flat m/m; Google global
  search share 91%, +100bps y/y.**

**Honest bottom line on the bear:** it's real and it's binary, and it's specifically about whether AI
Mode's **ad load/CTR on commercial queries** holds up as the format shifts. The publisher-CTR collapse
(Pew/Seer) is the scariest-looking data but is the **weakest evidence against Google's revenue** — it's
mostly evidence Google is **winning the walled-garden battle** at publishers' expense. The de-rate is
partly pricing publisher pain as if it were Google pain. That gap is the edge; the genuine uncertainty
is informational-query monetization, which is why you size it as core, not all-in.

---

## 4. Google's AI monetization surfaces (the "Muse / Copilot" inventory you asked for)
Meta has basically **one** AI consumer product (Muse). Microsoft has **Copilot** (enterprise
productivity) + Azure. **Google has the broadest stack of all three — consumer AND enterprise AND
infra AND the ad surface:**

| Surface | What it is | Competes with | Monetization | Scale (latest) |
|---|---|---|---|---|
| **Gemini app** | consumer assistant | ChatGPT, Meta **Muse** | Google One AI subs ($/mo); ads later | **1B MAU**, fastest-growing product ever |
| **Gemini Enterprise** | enterprise agent platform | **MSFT Copilot**, ServiceNow | per-seat | 100M+ knowledge-worker seats; **90% of Fortune 100** |
| **Gemini for Workspace** | AI in Gmail/Docs/Sheets | **M365 Copilot** | per-seat uplift | embedded across Workspace |
| **Vertex AI / model APIs** | dev platform, Gemini APIs | Azure OpenAI, Bedrock | consumption | **32B tokens/min**, +4x YoY |
| **TPU systems** | merchant AI silicon | **NVIDIA**, Trainium | hardware + cloud | ~100 customers; Apple, Anthropic, Oracle, Crux |
| **Google Cloud (GCP)** | core cloud + AI infra | AWS, Azure | consumption | **+103% YoY, 36% op margin** |
| **Security (Wiz + Gemini)** | AI cyber (CodeMender) | CrowdStrike, MSFT | subscription | 90% of Fortune 100 use Google cyber |
| **Search AI (AI Overviews/Mode)** | ad-monetized answers | ChatGPT, Perplexity | **advertising** | 2B+ users; the profit pool in question |
| **Google One AI plans** | consumer subscription | ChatGPT Plus | subscription | fastest-growing sub product |
| **Agentic commerce (UCP)** | shopping agents | Amazon, OpenAI | ads + take-rate | hundreds of thousands of merchants |
| **Waymo** | physical AI / robotaxi | Tesla, Cruise | rides (early) | 15 cities, 300M+ autonomous miles, ~$126B+ val |
| **Isomorphic Labs** | AI drug discovery | — | pharma deals/milestones | raised $2B+ |

**The point for the thesis:** this is why GOOGL is the "captures ROI wherever it accrues" name. If AI
value goes to **chips** → TPU. To **models** → Gemini/Vertex. To **cloud** → GCP. To **enterprise
software** → Gemini Enterprise/Workspace (the Copilot slot). To **consumer** → Gemini app. To **ads**
→ Search AI. Meta monetizes AI essentially one way (better ad targeting + Muse); Microsoft two (Copilot
+ Azure). **Google monetizes it six ways and owns the silicon underneath.** That breadth is the
structural answer to "what cushions the Search risk" — Cloud is the obvious one, but Gemini Enterprise
(Copilot-analog), Workspace, Vertex, and the TPU merchant business are all independent, growing legs.

---

## 5. "Is this a good position vs the AI names that derated most?"
The most-derated AI names (from the handover, off their highs): **Nebius −73%, CoreWeave −71%, NVDA
−47%, GOOGL −35%, Meta −28%, MSFT −13%.** My honest ranking for *risk-adjusted* ownership right now:

- **Nebius / CoreWeave (−70%+):** biggest bounce if the AI trade rips, but these are **levered,
  single-customer-concentrated neoclouds** — the exact Leopold-trap profile (leverage turns a drawdown
  into forced liquidation). Highest raw upside, highest blow-up risk. **Torque, not a core position.**
- **NVDA (−47%):** cheaper on P/E, but carries the **OpenAI knife + circular financing ($99B stakes +
  $118B guarantees) + governance shock (Jensen resigned)**. A fat-tailed binary, as your own NVDA
  scorecard concluded. Good torque stub, not ballast.
- **GOOGL (−35%):** the de-rate is driven by a **fear the data contradicts** (Search share is
  *gaining*), sitting on a **diversified, self-funding, 30%-op-growth, net-cash** business with six AI
  monetization legs and the merchant-silicon hedge. **Biggest drawdown relative to how little the
  fundamentals actually broke.** That "big price drop, small fundamental damage" asymmetry is the best
  Sharpe in the group.
- **MSFT (−13%) / Meta (−28%):** MSFT barely derated (less opportunity, carries OpenAI exposure).
  Meta is single-threaded ads + heavy capex + negative FCF + Muse unproven.

**Verdict:** Among the derated AI names, **GOOGL is the best risk-adjusted position — the one to size
as a core long** — precisely because its de-rate is the most disconnected from its fundamentals. It is
**not** the biggest bounce if the whole complex V-recovers (the levered neoclouds would 2–3x); it's the
best *Sharpe*, the ballast. In a liquidity-driven risk-off (VIX ~36), that's exactly what you want to
be *adding*, but it's high-beta (β 1.23) — it can still see $230–240 on a broad VIX flush, which is why
you **scale in and keep powder**, not back up the truck in one click. The barbell stands: **GOOGL
ballast (self-funding ROI-capturer + alt-silicon) vs a small NVDA torque stub.** Your instinct — own
the cleanest, lowest-idiosyncratic-risk AI-ROI name — points at GOOGL, and the −35% to the 52-week low
is the market handing it to you on a Search fear the share data doesn't support.

_Watch the same four things from the verdict doc: AI-Mode monetization, global search share in the
alt-data, the Feb-3 2027 capex guide, and Cloud operating margin. Those are the thesis tells._

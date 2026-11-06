# The 9.2%-of-GDP break-even (Van Nieuwerburgh)

**What "9.2%" actually is:** not AI capex's *current* share of GDP (that's ~1–2%). It's the
compute **revenue the buildout must GENERATE by 2032 to break even** on the money being
spent — ~9.2% of projected 2032 GDP. It's a hurdle, not a footprint. This is the cleanest
quantified version of the revenue-vs-capex canyon, and it's now mainstream (WSJ, Brookings).

## Sources
- Stijn Van Nieuwerburgh, **"Financing the AI Buildout,"** Brookings Papers on Economic Activity (BPEA), conference draft Sep 24–25, 2026. [PDF](https://www.brookings.edu/wp-content/uploads/2026/09/4c_Van-Nieuwerburgh.pdf)
- Hanno Lustig, **"Nine Percent of GDP,"** The Two Cents, Sep 27, 2026. [link](https://thetwocents.substack.com/p/nine-percent-of-gdp)
- Greg Ip, **"Will America Spend 9% of Its GDP on AI?"** WSJ, Oct 2, 2026 (rounds to ~8.8%). (via Columbia Business School newsroom)
- Cummings & Bernstein, "AI Companies Are In a Race Against Time," Sep 25, 2026 — similar numbers for hyperscalers, different approach.

## The baseline math
- US AI-infrastructure investment: **$1.15T in 2025**, projected **$1.43T in 2026**.
- ~**3.6% of GDP per year** in AI infra, 2025–2032. That's ~**3x** the late-'90s telecom/fiber boom and ~**1.5x** the 19th-century railroad boom. One of the largest infra booms in US history.
- Break-even (baseline, 10% discount rate): **$3.725T of annual compute revenue by 2032** = **~9.2% of projected 2032 GDP** ($40.5T GDP path).
- Today's US compute revenue base ≈ **$0.3T**. To reach ~$3.7T by 2032, data-center revenue must grow **~45% a year for seven years**.
- In the paper's units: $3.725T ≈ **$5.5 per installed GPU-hour at full utilization** (~$6.9 at 80%), vs current on-demand of $6–10+. (Note: gross revenue, not value-added — the economic footprint is smaller.)

## The assumptions it rests on
- 183 GW of US data-center capacity completed 2025–32.
- $8.54T construction cost → **$9.61T capital base** (grossed up for return on capital tied up during construction).
- **10% unlevered required return.**
- **6-year IT-equipment life** (68% of cost) and 20-year non-IT life (32%).
- **50% operating-cash-flow margin.**

## The sensitivity that is the whole Burry argument
- The 6-year IT life is **deliberately generous**. The risk isn't that the chip stops running — it's that nobody pays $5.50/GPU-hr in 2032 for a 2026 chip.
- **Shrink IT life to 3 years → required revenue jumps from 9.2% to 14.7% of 2032 GDP.**
- **CoreWeave's lenders reportedly use ~3-year assumptions.** So the depreciation debate (Post 1/2) is literally the difference between a 9.2% hurdle and a ~15% hurdle — the latter is close to impossible.

## The telecom precedent (how this kind of thing ended before)
- 1998–2003 non-wireless telecom invested ~$440B; to earn 10% it needed **$190B** more revenue by 2003 (1.7% of GDP). It got **$95B** (0.8%). Implied return: **negative.** → WorldCom, Global Crossing, dozens of CLECs bankrupt.
- But the losses fell on **shareholders and high-yield bondholders**, not levered banks. No bank bailout.
- **This time may differ:** financing is project debt, private credit, and **~90%-levered SPVs off the hyperscalers' balance sheets** — opaque. Banks were indirectly exposed, now increasingly direct: every CoreWeave facility since mid-2025 (~4 deals, ~$17B) was syndicated to 10–13 banks incl. JPMorgan, MUFG, Morgan Stanley, Goldman, Citi, Wells.

## The two objections worth keeping (from the comments)
1. **Azeem Azhar:** the $1.15T / $1.43T US figure looks too high/broad. The seven hyperscalers + neoclouds reported ~$459B (2025) / ~$879B (2026) capex, of which maybe ≤64% is AI data centers. So the headline investment number may be inflated by a broad definition → break-even hurdle possibly overstated.
2. **Justin (margin objection — the load-bearing one):** the 50% operating margin assumes **monopoly/natural-monopoly economics** (like railroads/winner-take-all internet). But Chinese models are taking share at the model layer and **custom ASICs compete inference down to lowest cost**. If AI infra can't hold 50% margins, required revenue to break even is even higher.

## Why this matters for our thesis
- **It quantifies "who pays" and puts it on a clock.** $0.3T → $3.7T, 45%/yr for 7 years. That's the single best number for the top of a post.
- **It is the academic/mainstream version of the bear case** — so "the buildout has to generate enormous revenue fast or returns go negative" is becoming consensus framing (WSJ ran it). Not contrarian anymore. Contrarian is having a *view on whether 45%/yr happens.*
- **The 50%-margin assumption is where own-silicon loops in.** The thing that makes Google/Amazon winners (cheap in-house TPU/Trainium) is precisely the thing that **breaks the 50% merchant-compute margin** the break-even relies on. So "own-silicon wins" and "the aggregate buildout under-earns" are the *same* force seen from two sides: commoditization of merchant compute.
- **On "hide in non-AI":** if a build worth ~3.6% of GDP/yr under-earns, the air-pocket is macro (telecom 2000, but bigger and more bank-connected per the paper) — so non-AI isn't a clean safe room. But the shovels are the sharp end: at a 3-yr life the hurdle (14.7%) is near-impossible, which is what the depreciation bears are really underwriting.

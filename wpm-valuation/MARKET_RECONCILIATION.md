# Market-Implied Gold & Live Re-Rating (verified Nov 27, 2026)
_How our DCF reconciles to WPM's price at depressed spot, and whether the market is re-rating it. Built from the model's FCFF gold-only sensitivity (Revenue Assumptions D55:D59, now fixed) and the 2027E comps. All our-model figures at the base 6% real discount rate. Supersedes the earlier $4,200 / $122.60 version of this note._

## 0. Current anchors (all refreshed)
- WPM price: **$131.02** (Nov 27 close).
- Spot gold **~$3,650**, spot silver ~$43.
- Base deck: gold **$4,500** flat 2027 to 2030 (2026 booked ~$4,300). FCFE **$144.83** (+10.5%), FCFF $144.64. The two converge (debt-light streamer).
- Bear $3,400 to $90 (scenario) · Bull $5,200 to $187.
- FCFF gold-only table (2026 booked, margins flex via fixed cost per GEO): 3400 to $102 · 3800 to $117 · 4200 to $133 · 4600 to $149 · 5000 to $164.

## 1. DCF at spot vs the market price
- **Basis (important):** every figure holds **2026 at ~$4,300 booked** (realized, locked, same in all cases) and varies **2027 to 2030 held flat**. So "$3,650" means 2027 to 2030 flat at spot, not spot in 2026 too, and not reverting later.
- **At spot held flat (gold ~$3,650): FCFF DCF is ~$112** (interpolating the gold-only table). This is the spot-forever floor, NOT the base.
- WPM trades **$131.02**. The market prices WPM **~$19 above spot-intrinsic.**

## 2. What gold is the market implying? (invert the gold-only table at 6% real)
| WPM price | Implied flat gold (2027-30) | vs spot ~$3,650 |
|---|---|---|
| ~$112 | ~$3,650 (spot) | 0 |
| **$131.02** (now) | **~$4,150** | +$500 (+13.7%) |
| $145 (our base) | $4,500 | +$850 |

- **The market is already looking through spot by ~$500/oz. It prices the floor, not the tape.**
- Our **$4,500 base is ~$350 above the market's own implied ~$4,150**, and just below the low end of the street's $4,600 to $5,200. Conservative-to-fair, not aggressive.

**Two caveats to say before anyone else does:**
1. **Observational equivalence.** The implied-gold read assumes the market discounts at our 6% real rate. Equivalently, the market could be using spot ~$3,650 with a lower discount rate or higher multiple. From price alone the two cannot be separated. Lead with the robust, basis-free claim: **the market is not marking WPM to depressed spot.** The specific "~$4,150" is illustrative, not provable.
2. **Margins are not the thumb on the scale.** The gold-only table flexes margins correctly: WPM's cost is ~fixed per GEO (~$1,100 incl. depletion), so gross profit is linear in price and the table already embeds operating leverage. It does not add the bear scenario's extra conservatism on volumes and other drivers, which is why gold-only $3,400 to $102 is milder than the scenario bear $3,400 to $90. So "~$4,150" is on the base-cost structure, and a harsher-margin basis would need an even higher gold price to reach $131. **$4,150 is a conservative (low) read of market-implied gold, not an optimistic one.**

## 3. The multiple (2027E consensus, same basis for all four names)
From the comps table (LSEG 2027E):
| | EV/EBITDA | P/OCF |
|---|---|---|
| **WPM** | **18.6x** | 17.9x |
| FNV | 20.0x | 23.3x |
| RGLD | 12.4x | 13.5x |
| TFPM | 14.7x | 13.2x |
| **Peer median (ex-WPM)** | **14.7x** | 13.5x |

- WPM trades at a premium to the peer median, in line with FNV (the royalty-pure, highest-quality comp), warranted by scale and sector-leading margins.
- Forward 2027E P/OCF 17.9x at $131 (OCF/sh $7.32). Re-rating room toward WPM's own history (~20x+ current-year).

## 4. Terminal / exit multiple reconciliation (resolves a stale comment)
The model applies an **18x exit multiple** to 2030 EBITDA. Reconciled to the comps on ONE basis (2027E):
- 18x is **≈ WPM's own current 18.6x** (essentially flat, marginally below).
- **Below FNV's 20.0x** (closest quality comp).
- **Above the 14.7x peer median.**
So the exit multiple is "WPM keeps trading roughly where it trades now, below its best comp." Mildly conservative.
**Fix needed:** DCF-FCFF D9 / FCFE D9 comments still say "vs 13x peer median," and C40 says "FNV 17.1x / WPM 15.7x." Those are from an older comps cut and contradict the current table (median 14.7x, FNV 20.0x, WPM 18.6x; 15.7x is the peer AVERAGE, not WPM). Rewrite them to the three lines above.

## 5. The Q&A that will come
**"Gold is at $3,650, your bear says $3,400, WPM is at $131 but your bear says ~$100. Isn't that a contradiction?"**
No. A scenario is a conditional valuation, not a price target for today.
- At spot held flat our own model is ~$112, and the stock is $131. So the market is ~$19 ABOVE even the spot-flat value: it is pricing gold's forward path (~$4,150 flat), not today's $3,650.
- The bear ($3,400 to ~$90-100) is "gold de-rates AND stays there," a downside case the market currently assigns low odds, which is exactly why WPM is at $131 and not ~$112.
- The leverage (a ~7% gold move mapping to a ~20%+ equity move) is the whole reason to own the vehicle, and it cuts both ways. That is why washout entries matter.
- One line: "If the market agreed with our bear, WPM would trade near $112. It trades at $131 because the market's central case is the floor holding and volume ramping, which is our base."

## 6. Model housekeeping still open (apply in Excel)
- DCF-FCFE **F93** and DCF-FCFF **F103** labels still read "vs 109.91"; change both to **"vs 131.02."**
- Revenue **D54** data-table corner shows **#VALUE!**; set to `='DCF - FCFF'!$D$74` (shows the $144.6 base) or format hidden. Table body D55:D59 is correct.
- Stale comments (cell values were updated, comments were not): Revenue C42 "$4,200" to **$4,500**; Revenue C46 silver "base $53.9 / bull $69.1" to **~$59.6 / ~$72.9** (bear ~$38.7 unchanged); DCF-FCFF C78 "$133" to **$145**; DCF-FCFF C81 "$133" to **$145** (the $116 at 8.15% is correct); DCF-FCFE C65 "$133 base" to **$145**; the exit-multiple comments per section 4.
- Street range standardized to $4,600 to $5,200 (Comps B39 and the written report now agree; our $4,500 base sits just below the street low).

_Sources: model df52f0dd (FCFF gold-only table D55:D59; Comparables 2027E, LSEG); spot gold and silver Nov 27, 2026._

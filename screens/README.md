# Small-cap "next position" screen — Nov 9, 2026

yfinance screen run to hunt the Itron-shaped setup (~$2-5B, cheap, laggard, inflecting,
non-discretionary/AI-proof) across grid-edge/T&D/metering, mission-critical infra w/ recurring
revenue, water infra, and "mispriced-by-category" hardware.

- `smallcap_screen.py` — the script (yfinance; computes price-derived YTD/1Y, 52-wk position,
  mcap, fwd P/E, EV/EBITDA, P/S, rev growth, gross margin for a 34-name universe).
- `smallcap_screen_2026-11-09.csv` — the output (prices as of ~Nov 6 close).

**Note:** yfinance needs Yahoo Finance hosts allowed on the cloud env's network allowlist
(`query1/query2.finance.yahoo.com`, `fc.yahoo.com`, `guce.yahoo.com`) — added to the Default
env on 9 Nov 2026. Re-run locally or on that env.

## Survivors (cheap + crashed + not-a-trap, ~$2-5B band)
| Ticker | Mcap | YTD | Off 52w low | Fwd P/E | EV/EBITDA | Rev gro | Note |
|---|---|---|---|---|---|---|---|
| **OSIS** (OSI Systems) | $3.1B | −23% | +2.5% | 15.3x | 14.4x | +4.9% | **THE PICK** — mispriced-by-category, recurring + RF/defense annuity |
| BDC (Belden) | $3.8B | −17% | +1.6% | 9.8x | 15.3x | +38% | cheapest, but weaker moat + M&A-juiced topline |
| ENS (EnerSys) | $5.3B | −2% | +12% | 10.2x | 9.5x | +4.8% | cheap, data-center DC power, but not crashed enough |
| MWA (Mueller Water) | $3.7B | +1% | +13% | 14.4x | 9.7x | −1% | water non-discretionary, but flat/pricey on sales |

Excluded: already-run (ATKR +30%, VICR, SLAB +68%, DGII, MG, MLAB, BE +75%, WTS, GNRC) and traps
(FLNC −77% + losses, ERII rev −65%, PRIM rev −10%, AMRC policy headwind).

**Winner → OSIS.** Full deep-dive in `../osis/`.

---

# Next-position screen, 11 Nov 2026

Wider follow-up to the 9 Nov screen: 880-ticker universe, 519 in the $1-15B band, a filing-based
product/service scan, and first-pass diligence on five finalists (NSSC, TRMB, ARLO, DGII, VNT) with
ITRI and OSIS as benchmark rows. **Read `next-position-2026-11-11.md`.** Scripts are `nextpos_*.py`
and `secutil.py`; outputs are in `data/`. Run scripts from this directory. They need the Yahoo and
SEC hosts on the network allowlist and send a generic SEC User-Agent.

---

# Next-position screen v2, 12 Nov 2026

Four-mechanism search (misclassification, contracted floor, overhang, pre-recognition) over 1,692 US-listed
names at $1B+, including every company above $15B. Finalists: KBR, HESM, LDOS, AMTM, with ITRI, LNG and ADBE
as benchmark rows. **Read `next-position-2026-11-12.md`.** Scripts are `np2_*.py` (they reuse `secutil.py`
and `nextpos_valuation.py`); outputs are in `data/np2_*`. Run from this directory.

# OSIS — Testing "Backlog Accrual = Value Accrual" + the Reverse-DCF Math

*Original empirical work. Answers two questions: (1) is rising backlog actually rising value, or just
a number? (2) how was the "~4% implied growth" derived? As of 10 Nov 2026.*

## The claim
"Backlog accruing is value accruing, whether or not the market claps." Testable — here's the data.

## Test 1 — Does backlog convert to revenue? (backlog vs NEXT-year revenue)
| FYE backlog | → next-yr revenue | ratio |
|---|---|---|
| FY21 $1.08B | FY22 $1.18B | 0.91x |
| FY22 $1.20B | FY23 $1.28B | 0.94x |
| FY23 $1.80B | FY24 $1.54B | 1.17x |
| FY24 $1.70B | FY25 $1.71B | 0.99x |
| FY25 $1.80B | FY26 $1.79B | 1.01x |

**Backlog ran ~1.00x next-year revenue every year (range 0.91–1.17). $1 of backlog ≈ $1 of revenue ~12
months later — reliable, not phantom.**

## Test 2 — Do backlog, revenue, EPS grow together? (FY21→FY26 CAGR)
Backlog **+12%/yr** · Revenue **+9%/yr** · EPS **+14%/yr** → compounded in lockstep. Value tracked the
order book.

## Test 3 — The mechanism on the tape
Backlog surged **+50% (FY22→FY23)**, revenue surged **+20% one year later (FY23→FY24)**. The build led
the conversion by ~a year.

## Verdict + the one caveat
**TRUE for OSI, empirically: backlog→revenue is ~1:1 and reliable over 5 years.** CAVEAT: backlog→
*earnings* (value) also depends on the **margin** it converts at. Revenue conversion is proven; margin
is the second variable (why we underwrite flat margins and watch GM). Further tests: cancellation rate
(10-K: firm orders, minimal cancellations), book-to-bill lead, conversion-margin stability.

## The reverse-DCF ("~4% implied growth") — exact math
Single-stage Gordon perpetuity solved backwards: **EV = FCF/(WACC − g) → g = WACC − FCF/EV.**
EV $3,841M, FCF ~$190M, WACC 9% → g = 0.09 − 190/3841 = **4.1%.**
Sensitivity: WACC 8%/9%/10% → g 3.1%/4.1%/5.1%; FCF $180M/$209M → 4.3%/3.6%.
**Crude and input-sensitive — DON'T quote "exactly 4%."** The robust claim: **the price embeds ~3–5%
perpetual growth, below the consensus 6–9% near-term revenue growth → the market prices less growth
than the Street's own estimates.**

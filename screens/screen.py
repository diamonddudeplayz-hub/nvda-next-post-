import yfinance as yf
import pandas as pd
from datetime import datetime
import json, time

# Universe: grid-edge/T&D/metering, mission-critical infra w/ recurring rev,
# water infra, "mispriced-by-category" hardware. Weighted to ~$1-6B band.
UNIVERSE = {
    # --- Benchmark / owned ---
    "ITRI": "Itron (benchmark)",
    # --- Grid / T&D / metering / power infra ---
    "POWL": "Powell Industries (electrical switchgear)",
    "NVT":  "nVent Electric (enclosures/connections)",
    "AEIS": "Advanced Energy (power conversion)",
    "ATKR": "Atkore (electrical conduit)",
    "ENS":  "EnerSys (industrial batteries/DC power)",
    "AMSC": "American Superconductor (grid)",
    "PLPC": "Preformed Line Products (T&D hardware)",
    "HPS-A.TO": "Hammond Power Solutions (transformers)",
    "VICR": "Vicor (power modules)",
    "BDC":  "Belden (connectivity infra)",
    "ESE":  "ESCO Technologies (utility/test)",
    "THR":  "Thermon (process heating)",
    "GNRC": "Generac (backup power)",
    "ARRY": "Array Technologies (solar trackers)",
    "SHLS": "Shoals Technologies (electrical BOS)",
    "FLNC": "Fluence Energy (battery storage)",
    "AMRC": "Ameresco (energy efficiency/DER)",
    "MYRG": "MYR Group (electrical T&D construction)",
    "PRIM": "Primoris Services (energy/utility infra)",
    "BE":   "Bloom Energy (fuel cells)",
    # --- Water infra / metering ---
    "MWA":  "Mueller Water Products (water infra/metering)",
    "FELE": "Franklin Electric (water/fueling systems)",
    "BMI":  "Badger Meter (water metering)",
    "ERII": "Energy Recovery (pressure exchangers)",
    "ZWS":  "Zurn Elkay (water solutions)",
    "WTS":  "Watts Water Technologies",
    # --- Mission-critical infra, recurring/hidden-software ---
    "OSIS": "OSI Systems (security screening + service)",
    "NSSC": "Napco Security (recurring alarm)",
    "MLAB": "Mesa Labs (calibration/recurring)",
    "MG":   "Mistras Group (asset inspection)",
    "DGII": "Digi International (IoT connectivity + recurring)",
    "SITM": "SiTime (precision timing)",
    "SLAB": "Silicon Labs (IoT silicon)",
    "CSWI": "CSW Industrials (HVAC/industrial)",
    "FIX":  "Comfort Systems (mechanical/data-center MEP)",
}

def ytd_and_1y(hist, last):
    out = {}
    if hist is None or hist.empty:
        return {"ytd": None, "oneY": None, "px": None, "pct_of_52w": None}
    closes = hist["Close"].dropna()
    if closes.empty:
        return {"ytd": None, "oneY": None, "px": None, "pct_of_52w": None}
    px = float(closes.iloc[-1])
    # YTD: first close on/after Jan 1 this year
    yr = datetime.now().year
    ytd_series = closes[closes.index >= f"{yr}-01-01"]
    ytd = None
    if not ytd_series.empty:
        base = float(ytd_series.iloc[0])
        if base: ytd = (px/base - 1)*100
    # 1Y: first available close ~ 1y ago
    oneY = None
    if len(closes) > 2:
        base1y = float(closes.iloc[0])
        if base1y: oneY = (px/base1y - 1)*100
    hi = float(closes.max()); lo = float(closes.min())
    pct_of_52w = (px - lo)/(hi - lo)*100 if hi > lo else None
    return {"ytd": ytd, "oneY": oneY, "px": px, "pct_of_52w": pct_of_52w, "hi52": hi, "lo52": lo}

rows = []
for tkr, name in UNIVERSE.items():
    try:
        t = yf.Ticker(tkr)
        hist = t.history(period="1y", auto_adjust=True)
        perf = ytd_and_1y(hist, None)
        info = {}
        try:
            info = t.info or {}
        except Exception:
            info = {}
        mcap = info.get("marketCap")
        row = {
            "ticker": tkr,
            "name": name,
            "mcap_B": round(mcap/1e9, 2) if mcap else None,
            "px": round(perf["px"],2) if perf["px"] else None,
            "ytd_%": round(perf["ytd"],1) if perf["ytd"] is not None else None,
            "1y_%": round(perf["oneY"],1) if perf["oneY"] is not None else None,
            "pos_in_52w_%": round(perf["pct_of_52w"],0) if perf["pct_of_52w"] is not None else None,
            "fwdPE": round(info.get("forwardPE"),1) if info.get("forwardPE") else None,
            "trailPE": round(info.get("trailingPE"),1) if info.get("trailingPE") else None,
            " evEbitda": round(info.get("enterpriseToEbitda"),1) if info.get("enterpriseToEbitda") else None,
            "ps": round(info.get("priceToSalesTrailing12Months"),1) if info.get("priceToSalesTrailing12Months") else None,
            "revGro_%": round(info.get("revenueGrowth")*100,1) if info.get("revenueGrowth") is not None else None,
            "grossMg_%": round(info.get("grossMargins")*100,1) if info.get("grossMargins") is not None else None,
        }
        rows.append(row)
        print(f"{tkr:10s} {str(row['mcap_B']):>7} B  ytd {str(row['ytd_%']):>7}  1y {str(row['1y_%']):>7}  fwdPE {str(row['fwdPE']):>6}")
    except Exception as e:
        print(f"{tkr:10s} ERROR {e}")
    time.sleep(0.3)

df = pd.DataFrame(rows)
df.to_csv("screen_out.csv", index=False)
print("\nSAVED screen_out.csv  rows:", len(df))

"""Next-position screen v2 (12 Nov 2026): widen yesterday's universe to all four mechanisms.
Adds (a) every US-listed name above $15B (mechanisms B and C are allowed to be large caps),
(b) energy infrastructure, contracted power, streaming/royalty and asset-light recurring names at $1B+.
Yahoo fundamentals are a SCREEN ONLY. Output: data/np2_universe_raw_2026-11-12.csv
"""
import yfinance as yf, pandas as pd, numpy as np, time, sys
from yfinance import EquityQuery as Q
from concurrent.futures import ThreadPoolExecutor

NEW_IND = ["Oil & Gas Midstream","Utilities - Independent Power Producers","Utilities - Renewable","Gold","Silver",
 "Other Precious Metals & Mining","Oil & Gas Equipment & Services","Financial Data & Stock Exchanges","Consulting Services",
 "Insurance Brokers","Education & Training Services","Marine Shipping","Utilities - Regulated Gas","Uranium",
 "Oil & Gas E&P","Oil & Gas Refining & Marketing","Thermal Coal","Railroads","Trucking","Integrated Freight & Logistics",
 "Staffing & Employment Services","Advertising Agencies","Medical Distribution","Medical Care Facilities","Healthcare Plans",
 "Drug Manufacturers - Specialty & Generic","Packaging & Containers","Specialty Chemicals","Semiconductors",
 "Semiconductor Equipment & Materials","Internet Content & Information","Electronic Gaming & Multimedia","Telecom Services",
 "Credit Services","Capital Markets","Asset Management","Insurance - Specialty","Real Estate Services","REIT - Specialty"]
HAND = ["LNG","CQP","VG","NFE","KMI","WMB","OKE","ET","EPD","MPLX","TRGP","DTM","AM","KNTK","HESM","WES","PAA","PAGP","ENLC","EE","GLNG","FLNG","NEXT",
 "VST","CEG","NRG","TLN","CWEN","BEPC","BEP","ORA","AES","NEP","XIFR","PEG",
 "WPM","FNV","RGLD","OR","TFPM","SAND","MTA","EMX","GROY","SSRM","AEM","NEM","GOLD","B","KGC","AGI",
 "TPL","VNOM","BSM","KRP","DMLP","STR","LB","NRP","SBR","PBT","MSB","CCJ","UEC",
 "ADBE","CRM","NOW","WDAY","INTU","ADSK","DDOG","SNOW","TEAM","HUBS","VEEV","ORCL","MSFT","GOOGL","META","AMZN","AAPL","NVDA","AVGO","AMD","MU","QCOM","TXN","ADI","MCHP","ON","NXPI","INTC","MRVL",
 "ACN","IT","VRSK","SPGI","MCO","MSCI","FDS","ICE","CME","NDAQ","CBOE","FICO","EFX","TRU","BR","ADP","PAYX","FI","FIS","GPN","V","MA","PYPL","CPAY","WEX",
 "UNH","ELV","CI","HUM","CNC","MOH","CVS","MCK","COR","CAH","DHR","TMO","A","IQV","ISRG","SYK","BSX","MDT","ABT","BDX","EW","ZBH","BAX","GEHC","RMD","IDXX","ZTS","REGN","VRTX","AMGN","GILD","BMY","PFE","MRK","LLY","JNJ","ABBV","NVO","AZN","NVS","SNY","GSK",
 "UNP","CSX","NSC","CP","CNI","ODFL","UPS","FDX","WM","RSG","WCN","CTAS","ROL","VRSN","CPRT","CSGP","CDNS","SNPS","ANSS","PTC","ROP","TYL","CHKP","FTNT","PANW","CRWD","ZS","OKTA","NET","GEN","AKAM","FFIV","CSCO","ANET","MSI","HPE","DELL","NTAP","IBM",
 "LIN","APD","SHW","ECL","PPG","IFF","DD","DOW","LYB","CTVA","NUE","STLD","FCX","SCCO","VMC","MLM","CRH",
 "NKE","LULU","SBUX","MCD","CMG","YUM","DPZ","TGT","DG","DLTR","COST","WMT","HD","LOW","TJX","ROST","ORLY","AZO","ULTA","EL","PG","KO","PEP","MDLZ","KHC","GIS","HSY","CL","KMB","CLX","CHD","STZ","BF-B","DEO","PM","MO","BTI",
 "DIS","NFLX","CMCSA","CHTR","T","VZ","TMUS","WBD","EA","TTWO","RBLX","SPOT","UBER","ABNB","BKNG","EXPE","MAR","HLT","RCL","CCL","LVS","WYNN",
 "BRK-B","JPM","BAC","WFC","C","GS","MS","SCHW","BLK","BX","KKR","APO","ARES","AXP","COF","PGR","ALL","TRV","CB","AIG","MET","PRU","AFL","MMC","AON","AJG","WTW","BRO","ERIE",
 "AMT","CCI","SBAC","EQIX","DLR","PLD","PSA","O","SPG","WELL","LAMR","OUT","IRM",
 "XOM","CVX","COP","EOG","OXY","SLB","HAL","BKR","FTI","PSX","VLO","MPC","CTRA","EQT","AR","RRC","EXE",
 "CACI","SAIC","BAH","LDOS","PSN","KBR","AMTM","VVX","CW","BWXT","HII","GD","LHX","NOC","LMT","RTX","TDG","HEI","GE","HON","MMM","EMR","ROK","ETN","PH","ITW","CMI","DE","CAT","PCAR","OTIS","CARR","JCI","TT","LII","VLTO","FTV","RAL","AME","KEYS","TER","GRMN","TRMB","ZBRA","TDY","MTD","WAT","VNT","ITRI","OSIS"]

def screen(queries):
    seen = {}
    for label, q in queries:
        off = 0
        while True:
            try: r = yf.screen(q, size=250, offset=off)
            except Exception as e: print("screen err", label, e); break
            qs = r.get('quotes', [])
            for x in qs:
                if x.get('exchange') in ('NMS','NYQ','NGM','NCM','ASE'): seen.setdefault(x['symbol'], label)
            off += 250
            if off >= r.get('total', 0) or not qs: break
        print(label, len(seen), flush=True); time.sleep(0.3)
    return seen

def metrics(tkr):
    t = yf.Ticker(tkr)
    try: info = t.info or {}
    except Exception: info = {}
    g = info.get
    row = {"ticker": tkr, "name": g("shortName"), "industry": g("industry"), "sector": g("sector"), "mcap_B": (g("marketCap") or np.nan)/1e9}
    if not ((row["mcap_B"] or 0) >= 0.8): return row
    row.update({
      "px": g("currentPrice"), "fwdPE": g("forwardPE"), "trailPE": g("trailingPE"), "evEbitda": g("enterpriseToEbitda"), "ev": g("enterpriseValue"),
      "revGro": g("revenueGrowth"), "grossMg": g("grossMargins"), "opMg": g("operatingMargins"),
      "ebitda": g("ebitda"), "debt": g("totalDebt"), "cash": g("totalCash"), "fcf": g("freeCashflow"), "ocf": g("operatingCashflow"),
      "nAnalysts": g("numberOfAnalystOpinions"), "shortPctFloat": g("shortPercentOfFloat"), "instPct": g("heldPercentInstitutions"),
      "epsFwd": g("forwardEps"), "epsTtm": g("trailingEps"), "country": g("country"), "divYield": g("dividendYield"),
      "sharesOut": g("sharesOutstanding"), "tgtMean": g("targetMeanPrice")})
    try:
        h = t.history(period="10y", interval="1wk", auto_adjust=False)["Close"].dropna()
        px = float(h.iloc[-1]); row["px"] = row["px"] or px
        row["wk200"] = float(h.iloc[-200:].mean()) if len(h) >= 200 else np.nan
        row["vs200wk"] = px/row["wk200"]-1 if len(h) >= 200 else np.nan
        row["dd52w"] = px/float(h.iloc[-52:].max())-1
        row["dd5y"] = px/float(h.iloc[-260:].max())-1
        row["ret1y"] = px/float(h.iloc[-53])-1 if len(h) > 53 else np.nan
        row["ret3m"] = px/float(h.iloc[-14])-1 if len(h) > 14 else np.nan
    except Exception: pass
    try:
        eh = t.earnings_history
        if eh is not None and len(eh):
            s = eh["surprisePercent"].astype(float).tolist()[-4:]
            row["beats4"] = sum(1 for x in s if x > 0); row["surprises"] = "|".join(f"{x*100:.1f}" for x in s)
    except Exception: pass
    try:
        ee = t.earnings_estimate
        row["epsGro0y"] = float(ee.loc["0y","growth"]); row["epsGro1y"] = float(ee.loc["+1y","growth"])
        re_ = t.revenue_estimate
        row["revGro0y"] = float(re_.loc["0y","growth"]); row["revGro1y"] = float(re_.loc["+1y","growth"])
    except Exception: pass
    return row

if __name__ == "__main__":
    old = pd.read_csv("data/nextpos_universe_raw_2026-11-11.csv")
    qs = [("large>15B", Q('and',[Q('eq',['region','us']),Q('gte',['intradaymarketcap',15e9])]))]
    for ind in NEW_IND:
        try: qs.append((ind, Q('and',[Q('eq',['region','us']),Q('eq',['industry',ind]),Q('gte',['intradaymarketcap',1e9]),Q('lte',['intradaymarketcap',15e9])])))
        except ValueError as e: print("skip", ind, e)
    uni = screen(qs)
    for h in HAND: uni.setdefault(h, "hand")
    # refresh everything, including yesterday's in-range names, so all prices are the same close
    for tk in old.loc[old.mcap_B.between(0.8, 18), 'ticker']: uni.setdefault(tk, "v1")
    print("to fetch:", len(uni), flush=True)
    def safe(tk):
        for _ in range(2):
            try:
                r = metrics(tk); r["src"] = uni[tk]; return r
            except Exception as e: time.sleep(2)
        return {"ticker": tk, "src": uni[tk]}
    with ThreadPoolExecutor(5) as ex: rows = list(ex.map(safe, sorted(uni)))
    df = pd.DataFrame(rows); df.to_csv("data/np2_universe_raw_2026-11-12.csv", index=False)
    print("saved", len(df), df.px.notna().sum())

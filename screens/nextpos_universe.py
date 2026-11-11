"""Stage 1+2 of the 'next position' screen (11 Nov 2026).
Universe from the Yahoo screener (US-listed, $0.8-18B, hardware-with-service industries),
then per-ticker Yahoo metrics. Yahoo fundamentals are a SCREEN ONLY; anything load-bearing
is re-derived from filings in nextpos_filings.py.
Usage: python3 nextpos_universe.py  -> data/nextpos_universe_2026-11-11.csv
"""
import yfinance as yf, pandas as pd, numpy as np, time, sys, json
from yfinance import EquityQuery as Q

INDUSTRIES = ["Scientific & Technical Instruments","Electronic Components","Security & Protection Services",
 "Specialty Industrial Machinery","Medical Devices","Medical Instruments & Supplies","Electrical Equipment & Parts",
 "Building Products & Equipment","Communication Equipment","Diagnostics & Research","Computer Hardware",
 "Aerospace & Defense","Pollution & Treatment Controls","Tools & Accessories","Specialty Business Services",
 "Health Information Services","Business Equipment & Supplies","Engineering & Construction","Industrial Distribution",
 "Information Technology Services","Rental & Leasing Services","Waste Management","Consumer Electronics","Conglomerates",
 "Farm & Heavy Construction Machinery","Auto Parts","Metal Fabrication","Software - Infrastructure","Software - Application"]
# software industries are included only to catch hardware-plus-software names Yahoo misfiles; filtered below by gross margin
EXTRA = ["ITRI","OSIS","NSSC","DGII","MLAB","MG","PAR","VNT","FTV","RAL","ALRM","PI","ZBRA","TRMB","BMI","MWA","ESE","GTLS","CECO","FELE","WTS","ZWS","OTIS","ALLE","AZZ","ARLO","IRDM","GRMN","NVT","POWL","ENS","BDC","THR","AEIS","VSAT","KTOS","MRCY","CGNX","NOVT","HAE","MMSI","ICUI","LMAT","GKOS","PEN","NVST","XRAY","OMCL","TNDM","PODD","MASI","GMED","ITGR","CNMD","TFX","QDEL","NEOG","BIO","BRKR","AZTA","RVTY","WAT","MTD","TDY","LDOS","CACI","EVTC","PAY","CMPO","NCR","VYX","NATL","DBD","CXT","CR","VRRM","ACVA","DXPE","LNN","ALG","HLIO","GTES","EPAC","KAI","SXI","MOG-A","WWD","CW","HEI","AIR","DCO","TGI","VVX","PSN","FLR","MIR","BWXT","CWST","SRCL","ROL","ABM","UNF","CTAS","ARMK","PRCT","INSP","IRTC","TMDX","SOLV","EMBC","STAA","AORT","UFPT","ATEC","LIVN","NARI","AXNX","SILK","OFIX","ESTA","RXST","BLFS","VCYT","NTRA","TXG","ADUS","ENOV","HOLX","COO","ALGN","RMD","DXCM","STE","BAX","ATR","WST","TECH","RGEN","AVTR","ILMN","PKG","KEYS","FTDR","ALGM","VIAV","LITE","CIEN","EXTR","CALX","HLIT","ADTN","INFN","NTCT","CRUS","SYNA","LFUS","ROG","OLED","PLXS","SANM","BHE","TTMI","FN","CLS","KN","VSH","AVT","ARW","SNX","NSIT","PLUS","CDW","EPAM","ASGN","GTM","SSTK","CCCS","PRGS","AGYS","QTWO","ALKT","NCNO","SPSC","PCTY","MANH","DSGX","TYL","GWRE","APPF","BSY","PTC","NTNX","OSPN","MITK","EVBG","PWSC","POWI","AMBA","LSCC","FORM","ONTO","CAMT","NVMI","ACLS","UCTT","ICHR","COHU","KLIC","PLAB","AOSL","DIOD","SMTC","MTSI","SITM","SLAB","RMBS","MXL","VECO","ACMR","ATKR","HUBB","AYI","GNRC","AOS","LII","CSL","TREX","AWI","SSD","UFPI","ROCK","GFF","NX","APOG","PGTI","JELD","DOOR","AMWD","FBIN","MAS","OC","BLDR","IBP","TILE","MHK","WMS","AAON","CSWI","FIX","EME","MTZ","PWR","DY","PRIM","MYRG","STRL","ROAD","GVA","TPC","IESC","AGX","VMI","ARCB","MSA","BRC","NPO","ITT","FLS","RRX","GGG","IEX","NDSN","DCI","CFX","WTS","MIDD","JBTM","TTC","LECO","KMT","TKR","RBC","ATMU","MLI","WOR","ESAB","CHX","XYL","PNR","BMI","ROP","AME","FTV","VLTO","VNT","ST","TEL","APH","GLW","COHR","IPGP","LASR","MKSI","ENTG","AXON","CRCT","SONO","GPRO","KOSS","UEIC","VZIO","LOGI","HEAR","CRSR","NTGR","DGII","CAMP","PDFS","SMRT","LYTS","ALNT","PLPC","VICR","AMSC","HPS-A.TO","BWMN","WLDN","TTEK","NVEE","KBR","J","ACM","STN","FCN","EXPO","ICFI","CBZ","HURN","MMS","TNET","CSGS","EEFT","WEX","FOUR","PAYO","RELY","FLYW","SHIFT4","GPN","JKHY","ACIW","BR","SSNC","FDS","MORN","VRSK","EFX","TRU","FICO","DNB","NRDS","MKTX","TW","VIRT","LPLA","SF","PIPR","EVR","HLI","MC","PJT","LAZ","IBKR","RJF","SCHW","AMP","ADT","BCO","GEO","CXW","ALLE","REZI","CARR","JCI","TT","LII","WSO","FERG","POOL","SITE","BECN","GMS","IBP","TTEK","MODG","ELF","PRO","NOVT","FARO","MTRN","VPG","LUNA","HURC","TRNS","CYBE","INVE","NNBR","ITI","IDCC","CEVA","PCTEL","AIRG","INSG","CMBM","CASA","DZSI","AVNW","GILT","KVHI","ORBC","ATEX","TDS","USM","SHEN","CNSL","LUMN","CCOI","FYBR","WOW","ATUS","CABO","CHTR","LBRDA","SIRI","IHRT","FWRD","XPEL","FOXF","THRM","GNTX","LEA","ADNT","ALV","BWA","DAN","MOD","SMP","DORM","LKQ","GPC","MNRO","VVV","CWH","LCII","PATK","WGO","THO","PII","BC","MBUU","HOG","HZO","ONEW","MCFT","MPX","LEVI","FTAI","WSC","MGRC","HRI","URI","HEES","AL","AER","GATX","TRN","GBX","WAB","RAIL","ALSN","CMI","PCAR","OSK","TEX","MTW","AGCO","DE","CNH","TITN","LNN","ALG","ASTE","GENC","CMCO","HY","MEC","NPK","PKOH","SXC","TWI","WNC","BLBD","SHYF","REVG","FSS","PLOW","MLR","DOV","GRC","HI","CIR","AIN","ESCO","OFLX","OTTR","ALE","AVA","BKH","IDA","NWE","OGE","PNM","POR","EE","HE","MGEE","NWN","SR","SWX","NJR","OGS","CPK","UTL","SJW","AWR","CWT","MSEX","YORW","ARTNA","CWCO","GWRS","AWK","WTRG","FLOW","VRT","ETN","EMR","ROK","HON","GE","MMM","ITW","PH","NVT","GEV","BE","PLUG","FCEL","BLDP","SEDG","ENPH","RUN","NOVA","FSLR","ARRY","SHLS","NXT","FLNC","STEM","EOSE","FREY","ENVX","QS","CHPT","BLNK","EVGO","WKHS","NKLA","HYLN","XOS","PTRA","LEV","GP","FTEK","ADES","CECO","ERII","PCT","LNZA","ORGN","GEVO","AMTX","REX","GPRE","CLNE","OPAL","MNTK","AMRC","TPIC","AZZ","NWPX","IIIN","HAYN","USAP","CRS","ATI","HWM","PCC","TDG","HXL","SPR","DCO","ASTR","RKLB","SPCE","LUNR","RDW","MNTS","BKSY","PL","SPIR","ASTS","GSAT","IRDM","VSAT","SATS","TSAT","CMTL","GOGO","KTOS","AVAV","MRCY","LHX","NOC","GD","LMT","RTX","BA","TXT","HII","SAIC","BAH","CACI","LDOS","PSN","VVX","KBR","MANT","DLHC","NSSC","CIX","EVLV","SPCB","ARLO","ALRM","VRNT","NICE","MSI","ZBRA","CGNX","NATI","FLIR","TDY","TRMB","GRMN","HXGBY","TER","NOVT","IPGP","COHR","ONTO","PAR","OLO","TOST","AGYS","NCR","VYX","NATL","DBD","CXT","CPI","EVRI","PLAY","IGT","LNW","AGS","ACEL","INSE","PRCH","OPRA","GDRX","HIMS","TDOC","AMWL","DOCS","PGNY","ACCD","HQY","PHR","HCAT","NRC","OMCL","TBRG","CPSI","EVH","PINC","RCM","CERT","SLP","SDGR","MEDP","ICLR","IQV","CRL","LH","DGX","SYNH","PRAH","OPCH","PDCO","HSIC","OMI","MCK","CAH","COR"]
EXTRA = sorted(set(EXTRA))

def screen_universe():
    seen = {}
    for ind in INDUSTRIES:
        try:
            q = Q('and',[Q('eq',['region','us']),Q('eq',['industry',ind]),
                     Q('gte',['intradaymarketcap',0.8e9]),Q('lte',['intradaymarketcap',18e9])])
        except ValueError as e: print("skip", ind, e); continue
        off = 0
        while True:
            try: r = yf.screen(q, size=250, offset=off)
            except Exception as e: print("screen err", ind, e); break
            qs = r.get('quotes', [])
            for x in qs:
                if x.get('exchange') in ('NMS','NYQ','NGM','NCM','ASE'):
                    seen[x['symbol']] = ind
            off += 250
            if off >= r.get('total', 0) or not qs: break
        print(ind, len(seen)); time.sleep(0.3)
    return seen

def metrics(tkr):
    t = yf.Ticker(tkr)
    try: info = t.info or {}
    except Exception: info = {}
    row = {"ticker": tkr, "name": info.get("shortName"), "industry": info.get("industry"),
           "mcap_B": (info.get("marketCap") or np.nan)/1e9}
    if not (0.8 <= (row["mcap_B"] or 0) <= 18): return row
    g = info.get
    row.update({
      "px": g("currentPrice"), "fwdPE": g("forwardPE"), "trailPE": g("trailingPE"), "evEbitda": g("enterpriseToEbitda"),
      "revGro": g("revenueGrowth"), "grossMg": g("grossMargins"), "opMg": g("operatingMargins"),
      "ebitda": g("ebitda"), "debt": g("totalDebt"), "cash": g("totalCash"), "fcf": g("freeCashflow"),
      "nAnalysts": g("numberOfAnalystOpinions"), "shortPctFloat": g("shortPercentOfFloat"),
      "epsFwd": g("forwardEps"), "epsTtm": g("trailingEps"), "country": g("country")})
    try:
        h = t.history(period="10y", interval="1wk", auto_adjust=False)["Close"].dropna()
        px = float(h.iloc[-1]); row["px"] = row["px"] or px
        row["wk200"] = float(h.iloc[-200:].mean()) if len(h) >= 200 else np.nan
        row["vs200wk"] = px/row["wk200"]-1 if len(h) >= 200 else np.nan
        row["dd52w"] = px/float(h.iloc[-52:].max())-1
        row["dd5y"] = px/float(h.iloc[-260:].max())-1
        row["ret1y"] = px/float(h.iloc[-53])-1 if len(h) > 53 else np.nan
    except Exception as e: pass
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
    uni = screen_universe()
    for e in EXTRA: uni.setdefault(e, "extra")
    print("universe candidates:", len(uni))
    rows = []
    for i, tkr in enumerate(sorted(uni)):
        try: r = metrics(tkr); r["src"] = uni[tkr]; rows.append(r)
        except Exception as e: print(tkr, "ERR", e)
        if i % 25 == 0: print(i, tkr, flush=True)
        time.sleep(0.15)
    df = pd.DataFrame(rows)
    df.to_csv("data/nextpos_universe_raw_2026-11-11.csv", index=False)
    print("saved", len(df))

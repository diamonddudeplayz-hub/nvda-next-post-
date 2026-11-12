"""Yahoo consensus detail for the shortlist (SCREEN/secondary source): price, coverage, beat history, FY estimates, next date."""
import yfinance as yf, sys, json, pandas as pd
out = {}
for tk in sys.argv[1:]:
    t = yf.Ticker(tk); i = t.info; g = i.get
    d = dict(px=g('currentPrice'), mcapB=round((g('marketCap') or 0)/1e9, 2), evB=round((g('enterpriseValue') or 0)/1e9, 2), nAn=g('numberOfAnalystOpinions'),
             tgt=g('targetMeanPrice'), inst=g('heldPercentInstitutions'), insider=g('heldPercentInsiders'), shortFloat=g('shortPercentOfFloat'), sharesM=round((g('sharesOutstanding') or 0)/1e6, 1),
             hi52=g('fiftyTwoWeekHigh'), lo52=g('fiftyTwoWeekLow'), div=g('dividendRate'))
    try:
        eh = t.earnings_history; d['beats'] = [(str(q.date()), round(r.epsActual, 2), round(r.epsEstimate, 2), round(r.surprisePercent*100, 1)) for q, r in eh.iterrows()]
    except Exception as e: d['beats'] = str(e)
    try:
        ee = t.earnings_estimate; d['eps'] = {k: (round(ee.loc[k, 'avg'], 2), int(ee.loc[k, 'numberOfAnalysts']), round(ee.loc[k, 'yearAgoEps'], 2)) for k in ('0y', '+1y')}
        re_ = t.revenue_estimate; d['rev'] = {k: (round(re_.loc[k, 'avg']/1e6), round(re_.loc[k, 'growth']*100, 1)) for k in ('0y', '+1y')}
    except Exception as e: d['eps'] = str(e)
    try: d['next'] = [str(x) for x in t.calendar.get('Earnings Date', [])]
    except Exception: pass
    out[tk] = d; print(tk, json.dumps(d))
json.dump(out, open('data/np2_detail_2026-11-12.json', 'w'), indent=1)

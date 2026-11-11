"""SEC helpers: filing index, income-statement R-pages (product vs service split), companyfacts.
Generic User-Agent only (no personal contact)."""
import requests, json, re, time, os, html
UA = {"User-Agent": "equity-research-screen/1.0 (research-bot@example.com)", "Accept-Encoding": "gzip, deflate"}
CACHE = os.environ.get("SEC_CACHE", "/tmp/sec_cache"); os.makedirs(CACHE, exist_ok=True)

def get(url, binary=False):
    fn = os.path.join(CACHE, re.sub(r'[^A-Za-z0-9._-]', '_', url)[-180:])
    if os.path.exists(fn):
        return open(fn, 'rb').read() if binary else open(fn, encoding='utf-8', errors='replace').read()
    for i in range(4):
        r = requests.get(url, headers=UA, timeout=40)
        if r.status_code == 200:
            open(fn, 'wb').write(r.content); time.sleep(0.12)
            return r.content if binary else r.content.decode('utf-8', errors='replace')
        if r.status_code == 404: return None
        time.sleep(1.5 * (i + 1))
    return None

_TK = None
def cik(ticker):
    global _TK
    if _TK is None:
        _TK = {v['ticker']: v['cik_str'] for v in json.loads(get("https://www.sec.gov/files/company_tickers.json")).values()}
    return _TK.get(ticker.upper())

def filings(ticker, forms=("10-Q", "10-K"), n=14):
    c = cik(ticker); sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{c:010d}.json"))
    pages = [sub['filings']['recent']]
    out = []
    def scan(r):
        for f, acc, d, rep, doc, items in zip(r['form'], r['accessionNumber'], r['filingDate'], r['reportDate'], r['primaryDocument'], r.get('items', [''] * len(r['form']))):
            if f in forms and len(out) < n:
                out.append(dict(form=f, acc=acc, filed=d, period=rep, doc=doc, items=items,
                                base=f"https://www.sec.gov/Archives/edgar/data/{c}/{acc.replace('-', '')}/"))
    scan(pages[0])
    for extra in sub['filings'].get('files', []):
        if len(out) >= n: break
        scan(json.loads(get("https://data.sec.gov/submissions/" + extra['name'])))
    return out

def _cells(row):
    return [html.unescape(re.sub(r'<[^>]+>', '', c)).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.S)]

def _num(s):
    s = s.replace('$', '').replace(',', '').strip()
    neg = s.startswith('(')
    s = s.strip('()')
    try: v = float(s)
    except ValueError: return None
    return -v if neg else v

def income_statement(f):
    """Return (title, header_cells, rows[(label, [values])]) for the income statement R-page of filing f.
    Values are scaled to $ thousands (per-share rows are scaled too; ignore them)."""
    for i in range(2, 9):
        h = get(f['base'] + f"R{i}.htm")
        if not h: continue
        m = re.search(r'<th[^>]*class="tl"[^>]*>(.*?)</th>', h, re.S)
        title = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else ''
        tl = title.lower()
        if 'parenthetical' in tl or 'balance' in tl or 'financial position' in tl or 'cash flow' in tl or 'equity' in tl or 'audit information' in tl or 'cover' in tl: continue
        rows = []; hdr = []
        for row in re.findall(r'<tr[^>]*>(.*?)</tr>', h, re.S):
            c = _cells(row)
            if not c: continue
            if '<th' in row: hdr += c; continue
            rows.append((c[0], [_num(x) for x in c[1:]]))
        labs = ' ; '.join(r[0].lower() for r in rows[:40])
        if not (re.search(r'revenue|sales', labs) and re.search(r'cost|expenses', labs)): continue
        scale = 1000.0 if 'in millions' in tl else (0.001 if 'in thousands' not in tl else 1.0)
        rows = [(l, [None if v is None else v * scale for v in vals]) for l, vals in rows]
        return title, hdr, rows
    return None, None, None

def facts(ticker):
    return json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik(ticker):010d}.json"))

def text(htmltxt):
    t = re.sub(r'(?is)<(script|style).*?</\1>', ' ', htmltxt)
    t = re.sub(r'(?i)</(p|div|tr|h\d|li)>|<br[^>]*>', '\n', t)
    t = re.sub(r'(?i)</t[dh]>', ' | ', t)
    t = html.unescape(re.sub(r'<[^>]+>', '', t)).replace('\xa0', ' ')
    t = re.sub(r'[ \t]+', ' ', t); t = re.sub(r'( \| )+', ' | ', t)
    return re.sub(r'\n\s*\n+', '\n', t)

def releases(ticker, n=60):
    """8-K filings with item 2.02 (earnings releases), newest first."""
    return [f for f in filings(ticker, forms=("8-K",), n=400) if '2.02' in (f['items'] or '')][:n]

def exhibit99(f):
    idx = get(f['base'] + 'index.json')
    if not idx: return None
    items = json.loads(idx)['directory']['item']
    names = [i['name'] for i in items if re.search(r'(?i)ex.?99|press|earn|release', i['name']) and i['name'].lower().endswith(('.htm', '.html'))]
    if not names:
        names = [i['name'] for i in items if i['name'].lower().endswith(('.htm', '.html')) and i['name'] != f['doc'] and 'index' not in i['name']]
    if not names: return None
    # prefer the largest candidate
    sizes = {i['name']: int(i.get('size') or 0) for i in items}
    names.sort(key=lambda x: -sizes.get(x, 0))
    h = get(f['base'] + names[0])
    return text(h) if h else None

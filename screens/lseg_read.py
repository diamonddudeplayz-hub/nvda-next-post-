"""Read LSEG .xlsx exports without openpyxl (their stylesheet breaks it): unzip, parse sharedStrings and each sheet.
Usage: python3 lseg_read.py FILE.xlsx -> list of (sheet_name, rows[list of cell strings])"""
import zipfile, re, sys, html
def col(c):
    n = 0
    for ch in re.match(r'[A-Z]+', c).group(0): n = n*26 + ord(ch) - 64
    return n - 1
def read(path):
    z = zipfile.ZipFile(path); names = z.namelist()
    _rd = z.read
    class _Z:  # strip the x: namespace prefix some LSEG exports use
        def read(self, n): return re.sub(rb'<(/?)x:', rb'<\1', _rd(n))
    z = _Z()
    ss = []
    if 'xl/sharedStrings.xml' in names:
        x = z.read('xl/sharedStrings.xml').decode('utf8', 'replace')
        for si in re.findall(r'<si>(.*?)</si>', x, re.S): ss.append(html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>', si, re.S))))
    wb = z.read('xl/workbook.xml').decode('utf8', 'replace'); snames = re.findall(r'''<sheet [^>]*name=["']([^"']+)["']''', wb)
    out = []
    sheets = sorted([n for n in names if re.match(r'xl/worksheets/sheet\d*\.xml', n)], key=lambda s: int((re.search(r'(\d+)', s) or re.search(r'()', s)).group(1) or 0))
    for i, sn in enumerate(sheets):
        x = z.read(sn).decode('utf8', 'replace'); rows = []
        for r in re.findall(r'<row[^>]*>(.*?)</row>', x, re.S):
            cells = {}
            for attrs0, body in re.findall(r'<c ([^>]*?)(?:/>|>(.*?)</c>)', r, re.S):
                m = re.search(r'''\br=["']([A-Z]+\d+)["']''', attrs0)
                if not m: continue
                ref, attrs = m.group(1), attrs0.replace("'", '"')
                v = re.search(r'<v>(.*?)</v>', body or '', re.S); t = re.search(r't="(\w+)"', attrs)
                if v is None:
                    it = re.findall(r'<t[^>]*>(.*?)</t>', body or '', re.S); val = html.unescape(''.join(it))
                else:
                    val = v.group(1); val = ss[int(val)] if t and t.group(1) == 's' else html.unescape(val)
                cells[col(ref)] = val
            if cells: rows.append([cells.get(k, '') for k in range(max(cells)+1)])
        out.append((snames[i] if i < len(snames) else sn, rows))
    return out
if __name__ == "__main__":
    for name, rows in read(sys.argv[1]):
        print('##', name, len(rows))
        for r in rows[:int(sys.argv[2]) if len(sys.argv) > 2 else 12]: print(' | '.join(c[:28] for c in r)[:240])

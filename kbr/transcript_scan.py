"""Pull the sentences that carry the thesis-relevant facts out of each KBR transcript (LSEG StreetEvents text).
python3 kbr/transcript_scan.py THEME_REGEX [max_per_file] [files...]"""
import sys, re, glob
pat = re.compile(sys.argv[1], re.I); mx = int(sys.argv[2]) if len(sys.argv) > 2 else 6
files = sys.argv[3:] or sorted(glob.glob('20*KBR.N*Transcript.txt'), key=lambda f: (f[:4], ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'].index(f[5:8]), f[9:11]))
for f in files:
    t = open(f, encoding='utf8', errors='replace').read()
    title = re.search(r'\n\n(.+?)\n(\w+ \d+, \d{4})', t)
    spk = None; hits = []
    for line in t.split('\n'):
        m = re.match(r'^([A-Z][\w\.\' -]+), (.+?) - (.+?) \[\d+\]', line)
        if m: spk = m.group(1); continue
        for s in re.split(r'(?<=[.?!]) +', line):
            if pat.search(s) and len(s) > 50: hits.append((spk, s.strip()))
    print(f"\n### {f[:11]} {title.group(1)[:50] if title else ''} ({len(hits)} hits)")
    for spk, s in hits[:mx]: print(f"  [{(spk or '?').split()[-1]}] {s[:430]}")

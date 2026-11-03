#!/usr/bin/env python3
"""
Regenerates every SVG under assets/generated/ from live GitHub data.

Outputs (each in a dark and a light variant, picked by the README with
<picture> + prefers-color-scheme):
  stats-*.svg            headline numbers
  langs-*.svg            most-used languages by bytes
  activity-*.svg         the repos I pushed to most recently
  cards/<repo>-*.svg     featured project cards (stars, language, last push)

Which projects are featured, and their one-line results, live in
scripts/featured.json, so editing the profile never means editing code.

Run locally:  GITHUB_TOKEN=... python3 scripts/generate_stats.py
Run in CI:    .github/workflows/refresh-profile.yml (daily).
Standard library only; no third-party badge service is involved.
"""
import datetime as dt
import json
import os
import textwrap
import urllib.parse
import urllib.request
from xml.sax.saxutils import escape

USERNAME = "claudialbombin"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "generated")
FONT = "Segoe UI, -apple-system, Helvetica, Arial, sans-serif"

THEMES = {
    "dark": {"bg": "#0d1117", "border": "#30363d", "text": "#e6edf3",
             "muted": "#8b949e", "accent": "#58a6ff", "track": "#1c2b3f",
             "pill": "#132238", "pill_text": "#9fd0ff"},
    "light": {"bg": "#ffffff", "border": "#d0d7de", "text": "#1f2328",
              "muted": "#59636e", "accent": "#0969da", "track": "#eaeef2",
              "pill": "#ddf4ff", "pill_text": "#0550ae"},
}
LANG_COLORS = {
    "Python": "#3572A5", "C": "#555555", "HTML": "#e34c26",
    "Jupyter Notebook": "#DA5B0B", "JavaScript": "#f1e05a", "CSS": "#563d7c",
    "Shell": "#89e051", "TeX": "#3D6117", "TSQL": "#e38c00", "Makefile": "#427819",
    "Swift": "#F05138", "C#": "#178600", "PowerShell": "#012456",
}


# ---------------------------------------------------------------- GitHub API

def gh_get(path):
    req = urllib.request.Request(API + path)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", f"{USERNAME}-profile-refresh")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode())


def fetch_repos():
    repos, page = [], 1
    while True:
        batch = gh_get(f"/users/{USERNAME}/repos?per_page=100&page={page}&type=owner")
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return [r for r in repos if not r.get("fork") and not r.get("private")]


def fetch_languages(repo_name):
    # Deliberately no try/except: a rate-limited or failed call must abort the
    # run so CI keeps yesterday's SVGs instead of committing a partial chart.
    return gh_get(f"/repos/{USERNAME}/{repo_name}/languages")


def fetch_commits_this_year(year):
    q = urllib.parse.quote(f"author:{USERNAME} committer-date:>={year}-01-01")
    try:
        return gh_get(f"/search/commits?q={q}&per_page=1")["total_count"]
    except Exception:
        return None


# ------------------------------------------------------------------ helpers

def ago(iso, now):
    then = dt.datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=dt.timezone.utc)
    days = (now - then).days
    if days <= 0:
        return "today"
    if days == 1:
        return "yesterday"
    if days < 14:
        return f"{days} days ago"
    if days < 60:
        return f"{days // 7} weeks ago"
    if days < 730:
        return f"{days // 30} months ago"
    return f"{days // 365} years ago"


def frame(w, h, t, body, label):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(label)}">\n'
            f'  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="12" '
            f'fill="{t["bg"]}" stroke="{t["border"]}"/>\n{body}\n</svg>\n')


def txt(x, y, s, size, fill, weight=400, anchor="start", extra=""):
    return (f'  <text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>'
            f'{escape(s)}</text>')


def fade_in(i, step=0.12):
    return (f'<animate attributeName="opacity" from="0" to="1" dur="0.6s" '
            f'begin="{i*step:.2f}s" fill="freeze"/>')


# ------------------------------------------------------------------- cards

def build_stats(t, tiles, updated):
    w, h = 900, 132
    tw = w / len(tiles)
    parts = []
    for i, (num, l1, l2) in enumerate(tiles):
        cx = tw * i + tw / 2
        parts.append(f'  <g opacity="0">{fade_in(i, 0.15)}')
        parts.append(txt(f"{cx:.1f}", 50, num, 30, t["accent"], 700, "middle"))
        parts.append(txt(f"{cx:.1f}", 72, l1, 12, t["text"], 400, "middle"))
        parts.append(txt(f"{cx:.1f}", 87, l2, 12, t["text"], 400, "middle"))
        parts.append("  </g>")
        if i:
            parts.append(f'  <line x1="{tw*i:.1f}" y1="24" x2="{tw*i:.1f}" y2="96" stroke="{t["border"]}"/>')
    parts.append(txt(w / 2, h - 14, f"live from the GitHub API · refreshed {updated}",
                     10, t["muted"], 400, "middle"))
    return frame(w, h, t, "\n".join(parts), "Profile stats")


def build_langs(t, totals, skipped=()):
    total = sum(totals.values()) or 1
    top = sorted(totals.items(), key=lambda kv: -kv[1])[:6]
    w, h = 900, 62 + len(top) * 30 + 28
    label_w, pct_w, pad = 170, 60, 24
    bar = w - 2 * pad - label_w - pct_w
    parts = [txt(pad, 34, "Most used languages", 15, t["accent"], 700)]
    for i, (name, n) in enumerate(top):
        y = 62 + i * 30
        pct = 100 * n / total
        bw = max(3, bar * pct / 100)
        color = LANG_COLORS.get(name, "#8b949e")
        parts.append(txt(pad, y + 11, name, 12.5, t["text"]))
        parts.append(f'  <rect x="{pad+label_w}" y="{y+2}" width="{bar}" height="10" rx="5" fill="{t["track"]}"/>')
        parts.append(f'  <rect x="{pad+label_w}" y="{y+2}" width="0" height="10" rx="5" fill="{color}">'
                     f'<animate attributeName="width" from="0" to="{bw:.1f}" dur="1.1s" '
                     f'begin="{i*0.1:.2f}s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/></rect>')
        parts.append(txt(w - pad, y + 11, f"{pct:.1f}%", 12, t["muted"], 400, "end"))
    note = "by bytes of code across public, non-fork repos"
    if skipped:
        note += " · excludes " + ", ".join(skipped)
    parts.append(txt(pad, h - 14, note, 10, t["muted"]))
    return frame(w, h, t, "\n".join(parts), "Most used languages")


def build_activity(t, repos, now):
    recent = sorted(repos, key=lambda r: r["pushed_at"], reverse=True)[:5]
    w, h = 900, 58 + len(recent) * 34 + 10
    parts = [txt(24, 34, "Recently pushed", 15, t["accent"], 700),
             txt(w - 24, 34, f"updated daily · {now:%Y-%m-%d}", 11, t["muted"], 400, "end")]
    for i, r in enumerate(recent):
        y = 64 + i * 34
        lang = r.get("language") or "—"
        color = LANG_COLORS.get(lang, "#8b949e")
        desc = (r.get("description") or "").strip()
        if len(desc) > 78:
            desc = desc[:75].rstrip() + "…"
        parts.append(f'  <g opacity="0">{fade_in(i)}')
        parts.append(f'  <circle cx="30" cy="{y}" r="5" fill="{color}"/>')
        parts.append(txt(44, y + 4.5, r["name"], 13.5, t["text"], 700))
        parts.append(txt(250, y + 4.5, desc, 12, t["muted"]))
        parts.append(txt(w - 24, y + 4.5, ago(r["pushed_at"], now), 12, t["accent"], 600, "end"))
        parts.append("  </g>")
    return frame(w, h, t, "\n".join(parts), "Recently pushed repositories")


def build_card(t, p, repo, now):
    w, h = 440, 190
    pad = 22
    langs = p.get("langs") or [l for l in [(repo or {}).get("language")] if l]
    stars = (repo or {}).get("stargazers_count", 0)
    pushed = ago(repo["pushed_at"], now) if repo else ""
    parts = [txt(pad, 30, p["kicker"], 10.5, t["muted"], 600, extra='letter-spacing="1.2"'),
             txt(pad, 54, p["title"], 18, t["accent"], 700)]
    for i, line in enumerate(textwrap.wrap(p["tagline"], 62)[:3]):
        parts.append(txt(pad, 80 + i * 18, line, 12.5, t["text"]))
    hl = p["highlight"]
    pill_w = min(w - 2 * pad, 20 + len(hl) * 6.2)
    parts.append(f'  <rect x="{pad}" y="128" width="{pill_w:.0f}" height="24" rx="12" fill="{t["pill"]}"/>')
    parts.append(txt(pad + 10, 144, hl, 11.5, t["pill_text"], 600))
    meta = []
    x = pad
    for lang in langs:
        meta.append(f'  <circle cx="{x+5}" cy="171" r="5" fill="{LANG_COLORS.get(lang, "#8b949e")}"/>')
        meta.append(txt(x + 15, 175, lang, 11.5, t["muted"]))
        x += 15 + len(lang) * 6.6 + 12
    right = f"★ {stars} · pushed {pushed}" if repo else ""
    if p.get("demo"):
        right += " · ▶ live demo"
    meta.append(txt(w - pad, 175, right, 11.5, t["muted"], 400, "end"))
    parts.extend(meta)
    return frame(w, h, t, "\n".join(parts), f'{p["title"]}: {p["tagline"]}')


# --------------------------------------------------------------------- main

def write(rel, content):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    with open(os.path.join(ROOT, "scripts", "featured.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    now = dt.datetime.now(dt.timezone.utc)
    repos = fetch_repos()
    by_name = {r["name"]: r for r in repos}

    excl = cfg.get("language_exclusions", {})
    skip_repos = set(excl.get("repos", {}))
    skip_langs = set(excl.get("languages", []))
    totals = {}
    for r in repos:
        if r["name"] in skip_repos:
            continue
        for lang, n in fetch_languages(r["name"]).items():
            if lang not in skip_langs:
                totals[lang] = totals.get(lang, 0) + n

    commits = fetch_commits_this_year(now.year)
    live = sum(1 for r in repos if r.get("has_pages"))
    tiles = [
        (str(len(repos)), "public", "repos"),
        (str(live), "live", "demos"),
        (str(len(set(cfg["quant_sim_repos"]) & by_name.keys())), "quant / sim", "projects"),
        ("—" if commits is None else str(commits), f"commits", f"in {now.year}"),
    ]
    for name, t in THEMES.items():
        write(f"stats-{name}.svg", build_stats(t, tiles, f"{now:%Y-%m-%d}"))
        write(f"langs-{name}.svg", build_langs(t, totals, sorted(skip_langs)))
        write(f"activity-{name}.svg", build_activity(t, repos, now))
        for p in cfg["featured"]:
            write(f"cards/{p['repo']}-{name}.svg", build_card(t, p, by_name.get(p["repo"]), now))

    print(f"Refreshed assets/generated from {len(repos)} public repos "
          f"({live} with Pages, {commits} commits in {now.year}).")


if __name__ == "__main__":
    main()

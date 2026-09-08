#!/usr/bin/env python3
"""
Regenerates assets/top-langs.svg and assets/profile-stats.svg from real,
live GitHub data — no third-party badge service involved.

Run locally:   GITHUB_TOKEN=... python3 scripts/generate_stats.py
Run in CI:     wired up in .github/workflows/update-stats.yml (uses the
               repo's built-in GITHUB_TOKEN, no secrets to configure).
"""
import json
import os
import urllib.request

USERNAME = "claudialbombin"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Repos that count as "quant / simulation" projects and repos that ship a
# parallel Python + C implementation. Maintained by hand since GitHub has
# no reliable way to infer this automatically — update as new repos land.
QUANT_SIM_REPOS = {
    "pitwall", "monte-carlo-option-pricer", "beat-the-dealer",
    "scm-heston-filter", "mus-stochastic-suite",
}
DUAL_PY_C_REPOS = {"beat-the-dealer", "monte-carlo-option-pricer", "mus-stochastic-suite"}

# Not derivable from the API — bump by hand once a year.
YEARS_AT_ICAI = 2

API = "https://api.github.com"


def gh_get(path):
    req = urllib.request.Request(API + path)
    req.add_header("Accept", "application/vnd.github+json")
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
    return [r for r in repos if not r.get("fork")]


def fetch_languages(repo_name):
    try:
        return gh_get(f"/repos/{USERNAME}/{repo_name}/languages")
    except Exception:
        return {}


def build_top_langs_svg(lang_totals):
    total = sum(lang_totals.values()) or 1
    colors = {
        "Python": "#3776AB", "C": "#00599C", "HTML": "#E34C26",
        "Jupyter Notebook": "#F37626", "JavaScript": "#f1e05a",
        "CSS": "#563d7c", "Shell": "#89E051", "TeX": "#3D6117",
        "SQL": "#e38c00", "R": "#198CE7",
    }
    top = sorted(lang_totals.items(), key=lambda kv: -kv[1])[:5]

    W, H = 480, 20 + 46 + len(top) * 37 + 24
    pad_l, label_w, pct_w = 24, 140, 40
    bar_max_w = W - 24 - label_w - pct_w
    rows, y = [], 66
    for i, (name, n) in enumerate(top):
        pct = 100 * n / total
        w = max(3, bar_max_w * pct / 100)
        color = colors.get(name, "#8b98a5")
        rows.append(f'''
    <g transform="translate({pad_l},{y})">
      <text x="0" y="14" font-family="Segoe UI, Verdana, sans-serif" font-size="13" fill="#c9d9ec">{name}</text>
      <rect x="{label_w}" y="4" width="{bar_max_w}" height="10" rx="5" fill="#1c2b3f"/>
      <rect x="{label_w}" y="4" width="0" height="10" rx="5" fill="{color}">
        <animate attributeName="width" from="0" to="{w:.1f}" dur="1.1s" begin="{i*0.12:.2f}s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/>
      </rect>
      <text x="{label_w + bar_max_w + 10}" y="14" font-family="Segoe UI, Verdana, sans-serif" font-size="12" fill="#8b98a5">{pct:.1f}%</text>
    </g>''')
        y += 37

    return f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Most used languages">
  <defs><clipPath id="r"><rect width="{W}" height="{H}" rx="12"/></clipPath></defs>
  <g clip-path="url(#r)">
    <rect width="{W}" height="{H}" fill="#0d1117"/>
    <rect width="{W}" height="{H}" fill="none" stroke="#30363d" stroke-width="1"/>
    <text x="{pad_l}" y="30" font-family="Segoe UI, Verdana, sans-serif" font-size="16" font-weight="700" fill="#58a6ff">Most Used Languages</text>
    {''.join(rows)}
    <text x="{pad_l}" y="{H-12}" font-family="Segoe UI, Verdana, sans-serif" font-size="10" fill="#586069">live from the GitHub API, by bytes across public repos</text>
  </g>
</svg>
'''


def build_profile_stats_svg(repo_count, quant_count, dual_count):
    stats = [
        (str(repo_count), ["Public", "repos"]),
        (str(quant_count), ["Quant / sim", "projects"]),
        (str(dual_count), ["Python + C", "repos"]),
        (str(YEARS_AT_ICAI), ["Years @", "ICAI"]),
    ]
    W, H = 480, 120
    tile_w = W / len(stats)
    tiles = []
    for i, (num, label_lines) in enumerate(stats):
        x = tile_w * i
        delay = i * 0.15
        label_tspans = "".join(
            f'<tspan x="{tile_w/2:.1f}" dy="{0 if j==0 else 14}">{line}</tspan>'
            for j, line in enumerate(label_lines)
        )
        tiles.append(f'''
    <g transform="translate({x:.1f},0)" opacity="0">
      <animate attributeName="opacity" from="0" to="1" dur="0.6s" begin="{delay:.2f}s" fill="freeze"/>
      <text x="{tile_w/2:.1f}" y="46" text-anchor="middle" font-family="Segoe UI, Verdana, sans-serif" font-size="28" font-weight="700" fill="#58a6ff">{num}</text>
      <text x="{tile_w/2:.1f}" y="66" text-anchor="middle" font-family="Segoe UI, Verdana, sans-serif" font-size="10.5" fill="#c9d9ec">{label_tspans}</text>
    </g>''')
        if i > 0:
            tiles.append(f'<line x1="{x:.1f}" y1="20" x2="{x:.1f}" y2="{H-20}" stroke="#30363d" stroke-width="1"/>')

    return f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Profile stats">
  <defs><clipPath id="r"><rect width="{W}" height="{H}" rx="12"/></clipPath></defs>
  <g clip-path="url(#r)">
    <rect width="{W}" height="{H}" fill="#0d1117"/>
    <rect width="{W}" height="{H}" fill="none" stroke="#30363d" stroke-width="1"/>
    {''.join(tiles)}
  </g>
</svg>
'''


def main():
    repos = fetch_repos()
    repo_names = {r["name"] for r in repos}

    lang_totals = {}
    for r in repos:
        for lang, n in fetch_languages(r["name"]).items():
            lang_totals[lang] = lang_totals.get(lang, 0) + n

    quant_count = len(QUANT_SIM_REPOS & repo_names)
    dual_count = len(DUAL_PY_C_REPOS & repo_names)

    os.makedirs("assets", exist_ok=True)
    with open("assets/top-langs.svg", "w") as f:
        f.write(build_top_langs_svg(lang_totals))
    with open("assets/profile-stats.svg", "w") as f:
        f.write(build_profile_stats_svg(len(repos), quant_count, dual_count))

    print(f"Updated assets/top-langs.svg and assets/profile-stats.svg "
          f"from {len(repos)} repos.")


if __name__ == "__main__":
    main()

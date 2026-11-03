<div align="center">

<img src="assets/header.svg" alt="Claudia Lopez Bombin: Mathematical Engineering and AI student at ICAI and 42 Madrid" width="100%"/>

<br/>

<a href="https://claudialbombin.github.io/"><img src="assets/badges/portfolio.svg" alt="Portfolio"/></a>
<a href="https://linkedin.com/in/claudia-lopez-bombin"><img src="assets/badges/linkedin.svg" alt="LinkedIn"/></a>
<a href="mailto:claudialbombin@gmail.com"><img src="assets/badges/email.svg" alt="Email"/></a>
<a href="https://x.com/claudialbzz"><img src="assets/badges/x.svg" alt="X"/></a>
<a href="https://instagram.com/claudialbzz"><img src="assets/badges/instagram.svg" alt="Instagram"/></a>

<br/><br/>

<a href="#about"><b>About</b></a> ·
<a href="#projects"><b>Projects</b></a> ·
<a href="#more"><b>More</b></a> ·
<a href="#tech-stack"><b>Tech stack</b></a> ·
<a href="#activity"><b>Activity</b></a>

</div>

<br/>

<div id="about"></div>

## 💫 About me

I'm a third-year **Mathematical Engineering & Artificial Intelligence** student at **ICAI, Universidad Pontificia Comillas**, and a **42 Madrid (Fundación Telefónica) Cursus** student on the side. Most of what lives here comes back to one idea: **turning uncertainty into a number I can act on**. That means Monte Carlo option pricing, an F1 pit-stop strategy solved as a Markov Decision Process, particle filters for stochastic volatility and a blackjack solver, alongside ICAI coursework and 42's C curriculum.

I also compete in academic and British Parliamentary debate, which is where the habit of stress-testing an argument before trusting it comes from. I apply the same instinct to a model before trusting its output, and every project below reports its limitations next to its results.

```python
class Claudia:
    studies   = ["iMAT @ ICAI (year 3)", "42 Madrid Cursus"]
    builds    = ["stochastic simulation", "quant models", "small tools I actually use"]
    languages = ["Python", "C", "JavaScript"]
    debates   = "British Parliamentary"
    looking_for = "analytical / quant internships, summer 2027"
```

<div id="projects"></div>

## 🚀 Featured projects

<sub>Cards are regenerated daily from the GitHub API (stars, last push). Click a card to open the live demo, or the repo if there is none.</sub>

<table>
<tr>
<td width="50%" valign="top">
<a href="https://claudialbombin.github.io/pitwall/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/cards/pitwall-dark.svg"/>
  <img src="assets/generated/cards/pitwall-light.svg" alt="pitwall: Pit-stop timing as a finite-horizon Markov Decision Process, solved by backward induction, with tyre wear from Gaussian Process regression and Bayesian safety-car estimates." width="100%"/>
</picture>
</a>
<p align="center"><a href="https://claudialbombin.github.io/pitwall/"><b>▶ Live demo</b></a> · <a href="https://github.com/claudialbombin/pitwall"><b>Code</b></a></p>
<details><summary>How it works</summary>
<ul><li>Tyre degradation per compound fitted with <b>Gaussian Process regression</b> on FastF1 lap data; safety-car probability by Bayesian updating.</li><li>Optimal pit-lap policy from <b>backward induction</b> over the full state space, stress-tested with Monte Carlo race simulations.</li><li>Backtested against real 2023 races. Honest result: a slight edge in head-to-head comparisons, not yet a proven strategy advantage.</li></ul>
</details>
</td>
<td width="50%" valign="top">
<a href="https://claudialbombin.github.io/beat-the-dealer/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/cards/beat-the-dealer-dark.svg"/>
  <img src="assets/generated/cards/beat-the-dealer-light.svg" alt="beat-the-dealer: Blackjack basic strategy derived by simulation, checked cell by cell against an exact solver, plus a Hi-Lo counting study over a billion rounds." width="100%"/>
</picture>
</a>
<p align="center"><a href="https://claudialbombin.github.io/beat-the-dealer/"><b>▶ Live demo</b></a> · <a href="https://github.com/claudialbombin/beat-the-dealer"><b>Code</b></a></p>
<details><summary>How it works</summary>
<ul><li>Basic strategy derived by Monte Carlo (with common random numbers for variance reduction), then checked against an exact solver: <b>380/380</b> decisions agree.</li><li>A C shoe simulator runs the <b>Hi-Lo</b> study: +0.50% player edge per true count.</li><li>The site lets you play with a coach, drill the chart and watch Monte Carlo estimates converge live in a Web Worker.</li></ul>
</details>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/claudialbombin/monte-carlo-option-pricer">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/cards/monte-carlo-option-pricer-dark.svg"/>
  <img src="assets/generated/cards/monte-carlo-option-pricer-light.svg" alt="monte-carlo-option-pricer: European, Asian and barrier options under Black-Scholes and Heston, with Greeks by pathwise, likelihood-ratio, finite-difference and closed-form methods." width="100%"/>
</picture>
</a>
<p align="center"><a href="https://github.com/claudialbombin/monte-carlo-option-pricer"><b>Code</b></a></p>
<details><summary>How it works</summary>
<ul><li>Black-Scholes and Heston paths (Euler, with absorption or reflection at zero variance) for European, Asian and barrier payoffs.</li><li>Greeks four ways, showing why pathwise fails on discontinuous payoffs and likelihood-ratio does not.</li><li>Python and C engines side by side, validated against closed-form prices.</li></ul>
</details>
</td>
<td width="50%" valign="top">
<a href="https://github.com/claudialbombin/scm-heston-filter">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/cards/scm-heston-filter-dark.svg"/>
  <img src="assets/generated/cards/scm-heston-filter-light.svg" alt="scm-heston-filter: A particle filter that tracks the hidden variance of the Heston model from noisy price observations alone: the estimation side of the pricer's problem." width="100%"/>
</picture>
</a>
<p align="center"><a href="https://github.com/claudialbombin/scm-heston-filter"><b>Code</b></a></p>
<details><summary>How it works</summary>
<ul><li>Bootstrap particle filter for the latent variance of the Heston model, observed only through noisy prices.</li><li>Convergence study by particle count, plus the implied-volatility smile the Heston model produces.</li></ul>
</details>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://claudialbombin.github.io/cececat/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/cards/cececat-dark.svg"/>
  <img src="assets/generated/cards/cececat-light.svg" alt="cececat: A debate tournament manager in a single HTML file: guided setup, pairings, judges that actually rotate, live scoring from each judge's phone and standings." width="100%"/>
</picture>
</a>
<p align="center"><a href="https://claudialbombin.github.io/cececat/"><b>▶ Live demo</b></a> · <a href="https://github.com/claudialbombin/cececat"><b>Code</b></a></p>
<details><summary>How it works</summary>
<ul><li>Pairings, judge rotation, scoring and standings all run in the browser; state autosaves locally.</li><li>Judges can score from their phones in real time through Firestore; links are sent by email.</li><li>Built for the Académico and British Parliamentary formats I compete in.</li></ul>
</details>
</td>
<td width="50%" valign="top">
<a href="https://github.com/claudialbombin/salchi-helper">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/cards/salchi-helper-dark.svg"/>
  <img src="assets/generated/cards/salchi-helper-light.svg" alt="salchi-helper: A tiny dachshund that floats above every window typing at its laptop. The sticker counts your pending tasks; hover and the whole list opens." width="100%"/>
</picture>
</a>
<p align="center"><a href="https://github.com/claudialbombin/salchi-helper"><b>Code</b></a></p>
<details><summary>How it works</summary>
<ul><li>Builds for macOS, Windows and Linux, each in two editions (local or Notion) that share all their code.</li><li>Optional Notion back end, so the same list follows you to your phone and an AI assistant can add tasks.</li><li>Dated tasks can sync to Google Calendar and disappear when ticked off.</li></ul>
</details>
</td>
</tr>
</table>

<div id="more"></div>

## 🧩 More I've built

| | Project | What it is |
|---|---|---|
| 🫁 | [**pause**](https://github.com/claudialbombin/pause) · [demo](https://claudialbombin.github.io/pause/) | Installable PWA that puts a short breathing exercise between you and Instagram, TikTok or YouTube: friction, not a hard block. |
| 🍳 | [**recetario-familiar**](https://github.com/claudialbombin/recetario-familiar) · [demo](https://claudialbombin.github.io/recetario-familiar/) | My family's recipe book as a small web app. |
| 🌐 | [**claudialbombin.github.io**](https://github.com/claudialbombin/claudialbombin.github.io) · [site](https://claudialbombin.github.io/) | My portfolio: one page per project with the question, the method and the numbers. |
| 🖥️ | [**42**](https://github.com/claudialbombin/42) | 42 Madrid Piscine and Cursus in C: [Libft](https://github.com/claudialbombin/42/tree/main/Cursus/Rank00/Libft), [ft_printf](https://github.com/claudialbombin/42/tree/main/Cursus/Rank01/ft_printf), [get_next_line](https://github.com/claudialbombin/42/tree/main/Cursus/Rank01/get_next_line), [push_swap](https://github.com/claudialbombin/42/tree/main/Cursus/Rank01/push_swap), [BSQ](https://github.com/claudialbombin/42/tree/main/Piscine/BSQ), [A-maze-ing](https://github.com/claudialbombin/42/tree/main/Cursus/Rank02/A-maze-ing). |
| 🎓 | [**2imat**](https://github.com/claudialbombin/2imat) · [**3imat**](https://github.com/claudialbombin/3imat) | ICAI coursework: data acquisition, ML, SQL/MongoDB/Neo4j, visualisation (year 2); year 3 just started. |
| 🀄 | [**mus-stochastic-suite**](https://github.com/claudialbombin/mus-stochastic-suite) <sub>planned</sub> | A Mus engine with bots and Monte Carlo strategy analysis. Design stage, no code yet. |

<div id="tech-stack"></div>

## 💻 Tech stack

<sub>Each badge links to a repo where that tool is actually used.</sub>

<p><sub><b>Languages</b></sub></p>
<a href="https://github.com/claudialbombin/pitwall"><img src="assets/tech/python.svg" alt="Python"/></a>
<a href="https://github.com/claudialbombin/beat-the-dealer"><img src="assets/tech/c.svg" alt="C"/></a>
<a href="https://github.com/claudialbombin/beat-the-dealer"><img src="assets/tech/javascript.svg" alt="JavaScript"/></a>

<p><sub><b>Data science & ML</b></sub></p>
<a href="https://github.com/claudialbombin/pitwall"><img src="assets/tech/numpy.svg" alt="NumPy"/></a>
<a href="https://github.com/claudialbombin/pitwall"><img src="assets/tech/pandas.svg" alt="pandas"/></a>
<a href="https://github.com/claudialbombin/scm-heston-filter"><img src="assets/tech/matplotlib.svg" alt="Matplotlib"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/seaborn.svg" alt="Seaborn"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/scikit-learn.svg" alt="scikit-learn"/></a>
<a href="https://github.com/claudialbombin/monte-carlo-option-pricer"><img src="assets/tech/jupyter.svg" alt="Jupyter"/></a>

<p><sub><b>Databases</b></sub></p>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/mysql.svg" alt="MySQL"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/mongodb.svg" alt="MongoDB"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/neo4j.svg" alt="Neo4j"/></a>

<p><sub><b>Dashboards & viz</b></sub></p>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/streamlit.svg" alt="Streamlit"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/tableau.svg" alt="Tableau"/></a>

<p><sub><b>Web</b></sub></p>
<a href="https://github.com/claudialbombin/cececat"><img src="assets/tech/html.svg" alt="HTML"/></a>
<a href="https://github.com/claudialbombin/beat-the-dealer"><img src="assets/tech/css.svg" alt="CSS"/></a>

<p><sub><b>Testing & CI/CD</b></sub></p>
<a href="https://github.com/claudialbombin/monte-carlo-option-pricer"><img src="assets/tech/pytest.svg" alt="pytest"/></a>
<a href="./.github/workflows/refresh-profile.yml"><img src="assets/tech/github-actions.svg" alt="GitHub Actions"/></a>

<div id="activity"></div>

## 📊 Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/activity-dark.svg"/>
  <img src="assets/generated/activity-light.svg" alt="Repositories I pushed to most recently" width="100%"/>
</picture>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/stats-dark.svg"/>
  <img src="assets/generated/stats-light.svg" alt="Profile stats" width="100%"/>
</picture>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/langs-dark.svg"/>
  <img src="assets/generated/langs-light.svg" alt="Most used languages" width="100%"/>
</picture>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile-3d-contrib/profile-night-green.svg"/>
  <img src="profile-3d-contrib/profile-green-animate.svg" alt="3D contribution calendar" width="100%"/>
</picture>

</div>

<sub>Language shares exclude Jupyter notebooks (their bytes are mostly outputs) and two repos whose bundled files distort the count; the reasons are listed in <a href="scripts/featured.json"><code>featured.json</code></a>.</sub>

<details>
<summary><b>🐍 Watch a snake eat my contribution graph</b></summary>
<br/>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/claudialbombin/claudialbombin/output/github-contribution-grid-snake-dark.svg"/>
  <img alt="A snake eating my GitHub contribution graph" src="https://raw.githubusercontent.com/claudialbombin/claudialbombin/output/github-contribution-grid-snake.svg" width="100%"/>
</picture>
</details>

---

<div align="center">
<sub>This profile rebuilds itself every morning: <a href="scripts/generate_stats.py"><code>generate_stats.py</code></a> reads <a href="scripts/featured.json"><code>featured.json</code></a> and the GitHub API, and <a href="./.github/workflows/refresh-profile.yml">a GitHub Action</a> commits the new SVGs. No third-party badge services.</sub>
</div>

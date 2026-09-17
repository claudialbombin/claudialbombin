<div align="center">

<img src="assets/header.svg" alt="Claudia Lopez Bombin" width="100%"/>

<br/>

<a href="https://linkedin.com/in/claudia-lopez-bombin"><img src="assets/badges/linkedin.svg" alt="LinkedIn"/></a>
<a href="https://x.com/@claudialbzz"><img src="assets/badges/x.svg" alt="X"/></a>
<a href="mailto:claudialbombin@gmail.com"><img src="assets/badges/email.svg" alt="Email"/></a>
<a href="https://instagram.com/@claudialbzz"><img src="assets/badges/instagram.svg" alt="Instagram"/></a>

<br/><br/>

<a href="#about"><b>About</b></a> ·
<a href="#projects"><b>Projects</b></a> ·
<a href="#tech-stack"><b>Tech Stack</b></a> ·
<a href="#analytics"><b>Analytics</b></a> ·
<a href="#snake"><b>Snake 🐍</b></a>

</div>

<br/>

<div id="about"></div>

## 💫 About Me

I'm a third-year **Mathematical Engineering & Artificial Intelligence** student at **ICAI, Universidad Pontificia Comillas**, and a **42 Madrid (Fundación Telefónica) Cursus** student on the side. Most of what lives in my repositories comes back to the same idea: **turning uncertainty into a number I can act on** — Monte Carlo option pricing, an F1 pit-stop strategy solved as a Markov Decision Process, particle filters for stochastic volatility, and a Hi-Lo blackjack solver, alongside my ICAI coursework and 42's C curriculum.

I also compete in academic and parliamentary debate (British Parliamentary format), which is where the habit of stress-testing an argument before trusting it comes from — the same instinct I apply to a model before trusting its output.

```txt
class Claudia:
    def __init__(self):
        self.role        = "iMAT student @ ICAI + 42 Madrid Cursus"
        self.builds_with  = ["Python", "C", "stochastic simulation"]
        self.currently    = "F1 pit-stop optimization (MDP) · options pricing engine"
        self.also_does    = "British Parliamentary debate"
```

<details>
<summary><b>🔭 quick facts</b> (click to expand)</summary>
<br/>
<ul>
<li>🎓 iMAT program (Mathematical Engineering &amp; AI) — ICAI, Comillas — year 3</li>
<li>🖥️ 42 Madrid Fundación Telefónica — Cursus (C, algorithms, systems)</li>
<li>🔭 Currently building <strong><a href="https://github.com/claudialbombin/pitwall">pitwall</a></strong>, a stochastic F1 pit-stop optimizer, and a dual Python/C <strong><a href="https://github.com/claudialbombin/monte-carlo-option-pricer">options pricing engine</a></strong></li>
<li>🤝 Open to collaborating on open-source simulation/ML tooling and data engineering projects</li>
<li>💬 Ask me about Monte Carlo methods, Python↔C performance trade-offs, or debate case construction</li>
<li>⚡ Fun fact: constructing a debate case and debugging a model are the same exercise — both mean tracing a conclusion back to the premise that's actually wrong</li>
</ul>
</details>

<br/>

<div id="projects"></div>

## 🚀 Featured Projects

<table>
<tr>
<td width="50%" valign="top">
<h3>🏎️ <a href="https://github.com/claudialbombin/pitwall">pitwall</a></h3>
<p>Stochastic <strong>F1 pit-stop strategy optimizer</strong>: a Markov Decision Process solved over tyre-degradation and safety-car models, calibrated with Gaussian Process Regression and Bayesian inference, backtested against real race data via Monte Carlo simulation — with an interactive web simulator to explore the resulting strategy.</p>
<p><code>Python</code> <code>MDP</code> <code>Bayesian inference</code> <code>Monte Carlo</code></p>
</td>
<td width="50%" valign="top">
<h3>📈 <a href="https://github.com/claudialbombin/monte-carlo-option-pricer">monte-carlo-option-pricer</a></h3>
<p>Option pricing engine covering <strong>European, Asian and barrier options</strong> under Black-Scholes and Heston stochastic volatility, with Greeks computed four ways (pathwise, likelihood-ratio, finite-difference, closed-form). Parallel Python and C implementations, 77 unit tests.</p>
<p><code>Python</code> <code>C</code> <code>Quant finance</code></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3>🃏 <a href="https://github.com/claudialbombin/beat-the-dealer">beat-the-dealer</a></h3>
<p>Blackjack solved two ways: Monte Carlo simulation derives optimal basic strategy, then a <strong>Hi-Lo card-counting</strong> layer shows the edge it buys — expected value rising roughly linearly with the true count. Dual Python/C implementation, the C version written under 42-style constraints (no dynamic memory, ≤25 lines per function).</p>
<p><code>Python</code> <code>C</code> <code>Monte Carlo</code></p>
</td>
<td width="50%" valign="top">
<h3>🎲 <a href="https://github.com/claudialbombin/scm-heston-filter">scm-heston-filter</a></h3>
<p>A <strong>particle filter</strong> (Sequential Monte Carlo) that tracks the unobserved volatility state of the Heston model from noisy price observations alone — the estimation half of the same stochastic-volatility problem <code>monte-carlo-option-pricer</code> prices.</p>
<p><code>Python</code> <code>Sequential Monte Carlo</code></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3>🫁 <a href="https://github.com/claudialbombin/pause">pause</a></h3>
<p>An installable <strong>PWA</strong> that puts a short breathing exercise between you and Instagram/TikTok/YouTube (or any app you name) — friction instead of a hard block, aimed at breaking the autopilot open-and-scroll habit.</p>
<p><code>JavaScript</code> <code>PWA</code> <code>Wellbeing</code></p>
</td>
<td width="50%" valign="top">
<h3>🀄 <a href="https://github.com/claudialbombin/mus-stochastic-suite">mus-stochastic-suite</a> <sub>· early stage</sub></h3>
<p>Planned: an interactive <strong>Mus</strong> (Spanish card game) suite — local multiplayer, bots at adjustable difficulty, a beginner tutorial, and dual Python/C engines that simulate thousands of games to model optimal strategy.</p>
<p><code>Python</code> <code>C</code> <code>Game theory</code></p>
</td>
</tr>
</table>

<div align="center">
<sub>Coursework & systems programming: <a href="https://github.com/claudialbombin/2imat"><b>2imat</b></a> — ICAI year-2 hub (data acquisition, ML, SQL/MongoDB) · 42 Madrid Cursus exercises in C: <a href="https://github.com/claudialbombin/BSQ">BSQ</a>, <a href="https://github.com/claudialbombin/push_swap">push_swap</a>, <a href="https://github.com/claudialbombin/42">42</a></sub>
</div>

<br/>

<div id="tech-stack"></div>

## 💻 Tech Stack

<sub>Every badge below is a real link, straight to the repo that proves it — self-hosted, animated, no badge service. Click one.</sub>

<br/>

<p><sub><b>Languages</b></sub></p>
<a href="https://github.com/claudialbombin/pitwall"><img src="assets/tech/python.svg" alt="Python"/></a>
<a href="https://github.com/claudialbombin/beat-the-dealer"><img src="assets/tech/c.svg" alt="C"/></a>

<p><sub><b>Data Science & ML</b></sub></p>
<a href="https://github.com/claudialbombin/pitwall"><img src="assets/tech/numpy.svg" alt="NumPy"/></a>
<a href="https://github.com/claudialbombin/monte-carlo-option-pricer"><img src="assets/tech/pandas.svg" alt="Pandas"/></a>
<a href="https://github.com/claudialbombin/scm-heston-filter"><img src="assets/tech/matplotlib.svg" alt="Matplotlib"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/seaborn.svg" alt="Seaborn"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/scikit-learn.svg" alt="scikit-learn"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/jupyter.svg" alt="Jupyter"/></a>

<p><sub><b>Databases</b></sub></p>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/mysql.svg" alt="MySQL"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/mongodb.svg" alt="MongoDB"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/neo4j.svg" alt="Neo4j"/></a>

<p><sub><b>Dashboards & Viz</b></sub></p>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/streamlit.svg" alt="Streamlit"/></a>
<a href="https://github.com/claudialbombin/pitwall"><img src="assets/tech/plotly.svg" alt="Plotly"/></a>
<a href="https://github.com/claudialbombin/2imat"><img src="assets/tech/tableau.svg" alt="Tableau"/></a>

<p><sub><b>Testing & CI/CD</b></sub></p>
<a href="https://github.com/claudialbombin/monte-carlo-option-pricer"><img src="assets/tech/pytest.svg" alt="pytest"/></a>
<a href="./.github/workflows/snake.yml"><img src="assets/tech/github-actions.svg" alt="GitHub Actions"/></a>

<p><sub><b>Web</b></sub></p>
<a href="https://github.com/claudialbombin/pause"><img src="assets/tech/javascript.svg" alt="JavaScript"/></a>
<a href="https://github.com/claudialbombin/pitwall"><img src="assets/tech/html.svg" alt="HTML"/></a>
<a href="https://github.com/claudialbombin/pitwall"><img src="assets/tech/css.svg" alt="CSS"/></a>

<br/>

<sub>Every technology above was verified by grepping my own public repos (dependency files, imports, coursework folders) — not copied from a generic list. Dropped from my old badge list for lack of evidence: TensorFlow, PyTorch, R, CUDA, Figma, Adobe CC, Canva, PowerShell, Selenium, ArangoDB, SQL Server.</sub>

<br/>

<div id="analytics"></div>

## 📊 GitHub Analytics

<div align="center">

<img src="assets/profile-stats.svg" alt="Profile stats" width="480"/>

<br/><br/>

<img src="assets/top-langs.svg" alt="Most used languages" width="480"/>

</div>

<sub>Both cards above are plain SVG files that live in this repo (`assets/`) — nothing is fetched from a third-party server, so they always render. They're kept current automatically by <a href="./.github/workflows/update-stats.yml">a weekly GitHub Action</a> that pulls real numbers from the GitHub API and re-commits the SVGs.</sub>

<div id="snake"></div>

### 🐍 Contribution Snake

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/claudialbombin/claudialbombin/output/github-contribution-grid-snake-dark.svg" />
  <img alt="A snake eating my GitHub contribution graph" src="https://raw.githubusercontent.com/claudialbombin/claudialbombin/output/github-contribution-grid-snake.svg" width="100%"/>
</picture>

<sub>Generated by <a href="./.github/workflows/snake.yml">a GitHub Action</a> from my real contribution graph — re-runs nightly to stay in sync.</sub>

<br/>

---

<div align="center">
<sub>⭐ Feel free to explore my repositories and reach out for collaboration — details above.</sub>
</div>

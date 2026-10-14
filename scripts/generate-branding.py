"""Generate the profile's SVG artwork with the Python standard library."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
PALETTES = {
    "dark": dict(bg="#111315", card="#171b20", ink="#f3f1ec", muted="#b3b6ba", gold="#dfbd78", line="#343a42", blue="#83a9b8"),
    "light": dict(bg="#f6f8fa", card="#ffffff", ink="#20262e", muted="#56616e", gold="#8a651f", line="#d1d9e0", blue="#3e6c7c"),
}
MONOGRAM = '''<g fill="none" stroke="{gold}" stroke-width="4" stroke-linecap="square" stroke-linejoin="bevel" transform="translate(3 0) skewX(-6)">
<path d="M8 50 22 14 36 50M13 38h18"/>
<path d="M42 50V14h15l8 8v8l-8 8H42m13 0 12 12"/>
<path d="m89 18-4-4h-8l-8 8v5l18 9v8l-7 6h-8l-4-4"/>
</g>'''


def document(width, height, title, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif">{body}</g>
</svg>\n'''


def banner(p):
    return document(1000, 280, "Abhinav Ranjan Sulabh — Software Engineer", f'''
<defs>
  <radialGradient id="glow"><stop stop-color="{p['gold']}" stop-opacity=".15"/><stop offset="1" stop-color="{p['gold']}" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".8" fill="{p['muted']}" opacity=".17"/></pattern>
  <linearGradient id="edge"><stop stop-color="{p['gold']}"/><stop offset="1" stop-color="{p['blue']}"/></linearGradient>
</defs>
<style>
  .pulse {{ animation: breathe 5s ease-in-out infinite; }}
  .second {{ animation-delay: -2.5s; }}
  @keyframes breathe {{ 0%,100% {{ opacity:.4; }} 50% {{ opacity:1; }} }}
  @media (prefers-reduced-motion: reduce) {{ .pulse {{ animation:none; }} }}
</style>
<rect x="1" y="1" width="998" height="278" rx="22" fill="{p['bg']}" stroke="{p['line']}"/>
<rect x="560" y="2" width="438" height="276" rx="22" fill="url(#grid)"/>
<ellipse cx="785" cy="140" rx="290" ry="170" fill="url(#glow)"/>
<path d="M40 1h220" stroke="url(#edge)" stroke-width="3"/>
<text x="48" y="54" fill="{p['gold']}" font-size="14">Software engineer</text>
<text x="46" y="124" fill="{p['ink']}" font-size="38" font-weight="600" letter-spacing="-.5">Abhinav Ranjan</text>
<text x="46" y="178" fill="{p['gold']}" font-size="42" font-weight="600" letter-spacing="-.5">Sulabh.</text>
<path d="M48 222h55" stroke="{p['gold']}" stroke-width="2"/>
<text x="118" y="227" fill="{p['muted']}" font-size="15">Java, Python, and backend systems.</text>
<g transform="translate(115 0) scale(.82)">
<g fill="none" stroke="{p['gold']}" stroke-opacity=".32">
  <circle cx="808" cy="168" r="105"/>
  <circle cx="808" cy="168" r="125" stroke-dasharray="3 10"/>
  <path d="M703 168h-47v-62h-29M913 168h36v72M808 273v36h-66"/>
</g>
<g transform="translate(695 90) scale(2.35)">{MONOGRAM.format(gold=p['gold'])}</g>
<g fill="{p['bg']}" stroke="{p['blue']}" stroke-width="2">
  <rect x="589" y="88" width="48" height="36" rx="9"/>
  <rect x="923" y="241" width="49" height="37" rx="9"/>
  <rect x="704" y="288" width="49" height="36" rx="9"/>
</g>
<g fill="none" stroke="{p['blue']}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="m607 100-6 6 6 6m12-12 6 6-6 6m-4-14-4 16"/>
  <ellipse cx="948" cy="253" rx="10" ry="4"/><path d="M938 253v12c0 5 20 5 20 0v-12m-20 6c0 5 20 5 20 0"/>
  <path d="M719 313h18c8 0 8-12 1-12-1-10-15-10-17-1-8-2-10 11-2 13Z"/>
</g>
<circle class="pulse" cx="703" cy="168" r="4" fill="{p['gold']}"/>
<circle class="pulse second" cx="913" cy="168" r="4" fill="{p['blue']}"/>
</g>
''')


PROJECTS = [
    ("banking", "01", "Backend", "Banking System", ("Java banking APIs with JDBC", "persistence and TTL caching."), ("Java", "JDBC", "MySQL"), "bank"),
    ("dns", "02", "Networking", "DNS in Java", ("DNS resolution, caching,", "and DNSSEC concepts."), ("Java", "DNS", "Caching"), "network"),
    ("forecasting", "03", "Forecasting", "Power Price Forecasting", ("A Python pipeline for power", "price forecasts and validation."), ("Python", "Pandas", "Scikit-learn"), "chart"),
    ("federated", "04", "Machine learning", "Federated Intrusion Detection", ("Network intrusion detection", "with differential privacy."), ("Python", "Federated ML", "Privacy"), "shield"),
]


def project(p, entry):
    slug, number, category, title, description, tags, icon = entry
    artwork = {
        "bank": '<path d="m5 16 23-12 23 12M10 19h36M13 22v22m15-22v22m15-22v22M7 48h42"/>',
        "network": '<circle cx="28" cy="28" r="6"/><circle cx="8" cy="8" r="4"/><circle cx="48" cy="8" r="4"/><circle cx="8" cy="48" r="4"/><circle cx="48" cy="48" r="4"/><path d="m11 11 13 13m8 0 13-13M11 45l13-13m8 0 13 13"/>',
        "chart": '<path d="M5 5v44h46M10 39l10-13 10 6 17-23m-9 0h9v9"/>',
        "shield": '<path d="m28 3 21 8v17c0 14-21 24-21 24S7 42 7 28V11Z"/><path d="m17 27 8 8 14-17"/>',
    }[icon]
    title_size = 17 if len(title) > 25 else 18
    pills = []
    x = 24
    for tag in tags:
        width = len(tag) * 7 + 22
        pills.append(f'<rect x="{x}" y="151" width="{width}" height="23" rx="6" fill="{p["bg"]}" stroke="{p["line"]}"/><text x="{x+11}" y="167" fill="{p["muted"]}" font-size="12">{escape(tag)}</text>')
        x += width + 8
    return document(420, 190, title + ". " + " ".join(description), f'''
<defs><linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{p['gold']}" stop-opacity=".08"/><stop offset="1" stop-color="{p['gold']}" stop-opacity="0"/></linearGradient></defs>
<rect x="1" y="1" width="418" height="188" rx="14" fill="{p['card']}" stroke="{p['line']}"/>
<rect x="2" y="2" width="416" height="186" rx="14" fill="url(#wash)"/>
<text x="24" y="31" fill="{p['gold']}" font-size="12">{escape(category)}</text>
<path d="M379 31l12-12m-11 0h11v11" fill="none" stroke="{p['gold']}" stroke-width="1.7"/>
<g transform="translate(346 91)" fill="none" stroke="{p['blue']}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" opacity=".45">{artwork}</g>
<text x="24" y="68" fill="{p['ink']}" font-size="{title_size}" font-weight="600">{escape(title)}</text>
<text x="24" y="104" fill="{p['muted']}" font-size="15">{escape(description[0])}</text>
<text x="24" y="128" fill="{p['muted']}" font-size="15">{escape(description[1])}</text>
{''.join(pills)}
''')


def button(p, label, primary=False):
    bg, ink = (p["gold"], p["bg"]) if primary else (p["card"], p["ink"])
    line = p["gold"] if primary else p["line"]
    return document(116, 36, label, f'''<rect x=".7" y=".7" width="114.6" height="34.6" rx="8" fill="{bg}" stroke="{line}"/>
<text x="16" y="23" fill="{ink}" font-size="13" font-weight="600">{escape(label)}</text>
<path d="M94 22l7-7m-7 0h7v7" fill="none" stroke="{ink}" stroke-width="1.4" stroke-linecap="round"/>''')


ICONS = {
    "code": '<path d="m18 12-12 16 12 16m20-32 12 16-12 16m-7-39-7 46"/>',
    "data": '<ellipse cx="28" cy="10" rx="21" ry="7"/><path d="M7 10v35c0 11 42 11 42 0V10m-42 17c0 11 42 11 42 0"/>',
    "cloud": '<path d="M12 43h31c17 0 17-23 2-24-2-20-31-20-35-2-17-3-19 25 2 26Z"/>',
    "network": '<circle cx="28" cy="28" r="6"/><circle cx="8" cy="8" r="4"/><circle cx="48" cy="8" r="4"/><circle cx="8" cy="48" r="4"/><circle cx="48" cy="48" r="4"/><path d="m11 11 13 13m8 0 13-13M11 45l13-13m8 0 13 13"/>',
    "activity": '<path d="M3 29h11l7-19 13 37 7-18h12"/>',
}
SECTIONS = [
    ("about", "01", "About me", "code"),
    ("projects", "02", "Projects", "network"),
    ("toolkit", "03", "Tools I use", "cloud"),
    ("activity", "04", "On GitHub", "activity"),
]
TOOLKIT = [
    ("languages", "Languages", ("Java · Python · SQL", "JavaScript · Bash"), "code"),
    ("backend", "Backend & data", ("REST APIs · JDBC · MySQL", "Auth · Caching · MongoDB"), "data"),
    ("cloud", "Cloud & delivery", ("Docker · Kubernetes · Helm", "OpenShift · Prometheus · CI/CD"), "cloud"),
    ("ml", "Applied ML", ("Pandas · Scikit-learn", "Forecasting · Differential privacy"), "network"),
]


def section(p, entry):
    slug, number, title, icon = entry
    return document(840, 68, title, f'''
<style>@media (max-width:600px) {{ .section-heading {{ font-size:40px; }} }}</style>
<defs><linearGradient id="glow"><stop stop-color="{p['gold']}" stop-opacity=".08"/><stop offset="1" stop-color="{p['gold']}" stop-opacity="0"/></linearGradient>
<pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="{p['muted']}" opacity=".16"/></pattern></defs>
<rect x="1" y="1" width="838" height="66" rx="14" fill="{p['bg']}" stroke="{p['line']}"/>
<rect x="2" y="2" width="836" height="64" rx="13" fill="url(#glow)"/>
<rect x="610" y="2" width="228" height="64" rx="14" fill="url(#dots)"/>
<path d="M25 2h90" stroke="{p['gold']}" stroke-width="2"/>
<text class="section-heading" x="24" y="44" fill="{p['ink']}" font-size="23" font-weight="600">{title}</text>
<path d="M607 34h65m55 0h70" stroke="{p['gold']}" stroke-opacity=".3"/>
<circle cx="700" cy="34" r="25" fill="{p['bg']}" stroke="{p['line']}"/>
<g transform="translate(686 20) scale(.5)" fill="none" stroke="{p['blue']}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>
<circle cx="608" cy="34" r="3" fill="{p['gold']}"/>
<circle cx="797" cy="34" r="3" fill="{p['blue']}"/>
''')


def toolkit(p, entry):
    slug, title, lines, icon = entry
    return document(420, 152, title + ": " + ". ".join(lines), f'''
<defs><linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{p['gold']}" stop-opacity=".07"/><stop offset="1" stop-color="{p['gold']}" stop-opacity="0"/></linearGradient></defs>
<rect x="1" y="1" width="418" height="150" rx="14" fill="{p['card']}" stroke="{p['line']}"/>
<rect x="2" y="2" width="416" height="148" rx="13" fill="url(#wash)"/>
<text x="24" y="40" fill="{p['ink']}" font-size="18" font-weight="600">{escape(title)}</text>
<g transform="translate(351 17) scale(.65)" fill="none" stroke="{p['blue']}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>
<path d="M24 62h40" stroke="{p['gold']}" stroke-width="2"/>
<text x="24" y="92" fill="{p['muted']}" font-size="15">{escape(lines[0])}</text>
<text x="24" y="120" fill="{p['muted']}" font-size="15">{escape(lines[1])}</text>
''')


def current_role(p):
    return document(420, 190, "Current role: Software Engineer at Airbnb, contracted via Altimetrik. Payments risk and alerting. August 2026 to present.", f'''
<defs><radialGradient id="halo"><stop stop-color="{p['gold']}" stop-opacity=".1"/><stop offset="1" stop-color="{p['gold']}" stop-opacity="0"/></radialGradient></defs>
<rect x="1" y="1" width="418" height="188" rx="14" fill="{p['card']}" stroke="{p['line']}"/>
<ellipse cx="338" cy="62" rx="140" ry="105" fill="url(#halo)"/>
<circle cx="30" cy="28" r="4" fill="{p['gold']}"/>
<text x="43" y="32" fill="{p['gold']}" font-size="12">Current role</text>
<text x="24" y="68" fill="{p['ink']}" font-size="22" font-weight="600">Airbnb</text>
<text x="24" y="96" fill="{p['muted']}" font-size="15">Contracted via Altimetrik</text>
<text x="24" y="127" fill="{p['ink']}" font-size="16">Payments risk &amp; alerting</text>
<text x="24" y="151" fill="{p['muted']}" font-size="15">APIs, logs, and monitoring</text>
<text x="24" y="174" fill="{p['gold']}" font-size="13">Aug 2026 — Present</text>
<g transform="translate(346 48) scale(.72)" fill="none" stroke="{p['blue']}" stroke-width="2.1" stroke-linecap="round">{ICONS['activity']}</g>
''')


def background(p):
    rows = [("Oracle", "Cloud & DevOps", 103), ("IIT Ropar", "Full stack & AI", 133), ("NIT Patna", "B.Tech · Computer Science", 163)]
    content = []
    for company, detail, y in rows:
        content.append(f'<circle cx="29" cy="{y-5}" r="3" fill="{p["gold"]}"/><text x="43" y="{y}" fill="{p["ink"]}" font-size="16" font-weight="600">{company}</text><text x="152" y="{y}" fill="{p["muted"]}" font-size="14">{escape(detail)}</text>')
    return document(420, 190, "Background: Oracle cloud infrastructure and DevOps internship; IIT Ropar software development internship; B.Tech in Computer Science and Engineering at NIT Patna.", f'''
<rect x="1" y="1" width="418" height="188" rx="14" fill="{p['card']}" stroke="{p['line']}"/>
<text x="24" y="32" fill="{p['gold']}" font-size="12">Background</text>
<text x="24" y="68" fill="{p['ink']}" font-size="20" font-weight="600">Before Airbnb</text>
<path d="M29 99v59" stroke="{p['gold']}" stroke-opacity=".3"/>
{''.join(content)}
''')


def contact(p):
    return document(840, 138, "Have a question about my work? You can reach me by email.", f'''
<style>@media (max-width:600px) {{ .contact-heading {{ font-size:34px; }} .contact-detail {{ font-size:25px; }} }}</style>
<defs><radialGradient id="glow"><stop stop-color="{p['gold']}" stop-opacity=".14"/><stop offset="1" stop-color="{p['gold']}" stop-opacity="0"/></radialGradient></defs>
<rect x="1" y="1" width="838" height="136" rx="16" fill="{p['bg']}" stroke="{p['line']}"/>
<ellipse cx="720" cy="70" rx="175" ry="100" fill="url(#glow)"/>
<text class="contact-heading" x="28" y="62" fill="{p['ink']}" font-size="24" font-weight="600">Have a question about my work?</text>
<text class="contact-detail" x="28" y="101" fill="{p['muted']}" font-size="16">You can reach me by email.</text>
<circle cx="739" cy="70" r="47" fill="none" stroke="{p['gold']}" stroke-opacity=".25"/>
<g transform="translate(688 32) scale(1.1)">{MONOGRAM.format(gold=p['gold'])}</g>
<path d="M618 70h74m94 0h30" stroke="{p['gold']}" stroke-opacity=".3"/>
<circle cx="618" cy="70" r="3" fill="{p['blue']}"/>
''')


for theme, palette in PALETTES.items():
    (ASSETS / f"banner-{theme}.svg").write_text(banner(palette), encoding="utf-8")
    for item in PROJECTS:
        (ASSETS / f"project-{item[0]}-{theme}.svg").write_text(project(palette, item), encoding="utf-8")
    for label in ("Portfolio", "Resume", "LinkedIn", "Email"):
        (ASSETS / f"link-{label.lower()}-{theme}.svg").write_text(button(palette, label, label == "Portfolio"), encoding="utf-8")
    for entry in SECTIONS:
        (ASSETS / f"section-{entry[0]}-{theme}.svg").write_text(section(palette, entry), encoding="utf-8")
    for entry in TOOLKIT:
        (ASSETS / f"toolkit-{entry[0]}-{theme}.svg").write_text(toolkit(palette, entry), encoding="utf-8")
    (ASSETS / f"about-current-{theme}.svg").write_text(current_role(palette), encoding="utf-8")
    (ASSETS / f"about-background-{theme}.svg").write_text(background(palette), encoding="utf-8")
    (ASSETS / f"contact-{theme}.svg").write_text(contact(palette), encoding="utf-8")

print("Generated 40 SVG assets for light and dark profiles.")

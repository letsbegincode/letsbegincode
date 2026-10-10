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
<g font-family="Arial, Helvetica, sans-serif">{body}</g>
</svg>\n'''


def banner(p):
    return document(1000, 340, "Abhinav Ranjan Sulabh — Software Engineer", f'''
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
<rect x="1" y="1" width="998" height="338" rx="22" fill="{p['bg']}" stroke="{p['line']}"/>
<rect x="560" y="2" width="438" height="336" rx="22" fill="url(#grid)"/>
<ellipse cx="785" cy="176" rx="290" ry="205" fill="url(#glow)"/>
<path d="M40 1h220" stroke="url(#edge)" stroke-width="3"/>
<text x="48" y="62" fill="{p['gold']}" font-size="17" letter-spacing="4">SOFTWARE ENGINEER</text>
<text x="44" y="150" fill="{p['ink']}" font-size="64" font-weight="700" letter-spacing="-2">Abhinav Ranjan</text>
<text x="44" y="224" fill="{p['gold']}" font-size="72" font-weight="700" letter-spacing="-2">Sulabh.</text>
<path d="M48 268h70" stroke="{p['gold']}" stroke-width="3"/>
<text x="135" y="274" fill="{p['muted']}" font-size="19">Systems. Cloud. Applied intelligence.</text>
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
''')


PROJECTS = [
    ("banking", "01", "BACKEND SYSTEMS", "Core Banking Engine", ("Banking APIs, transactions,", "persistence, and TTL caching."), ("Java", "JDBC", "MySQL"), "bank"),
    ("dns", "02", "NETWORKING", "DNS Resolution Engine", ("Hierarchical resolution,", "caching, and DNSSEC concepts."), ("Java", "DNS", "Caching"), "network"),
    ("forecasting", "03", "APPLIED MACHINE LEARNING", "Power Price Forecasting", ("From public data ingestion", "to validated price forecasts."), ("Python", "Pandas", "Scikit-learn"), "chart"),
    ("federated", "04", "PRIVACY & SECURITY", "Federated Intrusion Detection", ("Collaborative model training", "with differential privacy."), ("Python", "Federated ML", "Privacy"), "shield"),
]


def project(p, entry):
    slug, number, category, title, description, tags, icon = entry
    artwork = {
        "bank": '<path d="m5 16 23-12 23 12M10 19h36M13 22v22m15-22v22m15-22v22M7 48h42"/>',
        "network": '<circle cx="28" cy="28" r="6"/><circle cx="8" cy="8" r="4"/><circle cx="48" cy="8" r="4"/><circle cx="8" cy="48" r="4"/><circle cx="48" cy="48" r="4"/><path d="m11 11 13 13m8 0 13-13M11 45l13-13m8 0 13 13"/>',
        "chart": '<path d="M5 5v44h46M10 39l10-13 10 6 17-23m-9 0h9v9"/>',
        "shield": '<path d="m28 3 21 8v17c0 14-21 24-21 24S7 42 7 28V11Z"/><path d="m17 27 8 8 14-17"/>',
    }[icon]
    title_size = 23 if len(title) > 25 else 26
    pills = []
    x = 24
    for tag in tags:
        width = len(tag) * 7.3 + 22
        pills.append(f'<rect x="{x}" y="168" width="{width}" height="25" rx="6" fill="{p["bg"]}" stroke="{p["line"]}"/><text x="{x+11}" y="185" fill="{p["muted"]}" font-size="13">{escape(tag)}</text>')
        x += width + 8
    return document(420, 214, title + ". " + " ".join(description), f'''
<defs><linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{p['gold']}" stop-opacity=".08"/><stop offset="1" stop-color="{p['gold']}" stop-opacity="0"/></linearGradient></defs>
<rect x="1" y="1" width="418" height="212" rx="14" fill="{p['card']}" stroke="{p['line']}"/>
<rect x="2" y="2" width="416" height="210" rx="14" fill="url(#wash)"/>
<text x="24" y="31" fill="{p['gold']}" font-size="11" font-weight="700" letter-spacing="1.2">{number} / {escape(category)}</text>
<path d="M379 31l12-12m-11 0h11v11" fill="none" stroke="{p['gold']}" stroke-width="1.7"/>
<g transform="translate(346 102)" fill="none" stroke="{p['blue']}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" opacity=".45">{artwork}</g>
<text x="24" y="77" fill="{p['ink']}" font-size="{title_size}" font-weight="700" letter-spacing="-.7">{escape(title)}</text>
<text x="24" y="113" fill="{p['muted']}" font-size="18">{escape(description[0])}</text>
<text x="24" y="138" fill="{p['muted']}" font-size="18">{escape(description[1])}</text>
{''.join(pills)}
''')


def button(p, label, primary=False):
    bg, ink = (p["gold"], p["bg"]) if primary else (p["card"], p["ink"])
    line = p["gold"] if primary else p["line"]
    return document(116, 36, label, f'''<rect x=".7" y=".7" width="114.6" height="34.6" rx="8" fill="{bg}" stroke="{line}"/>
<text x="16" y="23" fill="{ink}" font-size="14" font-weight="700">{escape(label)}</text>
<path d="M94 22l7-7m-7 0h7v7" fill="none" stroke="{ink}" stroke-width="1.4" stroke-linecap="round"/>''')


for theme, palette in PALETTES.items():
    (ASSETS / f"banner-{theme}.svg").write_text(banner(palette), encoding="utf-8")
    for item in PROJECTS:
        (ASSETS / f"project-{item[0]}-{theme}.svg").write_text(project(palette, item), encoding="utf-8")
    for label in ("Portfolio", "Resume", "LinkedIn", "Email"):
        (ASSETS / f"link-{label.lower()}-{theme}.svg").write_text(button(palette, label, label == "Portfolio"), encoding="utf-8")

print("Generated 18 SVG assets for light and dark profiles.")

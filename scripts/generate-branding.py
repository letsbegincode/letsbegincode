"""Generate the ARS monogram and compact profile link buttons."""

from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
ASSETS.mkdir(exist_ok=True)
PALETTES = {"dark": "#dfbd78", "light": "#8a651f"}
BUTTONS = {"portfolio": "Portfolio", "resume": "Resume", "linkedin": "LinkedIn",
           "email": "Email", "kaggle": "Kaggle", "x": "X / Twitter"}

for theme, gold in PALETTES.items():
    artwork = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 104 68" role="img" aria-labelledby="title">
<title id="title">ARS — Abhinav Ranjan Sulabh</title>
<g fill="none" stroke="{gold}" stroke-width="4" stroke-linecap="square" stroke-linejoin="bevel" transform="translate(6 2) skewX(-6)">
<path d="M8 50 22 14 36 50M13 38h18"/>
<path d="M42 50V14h15l8 8v8l-8 8H42m13 0 12 12"/>
<path d="m89 18-4-4h-8l-8 8v5l18 9v8l-7 6h-8l-4-4"/>
</g>
</svg>
'''
    (ASSETS / f"ars-logo-{theme}.svg").write_text(artwork, encoding="utf-8")
    background, ink, border = (("#171b20", "#e6edf3", "#3d444d") if theme == "dark"
                               else ("#f6f8fa", "#1f2328", "#d1d9e0"))
    for slug, label in BUTTONS.items():
        primary = slug == "portfolio"
        fill = gold if primary else background
        text = ("#0d1117" if theme == "dark" else "#ffffff") if primary else ink
        stroke = gold if primary else border
        button = f'''<svg xmlns="http://www.w3.org/2000/svg" width="94" height="32" viewBox="0 0 94 32" role="img" aria-labelledby="title">
<title id="title">{escape(label)}</title>
<rect x=".5" y=".5" width="93" height="31" rx="6" fill="{fill}" stroke="{stroke}"/>
<text x="47" y="20.5" text-anchor="middle" font-family="'Mona Sans VF', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="12" font-weight="600" fill="{text}">{escape(label)}</text>
</svg>
'''
        (ASSETS / f"link-{slug}-{theme}.svg").write_text(button, encoding="utf-8")

print("Generated the ARS monogram and six link buttons for both themes.")

"""Write samples/index.html (a page linking every sample) and an artifact copy of it."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from variants import VARIANTS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS = """
:root{--bg:#F7F7F5;--surface:#FFFFFF;--fg:#191A19;--muted:#6E716E;--line:#E2E3E0;--accent:#191A19}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#121312;--surface:#1B1C1B;--fg:#ECECE8;--muted:#9A9D99;--line:#2C2D2C;--accent:#ECECE8;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#121312;--surface:#1B1C1B;--fg:#ECECE8;--muted:#9A9D99;--line:#2C2D2C;--accent:#ECECE8;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 "Manrope",system-ui,sans-serif}
.wrap{max-width:1240px;margin:0 auto;padding-left:max(16px, env(safe-area-inset-left, 0px));padding-right:max(16px, env(safe-area-inset-right, 0px));padding-block:48px 80px}
h1{font-weight:300;font-size:clamp(2.2rem,5vw,3.6rem);letter-spacing:-.03em;line-height:1.05;margin:8px 0 0;text-wrap:balance}
.k{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.lede{color:var(--muted);max-width:44em;margin-top:16px}
.notes{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:28px;font-size:.92rem;color:var(--muted)}
.notes b{display:block;color:var(--fg);font-weight:600;margin-bottom:2px}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:28px;margin-top:44px}
.card{background:var(--surface);border:1px solid var(--line);text-decoration:none;color:inherit;display:flex;flex-direction:column;min-width:0}
.card img{width:100%;aspect-ratio:16/10;object-fit:cover;object-position:top;display:block;border-bottom:1px solid var(--line)}
.card .b{padding:16px 18px 18px;display:grid;gap:4px}
.card h2{margin:0;font-weight:400;font-size:1.4rem;display:flex;justify-content:space-between;gap:10px;align-items:baseline}
.card h2 span{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.card p{margin:0;color:var(--muted);font-size:.93rem}
.pages{display:flex;gap:14px;flex-wrap:wrap;margin-top:6px;font-size:.88rem}
.pages a{color:var(--fg)}
.card:hover{border-color:var(--muted)}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
@media (max-width:760px){.grid,.notes{grid-template-columns:1fr}}
"""


def cards(prefix):
    out = []
    for i, v in enumerate(VARIANTS, 1):
        third = ("bio.html", "Bio") if v["structure"] == "bio" else ("contact.html", "Contact")
        base = f"{prefix}{v['slug']}/"
        struct = "Home · Menus · Bio + contact form on every page" if v["structure"] == "bio" else "Home with bio · Menus · Contact page"
        out.append(f'''<article class="card"><a href="{base}index.html"><img src="{prefix}../assets/shots/{v["slug"]}.jpg" alt="Home page of sample {i}, {v["name"]}" loading="lazy"></a>
<div class="b"><h2>{i:02d} · {v["name"]}<span>{struct}</span></h2><p>{v["blurb"]}</p>
<div class="pages"><a href="{base}index.html">Home</a><a href="{base}menus.html">Menus</a><a href="{base}{third[0]}">{third[1]}</a></div></div></article>''')
    return "".join(out)


def body(prefix):
    return f'''<main class="wrap">
<p class="k">chefcodycunningham.com · Round two</p>
<h1>Eight directions, all photo-first</h1>
<p class="lede">Each sample is a working three-page site: Home, Menus, and either a Bio page or a Contact page. The copy and menus are the same in all eight, taken from your 2026–27 winter menus and past proposals, with no prices. Open them on your phone too.</p>
<div class="notes">
<div><b>Two structures</b>Samples 1, 3, 5 and 7 have a Bio page, with a small contact form at the foot of every page. Samples 2, 4, 6 and 8 put your bio on the home page and add a Contact page.</div>
<div><b>Photos</b>These use the photos from your current site and your menu PDFs. Your "Photos a la food" favorites will replace them.</div>
<div><b>Mix and match</b>Any look works with either structure, and any menu layout (list, tabs, photo rows or fold-open) can go with any look.</div>
</div>
<div class="grid">{cards(prefix)}</div>
</main>'''


FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600&display=swap">'

with open(os.path.join(ROOT, "samples", "index.html"), "w") as f:
    f.write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>Website Samples · Cody Cunningham</title>{FONTS}<style>{CSS}</style></head><body>{body("")}</body></html>')

art = sys.argv[1] if len(sys.argv) > 1 else None
if art:
    with open(art, "w") as f:
        f.write(f'<title>Chef Cody Website Samples</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}<style>{CSS}</style>{body("samples/")}')
print("ok")

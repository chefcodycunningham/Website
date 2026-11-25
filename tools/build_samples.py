"""Generate the sample site designs into samples/<slug>/{index,menus,bio}.html.

Every sample shares the copy in content.py. Each design picks a hero layout, a menu layout,
a bio layout and its own stylesheet. Contact is a small block at the foot of every page.
Run: python3 tools/build_samples.py
"""
import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *  # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = "../../assets/img/"
e = html.escape


def img(key, cls="", pos=None, eager=False):
    style = f' style="object-position:{pos}"' if pos else ""
    load = "" if eager else ' loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="{IMG}{P[key]}" alt="{e(ALT[key])}"{style}{load}>'


# ---------- shared blocks ----------
def nav(v, page):
    if v["structure"] == "bio":
        links = [("index.html", "Home"), ("menus.html", "Menus"), ("bio.html", "Bio")]
        extra = '<a href="#contact" class="nav-contact">Contact</a>'
    else:
        links = [("index.html", "Home"), ("menus.html", "Menus"), ("contact.html", "Contact")]
        extra = ""
    cur = ' aria-current="page"'
    items = "".join(f'<a href="{h}"{cur if h.startswith(page) else ""}>{t}</a>' for h, t in links)
    return (f'<header class="nav"><div class="in"><a class="mark" href="index.html">{v["mark"]}</a>'
            f'<nav aria-label="Main">{items}{extra}</nav></div></header>')


FOOT = f'<footer class="foot"><div class="in"><span>Cody Cunningham · Private Chef · Avon, Colorado</span><span>{PHONE}</span></div></footer>'


def contact_band(v):
    return f'''<section class="contact band" id="contact"><div class="in">
  <h2>{e(CLOSING)}</h2><p class="c-direct"><a class="soft" href="contact.html">Get in touch</a><span>{PHONE} · call or text</span></p>
</div></section>''' + FOOT


def contact_page(v):
    return f'''<section class="contact-page"><div class="in">
  <figure class="cp-pic">{img(v["contact_pic"], "", None, True)}</figure>
  <div class="cp-body"><p class="kicker">Contact</p><h1>Let's plan something.</h1>
  <p>Tell me a little about what you have in mind: the date, how many of you, where you're staying, and anything you love or can't eat. I'll reply within a day.</p>
  <p class="c-direct"><span>{PHONE}</span><span>Call or text</span><a href="{INSTAGRAM}">@chefcodycunningham</a></p>
  {form(v)}</div></div></section>'''


def form(v):
    return f'''<form class="c-form" novalidate data-form>
    <label><span>Name</span><input id="c-name-{v['slug']}" name="name" autocomplete="name"></label>
    <label><span>Email or phone</span><input id="c-reach-{v['slug']}" name="reach"></label>
    <label><span>Date</span><input id="c-date-{v['slug']}" name="date" type="date"></label>
    <label><span>Guests</span><input id="c-guests-{v['slug']}" name="guests" type="number" min="1" inputmode="numeric"></label>
    <label class="wide"><span>The occasion, where you're staying, anything I should know</span><textarea id="c-note-{v['slug']}" name="note" rows="3"></textarea></label>
    <div class="wide c-send"><button type="submit">Send</button><p class="c-done" hidden>Thank you. I'll be in touch within a day. (Sample form, nothing was sent.)</p></div>
  </form>'''


def contact(v):
    if v["structure"] != "bio":
        return contact_band(v)
    return f'''<section class="contact" id="contact"><div class="in">
  <div class="c-intro">
    <p class="kicker">Contact</p>
    <h2>{e(CLOSING)}</h2>
    <p class="c-direct"><span>{PHONE}</span><span>Call or text</span></p>
    <p class="c-direct"><a href="{INSTAGRAM}">@chefcodycunningham</a></p>
  </div>
  {form(v)}
</div></section>''' + FOOT


def offer_list():
    items = ["Dinner parties", "Family-style feasts", "Ski-week stays", "Cocktail hours", "Cooking classes"]
    return "<ul class=\"offer\">" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# ---------- home heroes ----------
def hero_full(v):
    return f'''<section class="hero hero-full">{img(v["hero"], "hero-img", v.get("hero_pos"), True)}
<div class="hero-copy in"><h1>{OPENING}</h1><p>{OFFER}</p></div></section>'''


def hero_split(v):
    return f'''<section class="hero hero-split"><div class="hero-copy"><h1>{OPENING}</h1><p>{OFFER}</p>
<a class="soft" href="#contact">Plan a dinner</a></div>
<div class="hero-pic">{img(v["hero"], "", v.get("hero_pos"), True)}</div></section>'''


def hero_type(v):
    return f'''<section class="hero hero-type"><div class="in"><h1>{OPENING}</h1><p>{OFFER}</p></div></section>
<figure class="bleed">{img(v["hero"], "", v.get("hero_pos"), True)}</figure>'''


def hero_mosaic(v):
    a, b, c = v["mosaic"]
    return f'''<section class="hero hero-mosaic"><div class="in">
<div class="hero-copy"><h1>{OPENING}</h1><p>{OFFER}</p></div>
<div class="mos">{img(a, "m1", None, True)}{img(b, "m2", None, True)}{img(c, "m3", None, True)}</div></div></section>'''


def hero_strip(v):
    pics = "".join(f"<figure>{img(k, '', None, i < 3)}</figure>" for i, k in enumerate(v["strip"]))
    return f'''<section class="hero hero-strip"><div class="in hero-copy"><h1>{OPENING}</h1><p>{OFFER}</p></div>
<div class="strip" tabindex="0" aria-label="Dishes, scroll sideways">{pics}</div></section>'''


HEROES = dict(full=hero_full, split=hero_split, type=hero_type, mosaic=hero_mosaic, strip=hero_strip)


def home_body(v):
    gal = "".join(f'<figure class="g{i}">{img(k)}</figure>' for i, k in enumerate(v["gallery"]))
    if v["structure"] != "bio":
        paras = "".join(f"<p>{e(p)}</p>" for p in BIO[1:])
        places = "".join(f"<li>{p}</li>" for p in PLACES)
        intro = f'''<section class="intro full-bio"><div class="in">
  <div class="intro-pic">{img("portrait", "", "center 20%")}</div>
  <div class="intro-copy"><p class="kicker">Hello, I'm Cody</p><p class="lead">{e(BIO[0])}</p>{paras}
  <ol class="places" aria-label="Where I've cooked">{places}</ol></div></div></section>'''
        return HEROES[v["hero_kind"]](v) + intro + f'<section class="gallery"><div class="in grid">{gal}</div></section>' + f'''<section class="offers"><div class="in"><p class="kicker">What I cook</p>{offer_list()}
  <a class="soft" href="menus.html">See sample menus</a></div></section>'''
    intro = f'''<section class="intro"><div class="in">
  <div class="intro-pic">{img("portrait", "", "center 20%")}</div>
  <div class="intro-copy"><p class="kicker">Hello, I'm Cody</p><p class="lead">{e(BIO[0])}</p>
  <p>{e(BIO[2])}</p><a class="soft" href="bio.html">Read my story</a></div></div></section>'''
    offers = f'''<section class="offers"><div class="in"><p class="kicker">What I cook</p>{offer_list()}
  <a class="soft" href="menus.html">See sample menus</a></div></section>'''
    return HEROES[v["hero_kind"]](v) + offers + f'<section class="gallery"><div class="in grid">{gal}</div></section>' + intro


# ---------- menus ----------
def menu_card(name, line, items):
    li = "".join(f"<li>{e(i)}</li>" for i in items)
    sub = f'<p class="m-line">{e(line)}</p>' if line else ""
    return f'<article class="menu"><h3>{e(name)}</h3>{sub}<ul>{li}</ul></article>'


def menus_list(v):
    out = []
    pics = v["menu_pics"]
    for i, (sec, note, ms) in enumerate(MENUS):
        cards = "".join(menu_card(*m) for m in ms)
        out.append(f'''<section class="m-sec"><div class="in"><header class="m-head"><h2>{sec}</h2><p>{note}</p></header>
<div class="m-cards">{cards}</div></div></section>''')
        if i < len(pics):
            out.append(f'<figure class="bleed m-pic">{img(pics[i])}</figure>')
    return "".join(out)


def menus_tabs(v):
    tabs = "".join(f'<button role="tab" id="t{i}" aria-controls="s{i}" aria-selected="{str(i==0).lower()}">{sec}</button>'
                   for i, (sec, _, _) in enumerate(MENUS))
    panels = []
    for i, (sec, note, ms) in enumerate(MENUS):
        cards = "".join(menu_card(*m) for m in ms)
        pic = img(v["menu_pics"][i % len(v["menu_pics"])])
        panels.append(f'''<div class="m-panel" role="tabpanel" id="s{i}" aria-labelledby="t{i}"{"" if i == 0 else " hidden"}>
<figure class="m-pic">{pic}</figure><div><p class="m-note">{note}</p><div class="m-cards">{cards}</div></div></div>''')
    return f'<section class="m-tabs"><div class="in"><div class="tabs" role="tablist" aria-label="Menu types">{tabs}</div>{"".join(panels)}</div></section>'


def menus_rows(v):
    out = []
    pics = v["menu_pics"]
    n = 0
    for sec, note, ms in MENUS:
        out.append(f'<div class="in"><header class="m-head"><h2>{sec}</h2><p>{note}</p></header></div>')
        for m in ms:
            pic = img(pics[n % len(pics)])
            out.append(f'<section class="m-row{" flip" if n % 2 else ""}"><div class="in"><figure>{pic}</figure>{menu_card(*m)}</div></section>')
            n += 1
    return "".join(out)


def menus_accordion(v):
    out = []
    for i, (sec, note, ms) in enumerate(MENUS):
        body = "".join(menu_card(*m) for m in ms)
        out.append(f'''<details class="m-acc"{" open" if i == 0 else ""}><summary><span>{sec}</span><small>{note}</small></summary>
<div class="m-acc-body"><figure class="m-pic">{img(v["menu_pics"][i % len(v["menu_pics"])])}</figure><div class="m-cards">{body}</div></div></details>''')
    return f'<section class="m-accs"><div class="in">{"".join(out)}</div></section>'


MENU_KINDS = dict(list=menus_list, tabs=menus_tabs, rows=menus_rows, accordion=menus_accordion)


def menus_body(v):
    head = f'''<section class="page-head"><div class="in"><p class="kicker">Sample menus</p><h1>Menus</h1><p>{e(MENU_INTRO)}</p></div></section>'''
    foot = f'<section class="m-extra"><div class="in"><p>{e(EXTRAS)}</p></div></section>'
    return head + MENU_KINDS[v["menu_kind"]](v) + foot


# ---------- bio ----------
def bio_body(v):
    paras = "".join(f"<p>{e(p)}</p>" for p in BIO)
    places = "".join(f"<li>{p}</li>" for p in PLACES)
    pics = v["bio_pics"]
    return f'''<section class="bio"><div class="in">
  <figure class="bio-portrait">{img("portrait", "", "center 15%", True)}</figure>
  <div class="bio-copy"><p class="kicker">Bio</p><h1>Cody Cunningham</h1>{paras}
    <ol class="places" aria-label="Where I've cooked">{places}</ol></div>
</div></section>
<section class="bio-pics"><div class="in">{"".join(f"<figure>{img(k)}</figure>" for k in pics)}</div></section>
<section class="quote"><div class="in"><blockquote>“What you feel like eating at any given moment is what you should have.”<cite>Ferran Adrià</cite></blockquote></div></section>'''


# ---------- page ----------
BASE_CSS = """
*{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--body);font-size:17px;line-height:1.65}
img{display:block;max-width:100%;width:100%;height:100%;object-fit:cover}
figure{margin:0;overflow:hidden}
a{color:inherit}
h1,h2,h3{margin:0;font-weight:inherit;text-wrap:balance}
p{margin:0}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important;scroll-behavior:auto!important}}
.in{max-width:var(--max,1240px);margin:0 auto;padding-left:max(var(--gut,24px), env(safe-area-inset-left, 0px));padding-right:max(var(--gut,24px), env(safe-area-inset-right, 0px))}
.nav .in{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;padding-block:22px}
.nav nav{display:flex;gap:clamp(14px,2.5vw,32px)}
.nav a{text-decoration:none}
.kicker{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase}
.soft{display:inline-block;margin-top:20px;text-decoration:none;border-bottom:1px solid currentColor;padding-bottom:2px}
.offer{list-style:none;margin:0;padding:0}
.menu ul{list-style:none;margin:0;padding:0}
.strip{display:flex;gap:var(--sgap,8px);overflow-x:auto;scroll-snap-type:x mandatory;padding-left:max(var(--gut,24px), env(safe-area-inset-left, 0px))}
.strip figure{flex:0 0 auto;scroll-snap-align:start}
.c-form{display:grid;grid-template-columns:1fr 1fr;gap:14px 18px}
.c-form label{display:grid;gap:4px;min-width:0}
.c-form .wide{grid-column:1/-1}
.c-form input,.c-form textarea{font:inherit;color:inherit;width:100%;min-width:0}
.c-form textarea{resize:vertical}
.c-form button{font:inherit;cursor:pointer}
.c-send{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.c-direct{display:flex;gap:10px;flex-wrap:wrap}
.places{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap}
.samplebar{font:12px/1.4 system-ui,sans-serif;background:#111;color:#ddd;text-align:center;padding:7px max(16px, env(safe-area-inset-left, 0px))}
.samplebar a{color:#fff}
@media (max-width:640px){.c-form{grid-template-columns:1fr}}
"""

SCRIPT = """<script>
document.querySelectorAll('[data-form]').forEach(f=>f.addEventListener('submit',ev=>{ev.preventDefault();f.querySelector('.c-done').hidden=false;}));
const tabs=[...document.querySelectorAll('[role=tab]')];
tabs.forEach(t=>t.addEventListener('click',()=>tabs.forEach(x=>{const on=x===t;x.setAttribute('aria-selected',on);document.getElementById(x.getAttribute('aria-controls')).hidden=!on;})));
</script>"""


def page(v, name, title, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="Cody Cunningham, private chef in the Vail Valley. Dinner parties, family-style feasts, ski-week stays, cocktail hours and cooking classes in your home.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{v["fonts"]}">
<style>{BASE_CSS}{v["css"]}</style>
</head>
<body class="p-{name}">
<div class="samplebar">Sample {v["num"]} of {len(VARIANTS)} · {v["name"]} · <a href="../index.html">All samples</a></div>
{nav(v, name)}
<main>{body}</main>
{FOOT if name == "contact" else contact(v)}
{SCRIPT}
</body>
</html>'''


def build(v):
    d = os.path.join(ROOT, "samples", v["slug"])
    os.makedirs(d, exist_ok=True)
    third = ("bio", "Bio · Cody Cunningham", bio_body) if v["structure"] == "bio" else \
            ("contact", "Contact · Cody Cunningham", lambda v: contact_page(v))
    for name, title, fn in [("index", "Cody Cunningham · Private Chef", home_body),
                            ("menus", "Menus · Cody Cunningham", menus_body), third]:
        with open(os.path.join(d, name + ".html"), "w") as f:
            f.write(page(v, name, title, fn(v)))


from variants import VARIANTS  # noqa: E402

if __name__ == "__main__":
    for i, v in enumerate(VARIANTS, 1):
        v["num"] = i
        build(v)
    print("built", len(VARIANTS))

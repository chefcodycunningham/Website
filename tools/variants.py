"""Eight Scandinavian-minimal sample designs. COMMON holds shared layout; each variant adds its own look."""

COMMON = """
.hero-full{position:relative;height:min(84vh,860px);min-height:460px;color:#fff}
.hero-full .hero-img{position:absolute;inset:0}
.hero-full::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.5),rgba(0,0,0,0) 55%)}
.hero-full .hero-copy{position:absolute;left:0;right:0;bottom:0;z-index:1;padding-bottom:clamp(28px,6vw,64px)}
.hero-split{display:grid;grid-template-columns:1fr 1.3fr;min-height:min(86vh,840px)}
.hero-split .hero-copy{display:flex;flex-direction:column;justify-content:flex-end;padding:clamp(32px,6vw,88px) max(24px, env(safe-area-inset-left, 0px))}
.hero-split .hero-pic{min-height:420px}
.hero-type .in{padding-block:clamp(56px,10vw,140px) clamp(32px,5vw,64px)}
.bleed{height:min(78vh,760px)}
.hero-mosaic .in{display:grid;grid-template-columns:1fr 1.5fr;gap:clamp(24px,4vw,64px);padding-block:clamp(24px,4vw,48px) clamp(40px,6vw,80px);align-items:end}
.mos{display:grid;grid-template-columns:1.4fr 1fr;grid-template-rows:1fr 1fr;gap:8px;height:clamp(400px,58vw,720px)}
.mos .m1{grid-row:span 2}
.hero-strip .hero-copy{padding-block:clamp(40px,7vw,100px) clamp(24px,4vw,48px)}
.strip figure{height:clamp(340px,52vw,600px);aspect-ratio:4/5}
.offers .in{padding-block:clamp(56px,8vw,112px)}
.offer{display:flex;flex-wrap:wrap;gap:6px 28px;margin-top:16px}
.gallery .grid{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:clamp(200px,28vw,400px);gap:var(--ggap,8px)}
.gallery .g0{grid-column:span 2}
.gallery .g3{grid-row:span 2}
.intro .in{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(28px,6vw,96px);align-items:center;padding-block:clamp(64px,9vw,128px)}
.intro-pic{aspect-ratio:4/5}
.intro-copy p+p{margin-top:16px}
.intro-copy .lead{margin-top:14px}
.intro-copy .places{margin-top:24px;gap:8px 20px}
.page-head .in{padding-block:clamp(48px,8vw,112px) clamp(32px,4vw,56px);max-width:var(--max,1240px)}
.page-head p:last-child{max-width:36em;margin-top:18px}
.m-sec .in{padding-block:clamp(48px,7vw,96px)}
.m-head{display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:clamp(24px,4vw,44px)}
.m-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:clamp(28px,4vw,48px) clamp(24px,3vw,40px)}
.menu h3{margin-bottom:4px}
.menu ul{margin-top:12px;display:grid;gap:6px}
.m-pic.bleed{height:min(70vh,640px)}
.m-tabs .in{padding-block:0 clamp(48px,7vw,96px)}
.tabs{display:flex;flex-wrap:wrap;gap:6px 22px;margin-bottom:clamp(28px,4vw,48px)}
.tabs button{font:inherit;background:none;border:0;padding:6px 0;cursor:pointer;color:inherit;opacity:.5;border-bottom:1px solid transparent}
.tabs button[aria-selected=true]{opacity:1;border-bottom-color:currentColor}
.m-panel{display:grid;grid-template-columns:1fr 1.6fr;gap:clamp(28px,5vw,72px);align-items:start}
.m-panel .m-pic{aspect-ratio:4/5;position:sticky;top:24px}
.m-panel .m-note{margin-bottom:24px}
.m-head+.m-row,.m-row{padding-block:clamp(20px,3vw,40px)}
.m-row .in{display:grid;grid-template-columns:1.2fr 1fr;gap:clamp(24px,5vw,80px);align-items:center}
.m-row figure{aspect-ratio:4/3}
.m-row.flip figure{order:2}
.m-row + .in .m-head{margin-top:clamp(48px,7vw,96px)}
.m-accs .in{padding-bottom:clamp(48px,7vw,96px)}
.m-acc{border-top:1px solid var(--line)}
.m-acc:last-child{border-bottom:1px solid var(--line)}
.m-acc summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding-block:22px;flex-wrap:wrap}
.m-acc summary::-webkit-details-marker{display:none}
.m-acc-body{display:grid;grid-template-columns:1fr 2fr;gap:clamp(24px,4vw,56px);padding-bottom:40px}
.m-acc-body .m-pic{aspect-ratio:4/5}
.m-extra .in{padding-block:0 clamp(48px,6vw,80px)}
.bio .in{display:grid;grid-template-columns:1fr 1.1fr;gap:clamp(28px,6vw,96px);padding-block:clamp(40px,7vw,96px)}
.bio-portrait{aspect-ratio:4/5;position:sticky;top:24px;align-self:start}
.bio-copy h1{margin:12px 0 24px}
.bio-copy p+p{margin-top:16px}
.bio-copy .places{margin-top:32px;gap:8px 22px}
.bio-pics .in{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--ggap,8px)}
.bio-pics figure{aspect-ratio:1}
.quote .in{padding-block:clamp(64px,9vw,128px);max-width:900px}
.quote blockquote{margin:0}
.quote cite{display:block;margin-top:18px;font-style:normal}
.contact .in{display:grid;grid-template-columns:1fr 1.4fr;gap:clamp(28px,5vw,80px);padding-block:clamp(48px,7vw,96px)}
.c-intro .c-direct{margin-top:14px}
.contact.band .in{display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap}
.contact.band .c-direct{align-items:baseline;gap:20px}
.contact.band .soft{margin-top:0}
.contact-page .in{display:grid;grid-template-columns:1fr 1fr;gap:clamp(28px,5vw,80px);padding-block:clamp(24px,4vw,56px) clamp(56px,8vw,112px)}
.cp-pic{min-height:420px}
.cp-body h1{margin:12px 0 20px}
.cp-body .c-direct{margin:20px 0 32px;gap:8px 20px}
.foot .in{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding-block:22px;font-size:.8rem}
@media (max-width:860px){
 .hero-split,.hero-mosaic .in,.intro .in,.m-panel,.m-row .in,.m-acc-body,.bio .in,.contact .in,.contact-page .in{grid-template-columns:1fr}
 .hero-split .hero-pic{order:-1;min-height:0;height:62vh}
 .hero-split{min-height:0}
 .m-row.flip figure{order:0}
 .m-panel .m-pic,.bio-portrait{position:static;aspect-ratio:4/3}
 .m-acc-body .m-pic{aspect-ratio:16/9}
 .mos{height:440px}
 .gallery .grid{grid-template-columns:1fr 1fr;grid-auto-rows:44vw}
 .gallery .g3{grid-row:auto}
 .bio-pics .in{grid-template-columns:1fr 1fr}
 .cp-pic{min-height:0;height:46vh}
}
"""


def font(*fams):
    return "https://fonts.googleapis.com/css2?" + "&".join("family=" + f for f in fams) + "&display=swap"


VARIANTS = [
    dict(slug="01-fjord", name="Fjord", mark="Cody Cunningham", structure="bio",
         blurb="Bright white, one full-bleed photo, quiet sans. Contact form at the foot of each page.",
         hero_kind="full", hero="steak-wine", hero_pos="center 60%", menu_kind="list",
         gallery=["tuna-tataki", "beet-salad", "duck-green", "scallops-coho-roe", "foie-torchon", "sea-bass", "king-crab-caviar"],
         menu_pics=["scallops-coho-roe", "charcuterie", "uni-gem-lettuce"],
         bio_pics=["beet-salad", "wagyu-tartare", "melon-gazpacho"],
         fonts=font("Manrope:wght@300;400;500;600"),
         css="""
:root{--bg:#FFFFFF;--fg:#1B1D1E;--muted:#72777A;--line:#E6E8E8;--accent:#1B1D1E;--body:"Manrope",system-ui,sans-serif;color-scheme:light}
.nav .in{padding-block:26px}.mark{font-weight:600;letter-spacing:.02em}.nav nav a{color:var(--muted);font-size:.92rem}.nav nav a[aria-current]{color:var(--fg)}
.kicker{color:var(--muted)}
.hero-full h1{font-size:clamp(2.6rem,6.5vw,5.6rem);font-weight:300;letter-spacing:-.03em;line-height:1}
.hero-full p{max-width:30em;margin-top:18px;font-size:1.05rem;opacity:.92}
.offer li{font-size:clamp(1.3rem,2.4vw,1.9rem);font-weight:300;letter-spacing:-.01em}
.intro .lead{font-size:1.35rem;font-weight:300;line-height:1.5}.intro-copy p{color:#3C4043}
.page-head h1,.bio-copy h1{font-size:clamp(2.6rem,6vw,4.8rem);font-weight:300;letter-spacing:-.03em;line-height:1}
.m-head h2{font-size:1.9rem;font-weight:300}.m-head p,.m-line{color:var(--muted)}
.menu h3{font-weight:600;font-size:1.05rem}.menu li{color:#3C4043;font-size:.97rem}
.quote blockquote{font-size:clamp(1.6rem,3.4vw,2.6rem);font-weight:300;letter-spacing:-.02em;line-height:1.25}.quote cite{color:var(--muted)}
.places li{color:var(--muted);font-size:.9rem}
.contact{background:#F5F6F6}.contact h2{font-size:1.9rem;font-weight:300;line-height:1.2;margin-top:10px}.c-direct{color:var(--muted)}
.c-form span{font-size:.78rem;color:var(--muted)}.c-form input,.c-form textarea{border:0;border-bottom:1px solid #CBD0D1;background:transparent;padding:8px 0;border-radius:0}
.c-form button{background:var(--fg);color:#fff;border:0;padding:13px 30px;border-radius:999px}
.foot{color:var(--muted)}
"""),
    dict(slug="02-linen", name="Linen", mark="CODY CUNNINGHAM", structure="contact",
         blurb="Warm oat tones and an airy split opening. Bio on the home page, with its own contact page.",
         hero_kind="split", hero="tuna-tataki", hero_pos="center 40%", menu_kind="rows", contact_pic="beet-salad",
         gallery=["scallops-coho-roe", "steak-wine", "melon-gazpacho", "duck-green", "crudite", "foie-torchon", "salmon-crudo"],
         menu_pics=["wagyu-ny-strip", "sea-bass", "duck-green", "king-crab-caviar", "steak-wine", "cacio-e-pepe-truffle", "salmon-crudo",
                    "stuffed-calamari", "melon-gazpacho", "uni-gem-lettuce", "beet-salad", "wagyu-onion-mousse", "caviar", "charcuterie",
                    "lobster", "watermelon-rice", "crudite", "cured-salmon"],
         fonts=font("Jost:wght@300;400;500"),
         css="""
:root{--bg:#EEEAE4;--fg:#2A2723;--muted:#7D766D;--line:#D8D1C7;--accent:#2A2723;--body:"Jost",system-ui,sans-serif;color-scheme:light}
.mark{letter-spacing:.34em;font-size:.82rem}.nav nav a{font-size:.8rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}.nav nav a[aria-current]{color:var(--fg)}
.kicker{color:var(--muted)}
.hero-split h1{font-size:clamp(2.4rem,4.6vw,4.2rem);font-weight:300;line-height:1.05;letter-spacing:-.01em}
.hero-split p{margin-top:20px;max-width:26em;color:#4E4840}
.offer{flex-direction:column;gap:2px}.offer li{font-size:clamp(1.5rem,3vw,2.3rem);font-weight:300;border-bottom:1px solid var(--line);padding-block:10px}
.intro .lead{font-size:1.3rem;line-height:1.55}.intro-copy p{color:#4E4840}.places li{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}
.gallery .grid{--ggap:14px}
.page-head h1{font-size:clamp(2.6rem,6vw,4.6rem);font-weight:300}
.m-head{border-bottom:1px solid var(--line);padding-bottom:14px}.m-head h2{font-size:.85rem;letter-spacing:.3em;text-transform:uppercase}.m-head p{color:var(--muted)}
.menu h3{font-size:2rem;font-weight:300;line-height:1.1}.m-line{color:var(--muted);font-size:.9rem;margin-top:6px}.menu li{color:#4E4840;border-bottom:1px solid var(--line);padding-bottom:6px}
.contact.band{border-top:1px solid var(--line)}.band h2{font-size:clamp(1.6rem,3vw,2.4rem);font-weight:300;max-width:16em}
.cp-body h1{font-size:clamp(2.4rem,5vw,4rem);font-weight:300}
.c-form span{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.c-form input,.c-form textarea{background:#F6F3EF;border:1px solid var(--line);padding:12px}
.c-form button{background:var(--fg);color:var(--bg);border:0;padding:14px 34px;letter-spacing:.2em;text-transform:uppercase;font-size:.78rem}
.foot{color:var(--muted)}
"""),
    dict(slug="03-smoke", name="Smoke", mark="Cody Cunningham", structure="bio",
         blurb="Dark and moody, with plates glowing against charcoal. Tabbed menus.",
         hero_kind="full", hero="scallops-coho-roe", hero_pos="center 55%", menu_kind="tabs",
         gallery=["foie-torchon", "tuna-tataki", "wagyu-tartare", "crudite", "steak-wine", "caviar", "stuffed-calamari"],
         menu_pics=["wagyu-ny-strip", "cacio-e-pepe-truffle", "caviar", "crudite"],
         bio_pics=["crudite", "lobster", "scallops-coho-roe"],
         fonts=font("Outfit:wght@200;300;400;500"),
         css="""
:root{--bg:#121313;--fg:#ECE8E1;--muted:#8E8A84;--line:#2A2B2B;--accent:#D9C8A9;--body:"Outfit",system-ui,sans-serif;color-scheme:dark}
.mark{font-weight:400;letter-spacing:.04em}.nav nav a{color:var(--muted);font-size:.92rem}.nav nav a[aria-current]{color:var(--fg)}
.kicker{color:var(--accent)}
.hero-full::after{background:linear-gradient(to top,rgba(18,19,19,.95),rgba(18,19,19,0) 60%)}
.hero-full h1{font-size:clamp(2.6rem,7vw,6rem);font-weight:200;letter-spacing:-.02em;line-height:1}
.hero-full p{max-width:30em;margin-top:18px;color:#CFCAC2}
.offer li{font-size:clamp(1.2rem,2.2vw,1.7rem);font-weight:200}@media (min-width:700px){.offer li::after{content:"·";margin-left:28px;color:var(--accent)}.offer li:last-child::after{content:""}}
.gallery .grid{--ggap:2px}
.intro .lead{font-size:1.4rem;font-weight:300}.intro-copy p{color:#BDB8B0}
.page-head h1,.bio-copy h1{font-size:clamp(2.8rem,7vw,5.4rem);font-weight:200;line-height:1}
.page-head p,.bio-copy p{color:#BDB8B0}
.tabs button{font-size:1.15rem;font-weight:300}.tabs button[aria-selected=true]{color:var(--accent)}
.m-note{color:var(--muted)}.menu h3{font-size:1.4rem;font-weight:300;color:var(--accent)}.m-line{color:var(--muted);font-size:.88rem}.menu li{color:#CFCAC2;font-weight:300}
.quote blockquote{font-size:clamp(1.6rem,3.6vw,2.8rem);font-weight:200;line-height:1.25}.quote cite{color:var(--accent)}
.places li{color:var(--muted)}
.contact{border-top:1px solid var(--line)}.contact h2{font-size:2rem;font-weight:200;margin-top:10px;line-height:1.2}.c-direct{color:var(--muted)}
.c-form span{font-size:.78rem;color:var(--muted)}.c-form input,.c-form textarea{background:#1B1C1C;border:1px solid #303131;padding:12px;border-radius:2px;color:var(--fg)}
.c-form button{background:var(--accent);color:#121313;border:0;padding:13px 30px}
.foot{color:var(--muted)}
"""),
    dict(slug="04-birch", name="Birch", mark="Cody Cunningham", structure="contact",
         blurb="A light serif with a three-photo mosaic and fold-open menus. Bio on the home page.",
         hero_kind="mosaic", mosaic=["beet-salad", "duck-green", "scallops-coho-roe"], menu_kind="accordion", contact_pic="steak-wine",
         gallery=["tuna-tataki", "foie-torchon", "sea-bass", "melon-gazpacho", "charcuterie", "peach-salad", "wagyu-tartare"],
         menu_pics=["duck-green", "steak-wine", "king-crab-caviar", "crudite"],
         fonts=font("Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300", "Inter:wght@400;500"),
         css="""
:root{--bg:#F6F6F3;--fg:#1D201E;--muted:#727A74;--line:#DDE0DA;--accent:#3D5A48;--body:"Inter",system-ui,sans-serif;--serif:"Newsreader",Georgia,serif;color-scheme:light}
body{font-size:16px}
.mark{font-family:var(--serif);font-size:1.35rem}.nav nav a{color:var(--muted);font-size:.9rem}.nav nav a[aria-current]{color:var(--fg)}
.kicker{color:var(--accent)}
h1,h2,h3,.offer li,.lead,blockquote{font-family:var(--serif);font-weight:300}
.hero-mosaic h1{font-size:clamp(2.6rem,5.4vw,4.8rem);line-height:1.02;letter-spacing:-.015em}
.hero-mosaic p{margin-top:20px;color:#4B524D;max-width:24em}
.offer li{font-size:clamp(1.4rem,2.6vw,2.1rem);font-style:italic}
.intro .lead{font-size:1.45rem;line-height:1.45}.intro-copy p{color:#4B524D}.places li{color:var(--muted);font-size:.88rem}
.page-head h1{font-size:clamp(2.8rem,6vw,4.8rem)}
.m-acc summary span{font-family:var(--serif);font-size:clamp(1.6rem,3vw,2.4rem);font-weight:300}.m-acc summary small{color:var(--muted)}
.m-acc summary::after{content:"+";font-size:1.4rem;color:var(--accent)}.m-acc[open] summary::after{content:"–"}
.menu h3{font-size:1.4rem}.m-line{color:var(--muted);font-size:.86rem}.menu li{color:#4B524D;font-size:.95rem}
.band h2{font-size:clamp(1.6rem,3vw,2.4rem);font-style:italic}.contact.band{border-top:1px solid var(--line)}
.cp-body h1{font-size:clamp(2.4rem,5vw,4rem)}.cp-body p{color:#4B524D}
.c-form span{font-size:.78rem;color:var(--muted)}.c-form input,.c-form textarea{border:0;border-bottom:1px solid #C5CAC3;background:transparent;padding:9px 0}
.c-form button{background:var(--accent);color:#fff;border:0;padding:13px 28px}
.foot{color:var(--muted)}
"""),
    dict(slug="05-nord", name="Nord", mark="CODY CUNNINGHAM", structure="bio",
         blurb="Cool blue-grey and a sideways-scrolling strip of plates. Contact form at the foot of each page.",
         hero_kind="strip", strip=["tuna-tataki", "duck-green", "steak-wine", "beet-salad", "scallops-coho-roe", "foie-torchon", "melon-gazpacho"],
         menu_kind="list",
         gallery=["sea-bass", "king-crab-caviar", "wagyu-tartare", "salmon-crudo", "charcuterie", "uni-gem-lettuce", "peach-salad"],
         menu_pics=["sea-bass", "salmon-crudo", "caviar"],
         bio_pics=["steak-wine", "beet-salad", "tuna-tataki"],
         fonts=font("Archivo:wdth,wght@75..100,300;75..100,400;75..100,600"),
         css="""
:root{--bg:#E9EEF0;--fg:#17232B;--muted:#64737C;--line:#CBD5DA;--accent:#17232B;--body:"Archivo",system-ui,sans-serif;color-scheme:light}
.mark{font-weight:600;letter-spacing:.24em;font-size:.82rem}.nav nav a{font-size:.88rem;color:var(--muted)}.nav nav a[aria-current]{color:var(--fg)}
.kicker{color:var(--muted)}
.hero-strip h1{font-size:clamp(2.6rem,6.8vw,6rem);font-weight:300;font-stretch:80%;line-height:.98;letter-spacing:-.02em}
.hero-strip p{margin-top:20px;max-width:30em;color:#3E4C55}
.strip{--sgap:10px;padding-bottom:8px}
.offer li{font-size:clamp(1.3rem,2.6vw,2rem);font-weight:300;font-stretch:85%}
.gallery .grid{--ggap:10px}
.intro{background:#DCE4E7}.intro .lead{font-size:1.3rem}.intro-copy p{color:#3E4C55}
.page-head h1,.bio-copy h1{font-size:clamp(2.8rem,7vw,5.6rem);font-weight:300;font-stretch:80%;line-height:.98}
.m-head h2{font-size:clamp(2rem,4vw,3rem);font-weight:300;font-stretch:80%}.m-head p,.m-line{color:var(--muted)}
.menu{background:#F4F7F8;padding:22px 22px 24px}.menu h3{font-weight:600}.menu li{color:#3E4C55;font-size:.95rem}
.quote blockquote{font-size:clamp(1.8rem,4vw,3rem);font-weight:300;font-stretch:80%;line-height:1.15}.quote cite{color:var(--muted)}
.places li{font-size:.86rem;color:var(--muted)}
.contact{background:var(--fg);color:#E9EEF0}.contact .kicker,.contact .c-direct,.contact span{color:#9FB0BA}
.contact h2{font-size:clamp(1.8rem,3vw,2.4rem);font-weight:300;font-stretch:85%;margin-top:10px}
.c-form span{font-size:.78rem}.c-form input,.c-form textarea{background:#22313A;border:1px solid #33454F;padding:12px;color:#E9EEF0}
.c-form button{background:#E9EEF0;color:var(--fg);border:0;padding:13px 30px;font-weight:600}
.foot{background:var(--fg);color:#9FB0BA;border-top:1px solid #2A3A44}
"""),
    dict(slug="06-hygge", name="Hygge", mark="Cody Cunningham", structure="contact",
         blurb="Soft, warm and friendly, with rounded photos and big type. Bio on the home page.",
         hero_kind="type", hero="steak-wine", hero_pos="center 55%", menu_kind="rows", contact_pic="duck-green",
         gallery=["beet-salad", "tuna-tataki", "charcuterie", "peach-salad", "duck-green", "cacio-e-pepe-truffle", "watermelon-rice"],
         menu_pics=["king-crab-caviar", "salmon-crudo", "duck-green", "melon-gazpacho", "wagyu-ny-strip", "cacio-e-pepe-truffle", "charcuterie",
                    "uni-gem-lettuce", "steak-wine", "albacore-carrot", "beet-salad", "sea-bass", "cured-salmon", "caviar", "charcuterie",
                    "foie-torchon", "salmon-quinoa", "lobster"],
         fonts=font("Bricolage+Grotesque:opsz,wght@12..96,300;12..96,400;12..96,600", "Figtree:wght@400;500"),
         css="""
:root{--bg:#F4F0EB;--fg:#2B2A27;--muted:#7A756D;--line:#E0D9CF;--accent:#56624A;--body:"Figtree",system-ui,sans-serif;--disp:"Bricolage Grotesque",system-ui,sans-serif;color-scheme:light}
h1,h2,h3,.mark,.offer li,.lead,.band h2{font-family:var(--disp)}
.mark{font-weight:600;font-size:1.15rem}.nav nav a{color:var(--muted)}.nav nav a[aria-current]{color:var(--fg)}
.kicker{color:var(--accent);font-weight:500}
.hero-type h1{font-size:clamp(3rem,9vw,8rem);font-weight:300;line-height:.95;letter-spacing:-.04em}
.hero-type p{margin-top:24px;max-width:30em;font-size:1.1rem;color:#55524C}
.bleed{margin:0 max(16px, env(safe-area-inset-left, 0px));border-radius:28px}
figure{border-radius:22px}.mos,.strip figure{border-radius:22px}
.gallery .grid{--ggap:14px}
.offer{gap:10px}.offer li{background:#fff;border-radius:999px;padding:10px 20px;font-size:1.05rem}
.intro .lead{font-size:1.4rem;line-height:1.45;font-weight:300}.intro-copy p{color:#55524C}.places li{background:#EAE4DC;border-radius:999px;padding:4px 12px;font-size:.85rem}
.intro-copy .places{gap:8px}
.page-head h1{font-size:clamp(3rem,8vw,6rem);font-weight:300;letter-spacing:-.04em;line-height:1}
.m-head h2{font-size:clamp(1.8rem,3.4vw,2.6rem);font-weight:400}.m-head p,.m-line{color:var(--muted)}
.menu{background:#fff;border-radius:22px;padding:28px}.menu h3{font-size:1.6rem;font-weight:400}.menu li{color:#55524C}
.band h2{font-size:clamp(1.8rem,3.4vw,2.8rem);font-weight:300;letter-spacing:-.02em}
.contact.band .in{background:#fff;border-radius:28px;padding-block:40px;margin-bottom:24px}
.cp-body h1{font-size:clamp(2.6rem,6vw,4.6rem);font-weight:300;letter-spacing:-.03em;line-height:1}.cp-body p{color:#55524C}
.c-form span{font-size:.82rem;color:var(--muted)}.c-form input,.c-form textarea{background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 14px}
.c-form button{background:var(--accent);color:#fff;border:0;border-radius:999px;padding:14px 32px;font-weight:500}
.foot{color:var(--muted)}
"""),
    dict(slug="07-gallery", name="Gallery", mark="Cody Cunningham", structure="bio",
         blurb="Like a photo exhibition: pure white, strict grid, small captions in mono. Contact form at the foot of each page.",
         hero_kind="mosaic", mosaic=["tuna-tataki", "steak-wine", "beet-salad"], menu_kind="list",
         gallery=["duck-green", "scallops-coho-roe", "foie-torchon", "sea-bass", "crudite", "wagyu-tartare", "melon-gazpacho"],
         menu_pics=["duck-green", "charcuterie", "scallops-coho-roe"],
         bio_pics=["foie-torchon", "sea-bass", "king-crab-caviar"],
         fonts=font("Inter+Tight:wght@300;400;500", "IBM+Plex+Mono:wght@400"),
         css="""
:root{--bg:#FFFFFF;--fg:#0E0E0E;--muted:#7B7B7B;--line:#E9E9E9;--accent:#0E0E0E;--body:"Inter Tight",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace;color-scheme:light}
body{font-size:16px}
.mark{font-weight:500}.nav nav a,.kicker,.m-line,.places li,.c-form span,.foot,.m-head p,.c-direct{font-family:var(--mono);font-size:.74rem;letter-spacing:.04em;text-transform:uppercase}
.nav nav a{color:var(--muted)}.nav nav a[aria-current]{color:var(--fg)}
.kicker{color:var(--muted);letter-spacing:.08em}
.hero-mosaic .in{grid-template-columns:.8fr 1.6fr}
.hero-mosaic h1{font-size:clamp(1.8rem,3vw,2.6rem);font-weight:400;line-height:1.1;letter-spacing:-.02em}
.hero-mosaic p{margin-top:16px;color:#4A4A4A;max-width:22em}
.mos{gap:3px}.gallery .grid{--ggap:3px}.bio-pics .in{--ggap:3px}
.offer{gap:4px 22px}.offer li{font-size:clamp(1.2rem,2.2vw,1.7rem);font-weight:300}
.intro .lead{font-size:1.25rem}.intro-copy p{color:#4A4A4A}
.page-head h1,.bio-copy h1{font-size:clamp(2.4rem,5vw,4rem);font-weight:400;letter-spacing:-.03em}
.m-head{border-top:1px solid var(--fg);padding-top:12px}.m-head h2{font-size:1.4rem;font-weight:500}
.menu h3{font-size:1.1rem;font-weight:500}.menu li{color:#4A4A4A;font-size:.94rem}
.m-pic.bleed{height:min(60vh,560px)}
.quote blockquote{font-size:clamp(1.4rem,2.8vw,2.2rem);font-weight:300;letter-spacing:-.02em;line-height:1.3}.quote cite{font-family:var(--mono);font-size:.74rem;text-transform:uppercase;color:var(--muted)}
.places li{color:var(--muted)}
.contact{border-top:1px solid var(--fg)}.contact h2{font-size:1.6rem;font-weight:400;margin-top:10px}
.c-form input,.c-form textarea{border:1px solid #D6D6D6;padding:11px;border-radius:0;background:#fff}
.c-form button{background:var(--fg);color:#fff;border:0;padding:12px 26px;font-family:var(--mono);font-size:.78rem;text-transform:uppercase;letter-spacing:.06em}
.foot{color:var(--muted)}
"""),
    dict(slug="08-night-table", name="Night Table", mark="Cody Cunningham", structure="contact",
         blurb="Candlelit deep green with a large italic serif. Bio on the home page.",
         hero_kind="split", hero="foie-torchon", hero_pos="center 45%", menu_kind="tabs", contact_pic="scallops-coho-roe",
         gallery=["steak-wine", "tuna-tataki", "caviar", "duck-green", "wagyu-tartare", "king-crab-caviar", "crudite"],
         menu_pics=["steak-wine", "cacio-e-pepe-truffle", "king-crab-caviar", "charcuterie"],
         fonts=font("Instrument+Serif:ital@0;1", "Inter:wght@300;400;500"),
         css="""
:root{--bg:#111613;--fg:#E5E6DF;--muted:#8F9A90;--line:#26302A;--accent:#B9C7A9;--body:"Inter",system-ui,sans-serif;--serif:"Instrument Serif",Georgia,serif;color-scheme:dark}
body{font-weight:300}
.mark{font-family:var(--serif);font-size:1.5rem;font-style:italic}.nav nav a{color:var(--muted);font-size:.9rem}.nav nav a[aria-current]{color:var(--fg)}
.kicker{color:var(--accent)}
h1,h2,h3,.offer li,.lead,blockquote,.tabs button{font-family:var(--serif);font-weight:400}
.hero-split h1{font-size:clamp(3rem,6.4vw,6rem);line-height:.95;font-style:italic}
.hero-split p{margin-top:22px;max-width:26em;color:#BFC4BA}
.soft{color:var(--accent)}
.offer li{font-size:clamp(1.6rem,3vw,2.4rem);font-style:italic}
.gallery .grid{--ggap:6px}
.intro .lead{font-size:1.6rem;line-height:1.35}.intro-copy p{color:#BFC4BA}.places li{color:var(--muted);font-size:.86rem}
.page-head h1{font-size:clamp(3.2rem,8vw,6.4rem);font-style:italic;line-height:.95}.page-head p{color:#BFC4BA}
.tabs button{font-size:1.5rem}.tabs button[aria-selected=true]{color:var(--accent)}
.m-note{color:var(--muted)}.menu h3{font-size:1.9rem;font-style:italic;color:var(--accent)}.m-line{color:var(--muted);font-size:.86rem}.menu li{color:#C9CDC4}
.band h2{font-size:clamp(2rem,4vw,3.2rem);font-style:italic}.contact.band{border-top:1px solid var(--line)}
.cp-body h1{font-size:clamp(3rem,6vw,5rem);font-style:italic;line-height:.95}.cp-body p{color:#BFC4BA}
.c-form span{font-size:.78rem;color:var(--muted)}.c-form input,.c-form textarea{background:transparent;border:0;border-bottom:1px solid #3A463E;padding:9px 0;color:var(--fg)}
.c-form button{background:var(--accent);color:#111613;border:0;padding:13px 30px;font-weight:500}
.foot{color:var(--muted)}
"""),
]

for _v in VARIANTS:
    _v["css"] = COMMON + _v["css"]

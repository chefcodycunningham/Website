"""Fail if any private client term appears in this repo.

Terms come from the PRIVATE_TERMS secret (one per line), so the list itself
is never stored in a public or menu repo. Scans text files and the text
inside .docx files. Run locally with: PRIVATE_TERMS="$(cat path/to/list)" python3 .github/scripts/privacy_check.py
"""
import os, re, sys, zipfile, pathlib

terms = [t.strip() for t in os.environ.get("PRIVATE_TERMS", "").splitlines()
         if t.strip() and not t.strip().startswith("#")]
if not terms:
    sys.exit("PRIVATE_TERMS is empty; refusing to pass without a term list.")
pat = re.compile(r"\b(" + "|".join(re.escape(t) for t in terms) + r")\b", re.I)

TEXT = {".md", ".html", ".htm", ".txt", ".css", ".js", ".json", ".yml", ".yaml", ".py", ".xml", ".svg", ".csv"}
hits = []
for p in pathlib.Path(".").rglob("*"):
    if not p.is_file() or ".git" in p.parts:
        continue
    try:
        if p.suffix.lower() in TEXT:
            text = p.read_text(encoding="utf-8", errors="ignore")
        elif p.suffix.lower() == ".docx":
            with zipfile.ZipFile(p) as z:
                text = re.sub(r"<[^>]+>", " ", z.read("word/document.xml").decode("utf-8", "ignore"))
        else:
            continue
    except Exception as e:
        print(f"warning: could not read {p}: {e}")
        continue
    for m in pat.finditer(str(p) + "\n" + text):
        hits.append(f"{p}: matched a private term")
        break

if hits:
    print("PRIVATE CLIENT INFORMATION FOUND. Remove it before this goes anywhere public:")
    print("\n".join(sorted(set(hits))))
    sys.exit(1)
print(f"Privacy check passed ({len(terms)} terms).")

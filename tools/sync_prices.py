"""Copy the current season's prices from the private menus repo into tools/prices.json.

Reads ../menus/seasons/<current season>/menu.md (or MENUS_REPO=/path/to/menus) and keeps
ONLY each menu's name and its bold price line. Dishes, notes and anything else stay behind,
so nothing private can ride along into this public repo.

Run: python3 tools/sync_prices.py   then   python3 tools/build_samples.py
"""
import json, os, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
MENUS = pathlib.Path(os.environ.get("MENUS_REPO", HERE.parent.parent / "menus"))


def current_menu():
    for p in sorted(MENUS.glob("seasons/*/menu.md"), reverse=True):
        if re.search(r"^status:\s*current\s*$", p.read_text(encoding="utf-8"), re.M):
            return p
    sys.exit(f"No season with 'status: current' under {MENUS}/seasons")


def main():
    src = current_menu()
    text = src.read_text(encoding="utf-8")
    season = re.search(r"^season:\s*(.+)$", text, re.M).group(1).strip()
    prices, name = {}, None
    for line in text.splitlines():
        if line.startswith("### "):
            name = line[4:].strip()
        elif name and re.fullmatch(r"\*\*(.+)\*\*", line.strip()):
            prices[name] = line.strip().strip("*")
            name = None
    out = HERE / "prices.json"
    out.write_text(json.dumps({"season": season, "source": str(src.relative_to(MENUS)), "prices": prices},
                              ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(prices)} prices from {season} -> {out.relative_to(HERE.parent)}")


if __name__ == "__main__":
    main()

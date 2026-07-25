import json
import os
import re
import sys

import cloudscraper
from bs4 import BeautifulSoup, Tag

WIKI_BASE = "https://exceed-fighting-system.fandom.com/wiki/"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

CHARACTERS = [
    "Ryu", "Chun-Li", "Ken", "Guile", "M. Bison", "Cammy",
    "Vega", "Zangief", "Akuma", "Sagat", "Dan", "C. Viper",
]


def tag_text(tag: Tag | None) -> str | None:
    if tag is None:
        return None
    t = tag.get_text(separator="\n", strip=True)
    return t if t else None


def clean_effect_text(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n")
    text = soup.get_text().strip()
    parts = []
    for line in text.split("\n"):
        line = line.strip().rstrip("\t")
        if line:
            parts.append(line)
    return parts


def parse_card_rows(rows: list[Tag], section_type: str) -> dict | None:
    if len(rows) < 3:
        return None

    hdr = rows[0].find_all(["th", "td"], recursive=False)
    dat = rows[1].find_all(["th", "td"], recursive=False)

    if len(hdr) < 8 or len(dat) < 9:
        return None

    card_name = tag_text(hdr[0])
    if not card_name:
        return None

    boost_header = tag_text(hdr[7]) or ""
    boost_name = re.sub(r'^Boost:\s*', '', boost_header, flags=re.UNICODE).strip()
    if not boost_name:
        boost_name = boost_header

    cost_value = tag_text(dat[1]) or ""
    range_val = tag_text(dat[2]) or ""
    power_val = tag_text(dat[3]) or ""
    speed_val = tag_text(dat[4]) or ""
    armor_val = tag_text(dat[5]) or ""
    guard_val = tag_text(dat[6]) or ""

    force_cost_raw = tag_text(dat[7]) or ""
    timing = tag_text(dat[8]) or ""

    is_ultra = section_type == "specials" and ("G" in cost_value or "g" in cost_value)

    if section_type == "normals":
        card_type = "normal"
    elif is_ultra:
        card_type = "ultra"
    else:
        card_type = "special"

    m = re.search(r'Cost:\s*(\S+)', force_cost_raw)
    boost_cost = m.group(1) if m else None

    effect_cells = rows[2].find_all(["th", "td"], recursive=False)
    strike_effects = clean_effect_text(str(effect_cells[0])) if len(effect_cells) > 0 else []
    boost_effects = clean_effect_text(str(effect_cells[1])) if len(effect_cells) > 1 else []

    card = {
        "name": card_name,
        "type": card_type,
        "cost": cost_value if cost_value else None,
        "range": range_val,
        "power": power_val,
        "speed": speed_val,
        "armor": armor_val,
        "guard": guard_val,
        "boost": {
            "name": boost_name,
            "cost": boost_cost,
            "timing": timing,
            "effect": boost_effects,
        },
        "effect": strike_effects,
    }

    if card_type == "ultra" and cost_value:
        card["exceed_cost"] = cost_value

    return card


def extract_cards(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    cards = []

    for heading in soup.find_all("h2"):
        span = heading.find("span", class_="mw-headline")
        if not span:
            continue
        headline = span.get_text(strip=True)

        if headline == "Specials and Ultras":
            section_type = "specials"
        elif headline == "Normals":
            continue
        else:
            continue

        el = heading.find_next_sibling()
        while el and el.name != "h2":
            if el.name == "table" and "fandom-table" in el.get("class", []):
                all_rows = el.find_all("tr")
                for i in range(0, len(all_rows), 3):
                    card = parse_card_rows(all_rows[i:i+3], section_type)
                    if card:
                        cards.append(card)
            el = el.find_next_sibling()

    return cards


_SCRAPER = None

def fetch_page(url: str) -> str | None:
    global _SCRAPER
    if _SCRAPER is None:
        _SCRAPER = cloudscraper.create_scraper()
    try:
        resp = _SCRAPER.get(url, timeout=30)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"  Error: {e}", file=sys.stderr)
        return None


def process_character(name: str) -> list[dict] | None:
    url = WIKI_BASE + name.replace(" ", "_")
    print(f"Fetching {name}...")
    html = fetch_page(url)
    if not html:
        return None
    cards = extract_cards(html)
    if not cards:
        print(f"  No cards found", file=sys.stderr)
        return None

    path = os.path.join(OUT_DIR, f"{name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=2, ensure_ascii=False)
    print(f"  -> {len(cards)} cards -> {name}.json")
    return cards


def main():
    total = 0
    fails = []
    for ch in CHARACTERS:
        cards = process_character(ch)
        if cards is None:
            fails.append(ch)
        else:
            total += len(cards)

    print(f"\nDone. {total} cards extracted.")
    if fails:
        print(f"Failures: {', '.join(fails)}", file=sys.stderr)


if __name__ == "__main__":
    main()

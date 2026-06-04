import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import requests

CHUNK_SIZE = 400
OVERLAP = 100
DOCUMENTS_DIR = Path("documents")
OUTPUT_FILE = Path("chunks.json")

SOURCES = [
    {"name": "01_mobalytics_beginner", "url": "https://mobalytics.gg/blog/tft/tft-guide/"},
    {"name": "02_mobalytics_economy", "url": "https://mobalytics.gg/tft/guides/how-to-manage-your-economy-in-teamfight-tactics-three-strategies"},
    {"name": "03_mobalytics_leveling", "url": "https://mobalytics.gg/tft/guides/standard-leveling-strategy"},
    {"name": "04_mobalytics_positioning", "url": "https://mobalytics.gg/blog/tft/tft-positioning-guide-how-to-get-the-most-from-your-units/"},
    {"name": "05_reddit_fundamentals", "url": "https://www.reddit.com/r/TeamfightTactics/comments/1gmpr4y/tft_fundamentals_econ_and_leveling_guide_road_to/"},
    {"name": "06_reddit_economy", "url": "https://www.reddit.com/r/CompetitiveTFT/comments/1hwxtsq/item_economy_fundamentals/"},
    {"name": "07_reddit_positioning", "url": "https://www.reddit.com/r/CompetitiveTFT/comments/14qa1r8/beginner_how_to_learn_positioning/"},
    {"name": "08_metatft_composition", "url": "https://www.metatft.com/comps"},
    {"name": "09_tftacademy_tierlist", "url": "https://tftacademy.com/tierlist/comps"},
    {"name": "10_bunnymuffins_leveling", "url": "https://bunnymuffins.lol/tft-leveling-guide/"},
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


class _TextExtractor(HTMLParser):
    SKIP_TAGS = {"script", "style", "noscript", "head", "nav", "footer", "header", "aside"}

    def __init__(self):
        super().__init__()
        self._skip_depth = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data):
        if self._skip_depth == 0:
            self.parts.append(data)


# Simple regex patterns for predictable single-occurrence boilerplate
_BOILERPLATE_PATTERNS = [
    # Mobalytics primary game navigation bar
    r"LoL TFT Diablo 4.*?DOWNLOAD APP\s*",
    # Mobalytics secondary nav bar (Set/Home/Team Comps/Guides sub-menu)
    r"Set \d+ News Set \d+ Home.*?Desktop App\s*",
    # Social share buttons
    r"(Share on (X \(Twitter\)|Twitter|Facebook|Email|SMS)\s*){2,}",
    # Accessibility skip link at page start
    r"^Skip to (main )?content\s*",
]

_BOILERPLATE_RE = [re.compile(p, re.IGNORECASE) for p in _BOILERPLATE_PATTERNS]

# Matches "By [author] · Updated on [Month Day, Year]" — the article byline pattern.
# The first occurrence is the article header; the 3rd+ signal the related-articles footer.
_BYLINE_RE = re.compile(r"By \S+\s*[·∙]\s*Updated on \w+ \d+, \d{4}", re.IGNORECASE)


def strip_boilerplate(text: str) -> str:
    for pattern in _BOILERPLATE_RE:
        text = pattern.sub(" ", text)

    # The article header uses "By Name Updated on date" (no bullet).
    # The related-articles footer uses "By Name ∙ Updated on date" (with bullet).
    # Truncate at the first bullet-byline — everything from there is the footer.
    bylines = list(_BYLINE_RE.finditer(text))
    if bylines:
        text = text[: bylines[0].start()]

    return re.sub(r"\s+", " ", text).strip()


def fetch_url(url: str) -> str:
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as exc:
        print(f"  WARNING: Could not fetch {url} — {exc}", file=sys.stderr)
        return ""


def clean_html(raw_html: str) -> str:
    extractor = _TextExtractor()
    extractor.feed(raw_html)
    text = " ".join(extractor.parts)
    return re.sub(r"\s+", " ", text).strip()


def load_documents(documents_dir: Path) -> list:
    documents = []
    for source in SOURCES:
        filepath = documents_dir / f"{source['name']}.txt"
        if filepath.exists():
            print(f"  [cached]  {source['name']}")
            text = filepath.read_text(encoding="utf-8")
        else:
            print(f"  [fetch]   {source['name']} ...")
            raw = fetch_url(source["url"])
            if not raw:
                print(f"  SKIPPED:  {source['name']} (empty response)")
                print(f"            Tip: manually save the page text to {filepath}")
                continue
            text = clean_html(raw)
            if not text.strip():
                print(f"  SKIPPED:  {source['name']} (page requires JavaScript — no text extracted)")
                print(f"            Tip: manually save the page text to {filepath}")
                continue

        text = strip_boilerplate(text)
        filepath.write_text(text, encoding="utf-8")

        if text.strip():
            documents.append({"name": source["name"], "text": text})

    return documents


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP) -> list:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        if end >= len(text):
            chunk = text[start:].strip()
            if len(chunk) >= 50:
                chunks.append(chunk)
            break

        # Walk back to the last word boundary so we never cut mid-word
        boundary = text.rfind(" ", start, end)
        if boundary <= start:
            boundary = end  # no space found — force break (e.g. long URL)

        chunk = text[start:boundary].strip()
        if len(chunk) >= 50:
            chunks.append(chunk)

        next_start = boundary - overlap
        if next_start <= start:
            next_start = boundary + 1  # always advance
        start = next_start

    return chunks


def chunk_documents(documents: list) -> list:
    all_chunks = []
    for doc in documents:
        doc_chunks = chunk_text(doc["text"])
        for i, text in enumerate(doc_chunks):
            all_chunks.append({
                "id": f"{doc['name']}_chunk_{i}",
                "source": doc["name"],
                "text": text,
            })
    return all_chunks


def main():
    print("=== TFT RAG Pipeline — Document Ingestion ===\n")

    print("Loading documents...")
    documents = load_documents(DOCUMENTS_DIR)
    print(f"\nLoaded {len(documents)} document(s).\n")

    if not documents:
        print("No documents loaded. Add .txt files to documents/ or check your network connection.")
        sys.exit(1)

    print("Chunking...")
    chunks = chunk_documents(documents)
    print(f"Total chunks produced: {len(chunks)}\n")

    OUTPUT_FILE.write_text(json.dumps(chunks, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Chunks saved to: {OUTPUT_FILE}\n")

    print("--- Sample Chunks ---")
    for sample in chunks[:3]:
        print(f"\n[{sample['id']}]")
        print(f"Length: {len(sample['text'])} chars")
        print(sample["text"])
        print("-" * 60)


if __name__ == "__main__":
    main()

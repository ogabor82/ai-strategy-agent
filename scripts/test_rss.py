from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.collectors.rss_collector import fetch_rss_news


def main() -> None:
    items = fetch_rss_news()
    print(f"Fetched {len(items)} items.")


if __name__ == "__main__":
    main()

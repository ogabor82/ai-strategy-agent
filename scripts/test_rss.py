from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.collectors.rss_collector import fetch_rss_news
from src.config import RSS_FEEDS


def main() -> None:
    print("Configured feeds:")
    for feed in RSS_FEEDS:
        print(f"- {feed['source']}: {feed['url']}")

    items = fetch_rss_news()
    print(f"\nFetched {len(items)} items.")


if __name__ == "__main__":
    main()

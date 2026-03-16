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

    print(f"\nFetched {len(items)} items.\n")

    for item in items[:10]:
        print(f"[{item.source}] {item.title}")
        print(f"Published: {item.published}")
        print(f"Link: {item.link}")
        print(f"Summary: {item.summary[:250]}")
        print("-" * 80)


if __name__ == "__main__":
    main()

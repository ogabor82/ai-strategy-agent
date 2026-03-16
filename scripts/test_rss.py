from pathlib import Path
import sys
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.collectors.rss_collector import fetch_rss_news
from src.config import RSS_FEEDS


def main() -> None:
    print("Configured feeds:")
    for feed in RSS_FEEDS:
        print(f"- {feed['source']}: {feed['url']}")

    items = fetch_rss_news()

    print("\n" + "=" * 100)
    print(f"TOTAL FETCHED ITEMS: {len(items)}")
    print("=" * 100)

    source_counts = Counter(item.source for item in items)
    print("\nItems by source:")
    for source, count in source_counts.items():
        print(f"- {source}: {count}")

    print("\nSample items:")
    for idx, item in enumerate(items[:10], start=1):
        print("\n" + "-" * 100)
        print(f"Item #{idx}")
        print(f"Source    : {item.source}")
        print(f"Title     : {item.title}")
        print(f"Published : {item.published}")
        print(f"Link      : {item.link}")
        print(f"Summary   : {item.summary[:300] if item.summary else '[NO SUMMARY]'}")

    print("\n" + "=" * 100)
    print("FIELD QUALITY CHECK")
    print("=" * 100)

    missing_title = sum(1 for item in items if not item.title)
    missing_summary = sum(1 for item in items if not item.summary)
    missing_link = sum(1 for item in items if not item.link)
    missing_published = sum(1 for item in items if not item.published)

    print(f"Missing title     : {missing_title}")
    print(f"Missing summary   : {missing_summary}")
    print(f"Missing link      : {missing_link}")
    print(f"Missing published : {missing_published}")


if __name__ == "__main__":
    main()

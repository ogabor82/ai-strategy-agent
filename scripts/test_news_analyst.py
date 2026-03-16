from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.collectors.rss_collector import fetch_rss_news
from src.agents.news_analyst import analyze_news


def main() -> None:
    items = fetch_rss_news()

    # MVP-nél első körben csak pár hírt adunk oda a modellnek
    sample_items = items[:8]

    print(f"Analyzing {len(sample_items)} news items...\n")

    result = analyze_news(sample_items)

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()

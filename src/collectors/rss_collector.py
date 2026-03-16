import feedparser
from typing import List

from src.config import RSS_FEEDS
from src.models.news import RawNewsItem


def _get_entry_value(entry, *keys: str) -> str:
    for key in keys:
        value = entry.get(key, "")
        if value:
            return str(value).strip()
    return ""


def fetch_rss_news() -> List[RawNewsItem]:
    items: List[RawNewsItem] = []

    for feed in RSS_FEEDS:
        source = feed["source"]
        url = feed["url"]

        parsed = feedparser.parse(url)

        print(
            f"[DEBUG] Source={source} | entries={len(parsed.entries)} | bozo={getattr(parsed, 'bozo', 0)}"
        )

        for entry in parsed.entries:
            item = RawNewsItem(
                source=source,
                title=_get_entry_value(entry, "title"),
                summary=_get_entry_value(entry, "summary", "description"),
                link=_get_entry_value(entry, "link"),
                published=_get_entry_value(entry, "published", "pubDate"),
            )
            items.append(item)

    return items

import feedparser
import re
from html import unescape
from typing import List

from src.config import RSS_FEEDS
from src.models.news import RawNewsItem


def _get_entry_value(entry, *keys: str) -> str:
    for key in keys:
        value = entry.get(key, "")
        if value:
            return str(value).strip()
    return ""


def _strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    return text


def _normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _clean_text(text: str) -> str:
    text = unescape(text or "")
    text = _strip_html(text)
    text = _normalize_whitespace(text)
    return text


def _normalize_title_for_key(title: str) -> str:
    title = title.lower().strip()
    title = re.sub(r"\s+", " ", title)
    return title


def _deduplicate_items(items: List[RawNewsItem]) -> List[RawNewsItem]:
    deduped: List[RawNewsItem] = []
    seen_keys: set[str] = set()

    for item in items:
        title_key = _normalize_title_for_key(item.title)

        if not title_key:
            continue

        if title_key in seen_keys:
            continue

        seen_keys.add(title_key)
        deduped.append(item)

    return deduped


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
            raw_title = _get_entry_value(entry, "title")
            raw_summary = _get_entry_value(
                entry,
                "summary",
                "description",
                "subtitle",
            )
            raw_link = _get_entry_value(entry, "link")
            raw_published = _get_entry_value(entry, "published", "pubDate", "updated")

            cleaned_title = _clean_text(raw_title)
            cleaned_summary = _clean_text(raw_summary)

            item = RawNewsItem(
                source=source,
                title=cleaned_title,
                summary=cleaned_summary,
                link=raw_link.strip(),
                published=raw_published.strip(),
            )
            items.append(item)

    deduped_items = _deduplicate_items(items)

    print(f"[DEBUG] Before dedupe={len(items)} | After dedupe={len(deduped_items)}")

    return deduped_items

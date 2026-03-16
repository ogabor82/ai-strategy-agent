from typing import List

from src.agents.news_analyst_prompt import NEWS_ANALYST_SYSTEM_PROMPT
from src.llm import get_llm
from src.models.analysis import NewsAnalysisResult
from src.models.news import RawNewsItem


def _format_news_items(news_items: List[RawNewsItem]) -> str:
    lines: List[str] = []

    for idx, item in enumerate(news_items, start=1):
        lines.append(f"Item #{idx}")
        lines.append(f"Source: {item.source}")
        lines.append(f"Title: {item.title}")
        lines.append(f"Published: {item.published}")
        if item.summary:
            lines.append(f"Summary: {item.summary}")
        else:
            lines.append("Summary: [NO SUMMARY]")
        lines.append(f"Link: {item.link}")
        lines.append("")

    return "\n".join(lines)


def analyze_news(news_items: List[RawNewsItem]) -> NewsAnalysisResult:
    llm = get_llm().with_structured_output(NewsAnalysisResult)

    formatted_news = _format_news_items(news_items)

    user_prompt = f"""
Analyze the following financial news items and extract the most market-relevant events.

Return a NewsAnalysisResult object.

News items:
{formatted_news}
"""

    result = llm.invoke(
        [
            ("system", NEWS_ANALYST_SYSTEM_PROMPT),
            ("user", user_prompt),
        ]
    )

    return result

import os
from dotenv import load_dotenv

load_dotenv()

RSS_FEEDS = [
    {
        "source": "ECB",
        "url": "https://www.ecb.europa.eu/rss/press.html",
    },
    {
        "source": "Portfolio",
        "url": "https://www.portfolio.hu/rss/befektetes.xml",
    },
]

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

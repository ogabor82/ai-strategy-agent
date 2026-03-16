from pydantic import BaseModel
from typing import List
from src.models.news import RawNewsItem


class AppState(BaseModel):
    raw_news: List[RawNewsItem] = []

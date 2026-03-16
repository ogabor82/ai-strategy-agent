from pydantic import BaseModel


class RawNewsItem(BaseModel):
    source: str
    title: str
    summary: str
    link: str
    published: str

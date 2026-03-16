from langchain_openai import ChatOpenAI

from src.config import OPENAI_API_KEY, OPENAI_MODEL


def get_llm() -> ChatOpenAI:
    if not OPENAI_API_KEY:
        raise ValueError("Missing OPENAI_API_KEY in .env")

    return ChatOpenAI(
        model=OPENAI_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0,
    )

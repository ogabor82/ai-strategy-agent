from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.agents.news_analyst_prompt import NEWS_ANALYST_SYSTEM_PROMPT


def main() -> None:
    print(NEWS_ANALYST_SYSTEM_PROMPT)


if __name__ == "__main__":
    main()

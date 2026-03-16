from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.llm import get_llm
from src.config import OPENAI_MODEL


def main() -> None:
    llm = get_llm()
    print("LLM client created successfully.")
    print(f"Configured model: {OPENAI_MODEL}")
    print(f"Client type: {type(llm).__name__}")


if __name__ == "__main__":
    main()

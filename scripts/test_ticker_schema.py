from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.models.analysis import TickerSelectionResult


def main() -> None:
    sample = TickerSelectionResult(
        candidates=[
            {
                "asset": "XOM",
                "thesis": "Oil supply concerns may support large energy names.",
                "direction": "bullish",
                "confidence": 0.76,
                "related_event_indices": [1],
            },
            {
                "asset": "VGK",
                "thesis": "ECB policy tone may continue to pressure some European risk assets.",
                "direction": "mixed",
                "confidence": 0.62,
                "related_event_indices": [2],
            },
        ]
    )

    print(sample.model_dump_json(indent=2))


if __name__ == "__main__":
    main()

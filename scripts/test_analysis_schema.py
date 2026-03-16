from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.models.analysis import NewsAnalysisResult


def main() -> None:
    sample = NewsAnalysisResult(
        events=[
            {
                "summary": "Oil prices are rising due to geopolitical supply concerns.",
                "event_type": "geopolitics",
                "affected_assets": ["XOM", "CVX", "XLE"],
                "impact": "bullish",
                "confidence": 0.82,
                "tradeability": "high",
            },
            {
                "summary": "ECB signaled that restrictive policy may remain in place longer.",
                "event_type": "macro",
                "affected_assets": ["VGK", "EUFN"],
                "impact": "mixed",
                "confidence": 0.66,
                "tradeability": "medium",
            },
        ]
    )

    print(sample.model_dump_json(indent=2))


if __name__ == "__main__":
    main()

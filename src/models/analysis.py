from typing import List, Literal
from pydantic import BaseModel, Field


ImpactType = Literal["bullish", "bearish", "mixed", "uncertain"]
TradeabilityType = Literal["high", "medium", "low"]


class MarketEvent(BaseModel):
    summary: str = Field(..., description="Short summary of the market-relevant event")
    event_type: str = Field(
        ..., description="Type of event, e.g. macro, earnings, regulation, geopolitics"
    )
    affected_assets: List[str] = Field(
        default_factory=list,
        description="Relevant tickers, ETFs, or assets affected by the event",
    )
    impact: ImpactType = Field(..., description="Expected directional market impact")
    confidence: float = Field(
        ..., ge=0.0, le=1.0, description="Confidence score between 0 and 1"
    )
    tradeability: TradeabilityType = Field(
        ..., description="How tradeable the event appears"
    )


class NewsAnalysisResult(BaseModel):
    events: List[MarketEvent] = Field(
        default_factory=list,
        description="List of extracted market-relevant events",
    )

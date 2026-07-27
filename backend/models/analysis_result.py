"""
Analysis Result model.
"""

from dataclasses import dataclass

from backend.models.confluence_score_v2 import ConfluenceScoreV2
from backend.models.trade_signal import TradeSignal


@dataclass(frozen=True)
class AnalysisResult:
    """
    Final analysis returned to the application.
    """

    symbol: str

    timeframe: str

    current_price: float

    market_bias: str

    confluence: ConfluenceScoreV2

    signal: TradeSignal

    summary: str

    reasons: list[str]
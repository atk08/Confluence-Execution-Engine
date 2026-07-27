"""
Analysis Result Engine.
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.analysis_result import AnalysisResult
from backend.models.confluence_score_v2 import ConfluenceScoreV2
from backend.models.trade_signal import TradeSignal


class AnalysisResultEngine(AnalysisEngine):
    """
    Combines final outputs into a single application response.
    """

    name = "Analysis Result Engine"

    @classmethod
    def analyze(
        cls,
        symbol: str,
        timeframe: str,
        confluence: ConfluenceScoreV2,
        signal: TradeSignal,
        current_price: float = 0.0,
        market_bias: str = "UNKNOWN",
        reasons: list[str] | None = None,
    ) -> AnalysisResult:

        if signal.signal.value == "BUY":
            summary = (
                "Bullish setup detected with strong confluence."
            )

        elif signal.signal.value == "SELL":
            summary = (
                "Bearish setup detected with strong confluence."
            )

        else:
            summary = (
                "Setup does not have enough confluence yet."
            )

        return AnalysisResult(
            symbol=symbol,
            timeframe=timeframe,
            current_price=current_price,
            market_bias=market_bias,
            confluence=confluence,
            signal=signal,
            summary=summary,
            reasons=reasons or [],
        )
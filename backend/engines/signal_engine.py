"""
Signal Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.confluence_score_v2 import ConfluenceScoreV2
from backend.models.trade_signal import Signal, TradeSignal


class SignalEngine(AnalysisEngine):
    """
    Converts a confluence score into a trading signal.
    """

    name = "Signal Engine"

    BUY_THRESHOLD = 80.0
    SELL_THRESHOLD = 20.0

    @classmethod
    def analyze(
        cls,
        confluence: ConfluenceScoreV2,
    ) -> TradeSignal:

        if confluence.score >= cls.BUY_THRESHOLD:
            return TradeSignal(
                signal=Signal.BUY,
                confidence=confluence.score,
                confluence_score=confluence.score,
                reasons=[
                    "Confluence score exceeds BUY threshold.",
                ],
            )

        if confluence.score <= cls.SELL_THRESHOLD:
            return TradeSignal(
                signal=Signal.SELL,
                confidence=100.0 - confluence.score,
                confluence_score=confluence.score,
                reasons=[
                    "Confluence score is below SELL threshold.",
                ],
            )

        return TradeSignal(
            signal=Signal.WAIT,
            confidence=50.0,
            confluence_score=confluence.score,
            reasons=[
                "Confluence score is neutral.",
            ],
        )
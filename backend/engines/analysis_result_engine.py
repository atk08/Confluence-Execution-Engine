"""
Analysis Result Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_result import AnalysisResult
from backend.models.confluence_score_v2 import ConfluenceScoreV2
from backend.models.trade_signal import TradeSignal


class AnalysisResultEngine(AnalysisEngine):
    """
    Combines the final outputs into a single result.
    """

    name = "Analysis Result Engine"

    @classmethod
    def analyze(
        cls,
        symbol: str,
        timeframe: str,
        confluence: ConfluenceScoreV2,
        signal: TradeSignal,
    ) -> AnalysisResult:

        return AnalysisResult(
            symbol=symbol,
            timeframe=timeframe,
            confluence=confluence,
            signal=signal,
            reasons=[
                "Analysis completed successfully.",
            ],
        )
"""
Trend Engine.
"""

from backend.engines.structure_engine import StructureEngine
from backend.models.candles import Candle
from backend.models.trend import Trend
from backend.models.trend_result import TrendResult


class TrendEngine:
    """
    Determines the current market trend from market structure.
    """

    @staticmethod
    def analyze(candles: list[Candle]) -> TrendResult:

        structure = StructureEngine.analyze(candles)

        higher_high_score = structure.higher_highs.score
        higher_low_score = structure.higher_lows.score

        confidence = (
            higher_high_score +
            higher_low_score
        ) / 2

        if (
            higher_high_score >= 0.60
            and higher_low_score >= 0.60
        ):
            trend = Trend.BULLISH

        elif (
            higher_high_score <= 0.40
            and higher_low_score <= 0.40
        ):
            trend = Trend.BEARISH

        else:
            trend = Trend.RANGING

        return TrendResult(
            trend=trend,
            score=round(confidence, 2),
            confidence=round(confidence, 2),
        )
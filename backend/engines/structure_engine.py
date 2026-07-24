"""
Structure Engine.
"""

from backend.engines.higher_high_analyzer import HigherHighAnalyzer
from backend.engines.higher_low_analyzer import HigherLowAnalyzer
from backend.models.candles import Candle


class StructureEngine:

    @staticmethod
    def analyze(candles: list[Candle]):

        higher_highs = HigherHighAnalyzer.analyze(candles)
        higher_lows = HigherLowAnalyzer.analyze(candles)

        score = (
            higher_highs.score +
            higher_lows.score
        ) / 2

        return {
            "score": round(score, 2),
            "bullish": score >= 0.60,
            "higher_highs": higher_highs,
            "higher_lows": higher_lows,
        }
"""
Higher High Analyzer.
"""

from backend.models.candles import Candle


class HigherHighAnalyzer:
    """
    Detects whether highs are consistently increasing.
    """

    @staticmethod
    def score(candles: list[Candle]) -> float:

        if len(candles) < 2:
            return 0.5

        comparisons = 0
        higher_highs = 0

        for i in range(1, len(candles)):

            comparisons += 1

            if candles[i].high > candles[i - 1].high:
                higher_highs += 1

        return higher_highs / comparisons
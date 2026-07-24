"""
Higher High Analyzer.
"""

from backend.engines.swing_detector import SwingDetector
from backend.models.candles import Candle


class HigherHighAnalyzer:
    """
    Scores the consistency of higher swing highs.
    """

    @staticmethod
    def score(candles: list[Candle]) -> float:

        swings = SwingDetector.detect_swings(candles)

        highs = [
            swing
            for swing in swings
            if swing.kind == "HIGH"
        ]

        if len(highs) < 2:
            return 0.5

        comparisons = 0
        higher_highs = 0

        for i in range(1, len(highs)):

            comparisons += 1

            if highs[i].price > highs[i - 1].price:
                higher_highs += 1

        return higher_highs / comparisons
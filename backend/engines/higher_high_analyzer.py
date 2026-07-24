"""
Higher High Analyzer.
"""

from backend.engines.swing_detector import SwingDetector
from backend.models.candles import Candle
from backend.models.higher_high_result import HigherHighResult


class HigherHighAnalyzer:
    """
    Scores the consistency of higher swing highs.
    """

    @staticmethod
    def analyze(candles: list[Candle]) -> HigherHighResult:

        swings = SwingDetector.detect_swings(candles)

        highs = [
            swing
            for swing in swings
            if swing.kind == "HIGH"
        ]

        if len(highs) < 2:
            return HigherHighResult(
                score=0.5,
                total_highs=len(highs),
                higher_highs=0,
                failed_highs=0,
            )

        comparisons = len(highs) - 1
        higher_highs = 0

        for i in range(1, len(highs)):
            if highs[i].price > highs[i - 1].price:
                higher_highs += 1

        failed_highs = comparisons - higher_highs

        score = higher_highs / comparisons

        return HigherHighResult(
            score=score,
            total_highs=len(highs),
            higher_highs=higher_highs,
            failed_highs=failed_highs,
        )
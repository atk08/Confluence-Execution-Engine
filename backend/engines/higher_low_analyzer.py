"""
Higher Low Analyzer.
"""

from backend.engines.swing_detector import SwingDetector
from backend.models.candles import Candle
from backend.models.higher_low_result import HigherLowResult


class HigherLowAnalyzer:
    """
    Scores the consistency of higher swing lows.
    """

    @staticmethod
    def analyze(candles: list[Candle]) -> HigherLowResult:

        swings = SwingDetector.detect_swings(candles)

        lows = [
            swing
            for swing in swings
            if swing.kind == "LOW"
        ]

        if len(lows) < 2:
            return HigherLowResult(
                score=0.5,
                total_lows=len(lows),
                higher_lows=0,
                failed_lows=0,
            )

        comparisons = len(lows) - 1
        higher_lows = 0

        for i in range(1, len(lows)):
            if lows[i].price > lows[i - 1].price:
                higher_lows += 1

        failed_lows = comparisons - higher_lows

        score = higher_lows / comparisons

        return HigherLowResult(
            score=score,
            total_lows=len(lows),
            higher_lows=higher_lows,
            failed_lows=failed_lows,
        )
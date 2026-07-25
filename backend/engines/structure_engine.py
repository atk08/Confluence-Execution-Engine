"""
Structure Engine.
"""

from backend.engines.higher_high_analyzer import HigherHighAnalyzer
from backend.engines.higher_low_analyzer import HigherLowAnalyzer
from backend.engines.swing_detector import SwingDetector
from backend.models.candles import Candle
from backend.models.structure_result import StructureResult
from backend.models.swing_point import SwingPoint
from backend.models.trend import Trend


class StructureEngine:
    """
    Builds the current confirmed market structure.
    """

    @staticmethod
    def analyze(candles: list[Candle]) -> StructureResult:

        higher_highs = HigherHighAnalyzer.analyze(candles)
        higher_lows = HigherLowAnalyzer.analyze(candles)

        swings = SwingDetector.detect_swings(candles)

        swing_highs: list[SwingPoint] = [
            swing
            for swing in swings
            if swing.kind == "HIGH"
        ]

        swing_lows: list[SwingPoint] = [
            swing
            for swing in swings
            if swing.kind == "LOW"
        ]

        latest_swing_high = (
            swing_highs[-1]
            if len(swing_highs) >= 1
            else None
        )

        previous_swing_high = (
            swing_highs[-2]
            if len(swing_highs) >= 2
            else None
        )

        latest_swing_low = (
            swing_lows[-1]
            if len(swing_lows) >= 1
            else None
        )

        previous_swing_low = (
            swing_lows[-2]
            if len(swing_lows) >= 2
            else None
        )

        score = (
            higher_highs.score +
            higher_lows.score
        ) / 2

        if score >= 0.60:
            trend = Trend.BULLISH
        elif score <= 0.40:
            trend = Trend.BEARISH
        else:
            trend = Trend.RANGING

        return StructureResult(
            score=round(score, 2),
            trend=trend,
            latest_swing_high=latest_swing_high,
            previous_swing_high=previous_swing_high,
            latest_swing_low=latest_swing_low,
            previous_swing_low=previous_swing_low,
            higher_highs=higher_highs,
            higher_lows=higher_lows,
        )
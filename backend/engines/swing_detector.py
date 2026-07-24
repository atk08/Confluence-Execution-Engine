"""
Swing detection engine.
"""

from backend.models.candles import Candle
from backend.models.swing_point import SwingPoint


class SwingDetector:
    """
    Detects swing highs and swing lows.
    """

    @staticmethod
    def is_swing_high(previous: Candle, current: Candle, next: Candle) -> bool:
        return (
            current.high > previous.high
            and current.high > next.high
        )

    @staticmethod
    def is_swing_low(previous: Candle, current: Candle, next: Candle) -> bool:
        return (
            current.low < previous.low
            and current.low < next.low
        )

    @staticmethod
    def detect_swings(candles: list[Candle]) -> list[SwingPoint]:
        """
        Detect all swing highs and swing lows.
        """

        swings = []

        if len(candles) < 3:
            return swings

        for i in range(1, len(candles) - 1):

            previous = candles[i - 1]
            current = candles[i]
            next_candle = candles[i + 1]

            if SwingDetector.is_swing_high(previous, current, next_candle):
                swings.append(
                    SwingPoint(
                        index=i,
                        price=current.high,
                        kind="HIGH",
                    )
                )

            if SwingDetector.is_swing_low(previous, current, next_candle):
                swings.append(
                    SwingPoint(
                        index=i,
                        price=current.low,
                        kind="LOW",
                    )
                )

        return swings
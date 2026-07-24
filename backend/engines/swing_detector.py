"""
Swing detection engine.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Candle:
    high: float
    low: float
    close: float


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
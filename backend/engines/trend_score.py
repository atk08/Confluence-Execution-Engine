"""
Trend Score Engine.
"""

from backend.models.candles import Candle
from backend.models.trend_result import TrendResult


class TrendScore:
    """
    Evaluates trend direction and confidence.
    """

    @staticmethod
    def calculate(candles: list[Candle]) -> TrendResult:

        if len(candles) < 2:
            return TrendResult(
                score=0.0,
                direction="Unknown",
                confidence=0.0,
            )

        first_close = candles[0].close
        last_close = candles[-1].close

        if last_close > first_close:
            return TrendResult(
                score=1.0,
                direction="Bullish",
                confidence=1.0,
            )

        if last_close < first_close:
            return TrendResult(
                score=0.0,
                direction="Bearish",
                confidence=1.0,
            )

        return TrendResult(
            score=0.5,
            direction="Sideways",
            confidence=0.5,
        )
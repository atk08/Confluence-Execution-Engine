"""
Trend scoring.
"""

from backend.models.candles import Candle
from backend.models.trend import Trend
from backend.models.trend_result import TrendResult


class TrendScore:
    """
    Simple trend scoring.
    """

    @staticmethod
    def calculate(candles: list[Candle]) -> TrendResult:

        if len(candles) < 2:
            return TrendResult(
                trend=Trend.UNKNOWN,
                score=0.0,
                confidence=0.0,
            )

        first_close = candles[0].close
        last_close = candles[-1].close

        if last_close > first_close:
            return TrendResult(
                trend=Trend.BULLISH,
                score=1.0,
                confidence=1.0,
            )

        if last_close < first_close:
            return TrendResult(
                trend=Trend.BEARISH,
                score=0.0,
                confidence=1.0,
            )

        return TrendResult(
            trend=Trend.RANGING,
            score=0.5,
            confidence=0.5,
        )
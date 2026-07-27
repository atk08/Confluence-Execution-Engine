"""
ATR Engine.

Calculates the Average True Range (ATR).
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.atr_result import ATRResult


class ATREngine(AnalysisEngine):
    """
    Calculates Average True Range.
    """

    name = "ATR"

    DEFAULT_PERIOD = 14

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
        period: int = DEFAULT_PERIOD,
    ) -> ATRResult:

        candles = context.candles

        if len(candles) < 2:
            return ATRResult(
                value=0.0,
                period=period,
            )

        true_ranges = []

        previous_close = candles[0].close

        for candle in candles[1:]:

            tr = max(
                candle.high - candle.low,
                abs(candle.high - previous_close),
                abs(candle.low - previous_close),
            )

            true_ranges.append(tr)

            previous_close = candle.close

        #
        # Use only the most recent ATR period.
        #

        if len(true_ranges) > period:
            true_ranges = true_ranges[-period:]

        atr = sum(true_ranges) / len(true_ranges)

        return ATRResult(
            value=round(atr, 4),
            period=period,
        )
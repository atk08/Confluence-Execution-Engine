"""
Fair Value Gap Engine.
"""

from backend.models.candles import Candle
from backend.models.fair_value_gap_result import (
    FairValueGapResult,
)


class FairValueGapEngine:
    """
    Detects Fair Value Gaps (FVGs).
    """

    @staticmethod
    def analyze(candles: list[Candle]) -> FairValueGapResult:

        if len(candles) < 3:
            return FairValueGapResult(
                bullish_gap=False,
                bearish_gap=False,
                score=0.0,
                gap_high=None,
                gap_low=None,
            )

        c1 = candles[-3]
        c2 = candles[-2]  # kept for readability
        c3 = candles[-1]

        bullish_gap = (
            c3.low > c1.high
        )

        bearish_gap = (
            c3.high < c1.low
        )

        gap_high = None
        gap_low = None

        if bullish_gap:
            gap_high = c3.low
            gap_low = c1.high

        elif bearish_gap:
            gap_high = c1.low
            gap_low = c3.high

        score = 1.0 if bullish_gap or bearish_gap else 0.0

        return FairValueGapResult(
            bullish_gap=bullish_gap,
            bearish_gap=bearish_gap,
            score=score,
            gap_high=gap_high,
            gap_low=gap_low,
        )
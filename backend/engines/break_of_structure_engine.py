"""
Break Of Structure Engine.
"""

from backend.engines.structure_engine import StructureEngine
from backend.models.break_of_structure_result import (
    BreakOfStructureResult,
)
from backend.models.candles import Candle


class BreakOfStructureEngine:
    """
    Detects bullish or bearish Break of Structure
    using the current confirmed market structure.
    """

    @staticmethod
    def analyze(candles: list[Candle]) -> BreakOfStructureResult:

        structure = StructureEngine.analyze(candles)

        last_candle = candles[-1]

        bullish_break = (
            structure.latest_swing_high is not None
            and last_candle.close > structure.latest_swing_high.price
        )

        bearish_break = (
            structure.latest_swing_low is not None
            and last_candle.close < structure.latest_swing_low.price
        )

        broken_level = None

        if bullish_break:
            broken_level = structure.latest_swing_high.price

        elif bearish_break:
            broken_level = structure.latest_swing_low.price

        score = 1.0 if bullish_break or bearish_break else 0.0

        return BreakOfStructureResult(
            bullish_break=bullish_break,
            bearish_break=bearish_break,
            score=score,
            broken_level=broken_level,
        )
"""
Change Of Character Engine.
"""

from backend.engines.structure_engine import StructureEngine
from backend.models.candles import Candle
from backend.models.change_of_character_result import (
    ChangeOfCharacterResult,
)
from backend.models.trend import Trend


class ChangeOfCharacterEngine:
    """
    Detects institutional Change of Character (CHoCH).
    """

    @staticmethod
    def analyze(candles: list[Candle]) -> ChangeOfCharacterResult:

        structure = StructureEngine.analyze(candles)

        last_candle = candles[-1]

        bullish_choch = (
            structure.trend == Trend.BEARISH
            and structure.latest_swing_high is not None
            and last_candle.close > structure.latest_swing_high.price
        )

        bearish_choch = (
            structure.trend == Trend.BULLISH
            and structure.latest_swing_low is not None
            and last_candle.close < structure.latest_swing_low.price
        )

        broken_level = None

        if bullish_choch:
            broken_level = structure.latest_swing_high.price

        elif bearish_choch:
            broken_level = structure.latest_swing_low.price

        score = 1.0 if bullish_choch or bearish_choch else 0.0

        return ChangeOfCharacterResult(
            bullish_choch=bullish_choch,
            bearish_choch=bearish_choch,
            score=score,
            broken_level=broken_level,
        )
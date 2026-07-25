"""
Liquidity Sweep Engine.
"""

from backend.engines.structure_engine import StructureEngine
from backend.models.candles import Candle
from backend.models.liquidity_sweep_result import (
    LiquiditySweepResult,
)


class LiquiditySweepEngine:
    """
    Detects liquidity sweeps of confirmed swing highs and lows.
    """

    @staticmethod
    def analyze(candles: list[Candle]) -> LiquiditySweepResult:

        structure = StructureEngine.analyze(candles)

        last_candle = candles[-1]

        bullish_sweep = (
            structure.latest_swing_high is not None
            and last_candle.high > structure.latest_swing_high.price
            and last_candle.close < structure.latest_swing_high.price
        )

        bearish_sweep = (
            structure.latest_swing_low is not None
            and last_candle.low < structure.latest_swing_low.price
            and last_candle.close > structure.latest_swing_low.price
        )

        swept_level = None

        if bullish_sweep:
            swept_level = structure.latest_swing_high.price

        elif bearish_sweep:
            swept_level = structure.latest_swing_low.price

        score = 1.0 if bullish_sweep or bearish_sweep else 0.0

        return LiquiditySweepResult(
            bullish_sweep=bullish_sweep,
            bearish_sweep=bearish_sweep,
            score=score,
            swept_level=swept_level,
        )
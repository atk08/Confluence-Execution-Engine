"""
Institutional Liquidity Sweep Engine.

Detects recent liquidity grabs from swing highs/lows.
"""

from backend.engines.structure_engine import StructureEngine

from backend.models.candles import Candle

from backend.models.liquidity_sweep_result import (
    LiquiditySweepResult,
)


class LiquiditySweepEngine:

    """
    Detects institutional liquidity sweeps.
    """

    LOOKBACK = 20


    @staticmethod
    def analyze(
        candles: list[Candle],
    ) -> LiquiditySweepResult:


        if len(candles) < 5:

            return LiquiditySweepResult(
                bullish_sweep=False,
                bearish_sweep=False,
                score=0.0,
                swept_level=None,
            )


        start = max(
            0,
            len(candles) - LiquiditySweepEngine.LOOKBACK
        )


        recent = candles[start:]


        for i in range(
            len(recent) - 1,
            0,
            -1
        ):

            previous_candles = candles[:start+i]


            structure = StructureEngine.analyze(
                previous_candles
            )


            candle = recent[i]


            #
            # Sweep swing high
            # Project convention:
            # bullish sweep
            #

            if structure.latest_swing_high:

                level = (
                    structure.latest_swing_high.price
                )


                if (
                    candle.high > level
                    and candle.close < level
                ):

                    return LiquiditySweepResult(
                        bullish_sweep=True,
                        bearish_sweep=False,
                        score=1.0,
                        swept_level=level,
                    )


            #
            # Sweep swing low
            # Project convention:
            # bearish sweep
            #

            if structure.latest_swing_low:

                level = (
                    structure.latest_swing_low.price
                )


                if (
                    candle.low < level
                    and candle.close > level
                ):

                    return LiquiditySweepResult(
                        bullish_sweep=False,
                        bearish_sweep=True,
                        score=1.0,
                        swept_level=level,
                    )


        return LiquiditySweepResult(
            bullish_sweep=False,
            bearish_sweep=False,
            score=0.0,
            swept_level=None,
        )
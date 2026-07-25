"""
Institutional Order Block Engine.
"""

from backend.engines.break_of_structure_engine import BreakOfStructureEngine
from backend.engines.change_of_character_engine import ChangeOfCharacterEngine
from backend.engines.fair_value_gap_engine import FairValueGapEngine
from backend.models.candles import Candle
from backend.models.order_block_result import OrderBlockResult


class OrderBlockEngine:

    LOOKBACK_CANDLES = 20

    @staticmethod
    def analyze(candles: list[Candle]) -> OrderBlockResult:

        if len(candles) < 2:
            return OrderBlockEngine._empty_result()

        bos = BreakOfStructureEngine.analyze(candles)
        choch = ChangeOfCharacterEngine.analyze(candles)
        fvg = FairValueGapEngine.analyze(candles)

        # For v1 we require:
        # - Bullish BOS OR Bullish CHoCH
        # - Bullish FVG

        if not (
            (bos.bullish_break or choch.bullish_choch)
            and fvg.bullish_gap
        ):
            return OrderBlockEngine._empty_result()

        start = max(
            0,
            len(candles) - OrderBlockEngine.LOOKBACK_CANDLES,
        )

        for i in range(len(candles) - 2, start - 1, -1):

            candle = candles[i]

            if candle.close < candle.open:

                return OrderBlockResult(
                    bullish_block=True,
                    bearish_block=False,
                    score=1.0,
                    block_high=candle.high,
                    block_low=candle.low,
                    candle_index=i,
                    mitigated=False,
                    touched=False,
                    broken=False,
                )

        return OrderBlockEngine._empty_result()

    @staticmethod
    def _empty_result():

        return OrderBlockResult(
            bullish_block=False,
            bearish_block=False,
            score=0.0,
            block_high=None,
            block_low=None,
            candle_index=None,
            mitigated=False,
            touched=False,
            broken=False,
        )
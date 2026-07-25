"""
Institutional Order Block Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.order_block_result import OrderBlockResult


class OrderBlockEngine(AnalysisEngine):
    """
    Detects the last valid order block following a confirmed
    institutional move.
    """

    name = "OrderBlock"

    LOOKBACK_CANDLES = 20

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> OrderBlockResult:

        move = context.institutional_move

        if move is None:
            return cls._empty_result()

        if not move.bullish_move and not move.bearish_move:
            return cls._empty_result()

        candles = context.candles

        start = max(
            0,
            len(candles) - cls.LOOKBACK_CANDLES,
        )

        if move.bullish_move:

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

        if move.bearish_move:

            for i in range(len(candles) - 2, start - 1, -1):

                candle = candles[i]

                if candle.close > candle.open:

                    return OrderBlockResult(
                        bullish_block=False,
                        bearish_block=True,
                        score=1.0,
                        block_high=candle.high,
                        block_low=candle.low,
                        candle_index=i,
                        mitigated=False,
                        touched=False,
                        broken=False,
                    )

        return cls._empty_result()

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
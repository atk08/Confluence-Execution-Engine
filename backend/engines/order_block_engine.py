"""
Institutional Order Block Engine.

Detects potential institutional order blocks
after displacement and directional momentum.
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.analysis_context import AnalysisContext

from backend.models.order_block_result import OrderBlockResult


class OrderBlockEngine(AnalysisEngine):
    """
    Detects institutional order blocks.
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


        #
        # Require minimum institutional strength
        #

        if move.score < 30:
            return cls._empty_result()


        candles = context.candles


        if len(candles) < 3:
            return cls._empty_result()


        start = max(
            0,
            len(candles) - cls.LOOKBACK_CANDLES,
        )


        current = candles[-1]


        #
        # Bullish Order Block
        #
        # Last bearish candle before bullish displacement
        #

        bullish_confirmation = (
            move.bullish_move
            or (
                move.displacement
                and current.close > current.open
            )
        )


        if bullish_confirmation:

            for i in range(
                len(candles) - 2,
                start - 1,
                -1,
            ):

                candle = candles[i]


                if candle.close < candle.open:

                    return OrderBlockResult(
                        bullish_block=True,
                        bearish_block=False,
                        score=move.score,
                        block_high=candle.high,
                        block_low=candle.low,
                        candle_index=i,
                        mitigated=False,
                        touched=False,
                        broken=False,
                    )


        #
        # Bearish Order Block
        #
        # Last bullish candle before bearish displacement
        #

        bearish_confirmation = (
            move.bearish_move
            or (
                move.displacement
                and current.close < current.open
            )
        )


        if bearish_confirmation:

            for i in range(
                len(candles) - 2,
                start - 1,
                -1,
            ):

                candle = candles[i]


                if candle.close > candle.open:

                    return OrderBlockResult(
                        bullish_block=False,
                        bearish_block=True,
                        score=move.score,
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
"""
Institutional Move Engine V2.

Scores institutional strength using:
- displacement
- BOS
- CHoCH
- FVG
- momentum
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.analysis_context import AnalysisContext

from backend.models.institutional_move_result import (
    InstitutionalMoveResult,
)


class InstitutionalMoveEngine(AnalysisEngine):
    """
    Calculates institutional move confidence.
    """

    name = "InstitutionalMove"


    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> InstitutionalMoveResult:


        candles = context.candles


        if len(candles) < 2:

            return cls.empty()


        previous = candles[-2]
        current = candles[-1]


        #
        # Displacement
        #

        previous_body = abs(
            previous.close - previous.open
        )

        current_body = abs(
            current.close - current.open
        )


        displacement = (
            current_body > previous_body
        )


        score = 0.0


        #
        # Displacement score
        #

        if displacement:
            score += 30


        #
        # BOS
        #

        has_bos = (
            context.bos.bullish_break
            or context.bos.bearish_break
        )

        if has_bos:
            score += 25


        #
        # CHoCH
        #

        has_choch = (
            context.choch.bullish_choch
            or context.choch.bearish_choch
        )

        if has_choch:
            score += 20


        #
        # Fair Value Gap
        #

        has_fvg = (
            context.fvg.bullish_gap
            or context.fvg.bearish_gap
        )

        if has_fvg:
            score += 15


        #
        # Direction
        #

        bullish_move = (
            current.close > current.open
            and score >= 40
        )

        bearish_move = (
            current.close < current.open
            and score >= 40
        )


        return InstitutionalMoveResult(
            bullish_move=bullish_move,
            bearish_move=bearish_move,
            score=min(score,100),
            has_bos=has_bos,
            has_choch=has_choch,
            has_fvg=has_fvg,
            displacement=displacement,
        )


    @staticmethod
    def empty():

        return InstitutionalMoveResult(
            bullish_move=False,
            bearish_move=False,
            score=0.0,
            has_bos=False,
            has_choch=False,
            has_fvg=False,
            displacement=False,
        )
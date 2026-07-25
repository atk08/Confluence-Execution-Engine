"""
Institutional Move Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.institutional_move_result import (
    InstitutionalMoveResult,
)


class InstitutionalMoveEngine(AnalysisEngine):
    """
    Detects high-conviction institutional moves.
    """

    name = "InstitutionalMove"

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> InstitutionalMoveResult:

        candles = context.candles

        if len(candles) < 2:
            return InstitutionalMoveResult(
                bullish_move=False,
                bearish_move=False,
                score=0.0,
                has_bos=False,
                has_choch=False,
                has_fvg=False,
                displacement=False,
            )

        previous = candles[-2]
        current = candles[-1]

        previous_body = abs(previous.close - previous.open)
        current_body = abs(current.close - current.open)

        displacement = current_body > previous_body

        bullish_move = (
            displacement
            and context.fvg.bullish_gap
            and (
                context.bos.bullish_break
                or context.choch.bullish_change
            )
        )

        bearish_move = (
            displacement
            and context.fvg.bearish_gap
            and (
                context.bos.bearish_break
                or context.choch.bearish_change
            )
        )

        score = 100.0 if (bullish_move or bearish_move) else 0.0

        return InstitutionalMoveResult(
            bullish_move=bullish_move,
            bearish_move=bearish_move,
            score=score,
            has_bos=(
                context.bos.bullish_break
                or context.bos.bearish_break
            ),
            has_choch=(
                context.choch.bullish_choch
                or context.choch.bearish_choch
            ),
            has_fvg=(
                context.fvg.bullish_gap
                or context.fvg.bearish_gap
            ),
            displacement=displacement,
        )
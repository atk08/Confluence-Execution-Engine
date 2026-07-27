"""
Institutional Context Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.institutional_context import InstitutionalContext


class InstitutionalContextEngine(AnalysisEngine):
    """
    Evaluates institutional trading context using liquidity,
    displacement, order blocks and fair value gaps.
    """

    name = "Institutional Context Engine"

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> InstitutionalContext:

        liquidity_quality = (
            context.liquidity.score
            if context.liquidity is not None
            else 0.0
        )

        displacement_quality = (
            context.institutional_move.score
            if context.institutional_move is not None
            else 0.0
        )

        # Placeholder until V2 engines are upgraded
        order_block_quality = 20.0
        fair_value_gap_quality = 20.0
        alignment_quality = 20.0

        total = (
            order_block_quality
            + fair_value_gap_quality
            + liquidity_quality
            + displacement_quality
            + alignment_quality
        )

        bullish = False
        bearish = False

        strengths: list[str] = []
        weaknesses: list[str] = []

        if (
            context.institutional_move is not None
            and context.institutional_move.bullish_move
        ):
            bullish = True
            strengths.append("Bullish institutional move")

        if (
            context.institutional_move is not None
            and context.institutional_move.bearish_move
        ):
            bearish = True
            strengths.append("Bearish institutional move")

        if liquidity_quality < 10.0:
            weaknesses.append("Weak liquidity confirmation")

        if displacement_quality < 10.0:
            weaknesses.append("Weak displacement")

        return InstitutionalContext(
            score=min(total, 100.0),
            order_block_quality=order_block_quality,
            fair_value_gap_quality=fair_value_gap_quality,
            liquidity_quality=liquidity_quality,
            displacement_quality=displacement_quality,
            alignment_quality=alignment_quality,
            bullish=bullish,
            bearish=bearish,
            strengths=strengths,
            weaknesses=weaknesses,
            reasons=[
                "Institutional context evaluated.",
            ],
        )
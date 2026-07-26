"""
Confluence Engine.

Combines analysis results into a single normalized score.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.confluence_result import ConfluenceResult


class ConfluenceEngine(AnalysisEngine):
    """
    Produces an overall market confluence score.
    """

    name = "Confluence"

    WEIGHTS = {
        "trend": 40,
        "structure": 30,
        "institutional": 30,
    }

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> ConfluenceResult:

        trend_score = context.trend.score
        structure_score = context.structure.score

        institutional_score = (
            context.institutional_move.score
            if context.institutional_move
            else 0.0
        )

        final_score = (
            trend_score * cls.WEIGHTS["trend"]
            + structure_score * cls.WEIGHTS["structure"]
            + institutional_score * cls.WEIGHTS["institutional"]
        ) / 100

        return ConfluenceResult(
            score=round(final_score, 2),

            trend_score=trend_score,
            structure_score=structure_score,
            institutional_score=institutional_score,

            order_block_score=0.0,
            avwap_score=0.0,
            volume_profile_score=0.0,

            bullish=final_score >= 70,
            bearish=final_score <= 30,
        )
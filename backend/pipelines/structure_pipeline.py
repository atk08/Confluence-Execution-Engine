"""
Structure Pipeline.

Responsible for all market structure analysis.
"""

from backend.engines.structure_engine import (
    StructureEngine,
)

from backend.engines.trend_engine import (
    TrendEngine,
)

from backend.models.analysis_context import (
    AnalysisContext,
)


class StructurePipeline:
    """
    Computes all market structure analysis.
    """

    @staticmethod
    def run(
        context: AnalysisContext,
    ) -> AnalysisContext:

        structure = StructureEngine.analyze(
            context.candles
        )

        trend = TrendEngine.analyze(
            context.candles
        )

        return AnalysisContext(
            candles=context.candles,

            structure=structure,

            trend=trend,

            bos=context.bos,

            choch=context.choch,

            liquidity=context.liquidity,

            fvg=context.fvg,

            institutional_move=context.institutional_move,

            avwap=context.avwap,

            volume_profile=context.volume_profile,
        )
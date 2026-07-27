"""
Main Analysis Pipeline.

Runs all analysis stages and preserves the full AnalysisContext.
"""

from backend.models.analysis_context import AnalysisContext
from backend.models.candles import Candle

from backend.engines.structure_engine import StructureEngine
from backend.engines.trend_engine import TrendEngine
from backend.engines.break_of_structure_engine import (
    BreakOfStructureEngine,
)
from backend.engines.change_of_character_engine import (
    ChangeOfCharacterEngine,
)
from backend.engines.liquidity_sweep_engine import (
    LiquiditySweepEngine,
)
from backend.engines.fair_value_gap_engine import (
    FairValueGapEngine,
)

from backend.pipelines.structure_pipeline import (
    StructurePipeline,
)

from backend.pipelines.institutional_pipeline import (
    InstitutionalPipeline,
)


class AnalysisPipeline:
    """
    Master pipeline.
    """

    @staticmethod
    def run(
        candles: list[Candle],
    ) -> AnalysisContext:

        #
        # Initial context
        #

        context = AnalysisContext(
            candles=candles,

            structure=StructureEngine.analyze(
                candles
            ),

            trend=TrendEngine.analyze(
                candles
            ),

            bos=BreakOfStructureEngine.analyze(
                candles
            ),

            choch=ChangeOfCharacterEngine.analyze(
                candles
            ),

            liquidity=LiquiditySweepEngine.analyze(
                candles
            ),

            fvg=FairValueGapEngine.analyze(
                candles
            ),

            institutional_move=None,

            avwap=None,

            volume_profile=None,
        )


        #
        # Market structure enrichment
        #

        context = StructurePipeline.run(
            context
        )


        #
        # Institutional enrichment
        #

        context = InstitutionalPipeline.run(
            context
        )


        return context
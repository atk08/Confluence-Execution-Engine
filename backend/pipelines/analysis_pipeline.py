"""
Main Analysis Pipeline.
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
    Executes every analysis pipeline.
    """

    @staticmethod
    def run(candles: list[Candle]) -> AnalysisContext:

        context = AnalysisContext(
            candles=candles,
            structure=StructureEngine.analyze(candles),
            trend=TrendEngine.analyze(candles),
            bos=BreakOfStructureEngine.analyze(candles),
            choch=ChangeOfCharacterEngine.analyze(candles),
            liquidity=LiquiditySweepEngine.analyze(candles),
            fvg=FairValueGapEngine.analyze(candles),
        )

        context = StructurePipeline.run(context)

        context = InstitutionalPipeline.run(context)

        return context
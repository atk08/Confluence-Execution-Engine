"""
Institutional Pipeline.

Responsible for institutional concepts.
"""

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
from backend.models.analysis_context import AnalysisContext


class InstitutionalPipeline:
    """
    Computes institutional concepts.
    """

    @staticmethod
    def run(context: AnalysisContext) -> AnalysisContext:

        bos = BreakOfStructureEngine.analyze(context.candles)

        choch = ChangeOfCharacterEngine.analyze(context.candles)

        liquidity = LiquiditySweepEngine.analyze(context.candles)

        fvg = FairValueGapEngine.analyze(context.candles)

        return AnalysisContext(
            candles=context.candles,
            structure=context.structure,
            trend=context.trend,
            bos=bos,
            choch=choch,
            liquidity=liquidity,
            fvg=fvg,
        )
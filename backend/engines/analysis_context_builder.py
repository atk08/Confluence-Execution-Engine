"""
Analysis Context Builder.
"""

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
from backend.engines.institutional_move_engine import (
    InstitutionalMoveEngine,
)
from backend.models.analysis_context import AnalysisContext
from backend.models.candles import Candle


class AnalysisContextBuilder:
    """
    Builds a complete AnalysisContext from raw candles.
    """

    @staticmethod
    def build(candles: list[Candle]) -> AnalysisContext:

        structure = StructureEngine.analyze(candles)

        trend = TrendEngine.analyze(candles)

        bos = BreakOfStructureEngine.analyze(candles)

        choch = ChangeOfCharacterEngine.analyze(candles)

        liquidity = LiquiditySweepEngine.analyze(candles)

        fvg = FairValueGapEngine.analyze(candles)

        context = AnalysisContext(
            candles=candles,
            structure=structure,
            trend=trend,
            bos=bos,
            choch=choch,
            liquidity=liquidity,
            fvg=fvg,
            institutional_move=None,
        )

        institutional_move = InstitutionalMoveEngine.analyze(context)

        return AnalysisContext(
            candles=context.candles,
            structure=context.structure,
            trend=context.trend,
            bos=context.bos,
            choch=context.choch,
            liquidity=context.liquidity,
            fvg=context.fvg,
            institutional_move=institutional_move,
        )
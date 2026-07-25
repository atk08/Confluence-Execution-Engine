"""
Shared Analysis Context.
"""

from dataclasses import dataclass

from backend.models.candles import Candle
from backend.models.structure_result import StructureResult
from backend.models.trend_result import TrendResult
from backend.models.break_of_structure_result import (
    BreakOfStructureResult,
)
from backend.models.change_of_character_result import (
    ChangeOfCharacterResult,
)
from backend.models.liquidity_sweep_result import (
    LiquiditySweepResult,
)
from backend.models.fair_value_gap_result import (
    FairValueGapResult,
)


@dataclass(frozen=True)
class AnalysisContext:
    """
    Contains every analysis result produced for one asset.

    Higher-level engines should consume this object instead of
    recalculating lower-level analyses.
    """

    candles: list[Candle]

    structure: StructureResult

    trend: TrendResult

    bos: BreakOfStructureResult

    choch: ChangeOfCharacterResult

    liquidity: LiquiditySweepResult

    fvg: FairValueGapResult
"""
Shared Analysis Context.
"""

from dataclasses import dataclass

from backend.models.candles import Candle
from backend.models.structure_result import StructureResult
from backend.models.trend_result import TrendResult
from backend.models.break_of_structure_result import BreakOfStructureResult
from backend.models.change_of_character_result import ChangeOfCharacterResult
from backend.models.liquidity_sweep_result import LiquiditySweepResult
from backend.models.fair_value_gap_result import FairValueGapResult
from backend.models.institutional_move_result import InstitutionalMoveResult


@dataclass(frozen=True)
class AnalysisContext:
    """
    Contains every analysis result produced for one asset.
    """

    candles: list[Candle]

    structure: StructureResult
    trend: TrendResult

    bos: BreakOfStructureResult
    choch: ChangeOfCharacterResult
    liquidity: LiquiditySweepResult
    fvg: FairValueGapResult

    institutional_move: InstitutionalMoveResult | None = None
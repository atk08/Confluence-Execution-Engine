"""
Test helpers for building AnalysisContext objects.
"""

from backend.models.analysis_context import AnalysisContext
from backend.models.break_of_structure_result import BreakOfStructureResult
from backend.models.candles import Candle
from backend.models.change_of_character_result import (
    ChangeOfCharacterResult,
)
from backend.models.fair_value_gap_result import (
    FairValueGapResult,
)
from backend.models.higher_high_result import HigherHighResult
from backend.models.higher_low_result import HigherLowResult
from backend.models.institutional_move_result import (
    InstitutionalMoveResult,
)
from backend.models.liquidity_sweep_result import (
    LiquiditySweepResult,
)
from backend.models.structure_result import StructureResult
from backend.models.trend import Trend
from backend.models.trend_result import TrendResult


def build_context(
    candles: list[Candle],
    bullish_move: bool = False,
    bearish_move: bool = False,
) -> AnalysisContext:

    return AnalysisContext(
        candles=candles,

        structure=StructureResult(
            score=0.0,
            trend=Trend.RANGING,
            latest_swing_high=None,
            previous_swing_high=None,
            latest_swing_low=None,
            previous_swing_low=None,
            higher_highs=HigherHighResult(
                score=0.0,
                total_highs=0,
                higher_highs=0,
                failed_highs=0,
            ),
            higher_lows=HigherLowResult(
                score=0.0,
                total_lows=0,
                higher_lows=0,
                failed_lows=0,
            ),
        ),

        trend=TrendResult(
            trend=Trend.RANGING,
            score=0.0,
            confidence=0.0,
        ),

        bos=BreakOfStructureResult(
            bullish_break=False,
            bearish_break=False,
            score=0.0,
            broken_level=None,
        ),

        choch=ChangeOfCharacterResult(
            bullish_choch=False,
            bearish_choch=False,
            score=0.0,
            broken_level=None,
        ),

        liquidity=LiquiditySweepResult(
            bullish_sweep=False,
            bearish_sweep=False,
            score=0.0,
            swept_level=None,
        ),

        fvg=FairValueGapResult(
            bullish_gap=False,
            bearish_gap=False,
            score=0.0,
            gap_high=None,
            gap_low=None,
            mitigated=False,
            fill_percent=0.0,
            gap_size=0.0,
        ),

        institutional_move=InstitutionalMoveResult(
            bullish_move=bullish_move,
            bearish_move=bearish_move,
            score=100.0 if (bullish_move or bearish_move) else 0.0,
            has_bos=bullish_move or bearish_move,
            has_choch=False,
            has_fvg=False,
            displacement=bullish_move or bearish_move,
        ),
    )
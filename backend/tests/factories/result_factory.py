"""
Reusable test factories for engine tests.
"""

from backend.models.analysis_context import AnalysisContext
from backend.models.break_of_structure_result import BreakOfStructureResult
from backend.models.change_of_character_result import ChangeOfCharacterResult
from backend.models.institutional_move_result import InstitutionalMoveResult
from backend.models.liquidity_sweep_result import LiquiditySweepResult
from backend.models.structure_result import StructureResult
from backend.models.trend import Trend
from backend.models.trend_result import TrendResult


def make_trend_result() -> TrendResult:
    return TrendResult(
        trend=Trend.BULLISH,
        score=20.0,
        confidence=1.0,
    )


def make_structure_result() -> StructureResult:
    return StructureResult(
        score=20.0,
        trend=Trend.BULLISH,
        latest_swing_high=None,
        previous_swing_high=None,
        latest_swing_low=None,
        previous_swing_low=None,
        higher_highs=None,
        higher_lows=None,
    )


def make_bos_result() -> BreakOfStructureResult:
    return BreakOfStructureResult(
        bullish_break=True,
        bearish_break=False,
        score=15.0,
        broken_level=None,
    )


def make_choch_result() -> ChangeOfCharacterResult:
    return ChangeOfCharacterResult(
        bullish_choch=False,
        bearish_choch=False,
        score=10.0,
        broken_level=None,
    )


def make_liquidity_result() -> LiquiditySweepResult:
    return LiquiditySweepResult(
        bullish_sweep=True,
        bearish_sweep=False,
        score=20.0,
        swept_level=None,
    )


def make_institutional_result() -> InstitutionalMoveResult:
    return InstitutionalMoveResult(
        bullish_move=True,
        bearish_move=False,
        displacement=True,
        score=20.0,
        has_bos=True,
        has_choch=False,
        has_fvg=True,
    )


def make_analysis_context() -> AnalysisContext:
    return AnalysisContext(
        candles=[],
        structure=make_structure_result(),
        trend=make_trend_result(),
        bos=make_bos_result(),
        choch=make_choch_result(),
        liquidity=make_liquidity_result(),
        fvg=None,
        institutional_move=make_institutional_result(),
        avwap=None,
        volume_profile=None,
    )
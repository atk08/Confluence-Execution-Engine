"""
Tests for InstitutionalContextEngine.
"""

from backend.engines.institutional_context_engine import InstitutionalContextEngine
from backend.models.analysis_context import AnalysisContext
from backend.models.break_of_structure_result import BreakOfStructureResult
from backend.models.change_of_character_result import ChangeOfCharacterResult
from backend.models.institutional_move_result import InstitutionalMoveResult
from backend.models.liquidity_sweep_result import LiquiditySweepResult
from backend.models.structure_result import StructureResult
from backend.models.trend import Trend
from backend.models.trend_result import TrendResult


def test_institutional_context_engine():

    trend = TrendResult(
        trend=Trend.BULLISH,
        score=20.0,
        confidence=1.0,
    )

    structure = StructureResult(
        score=20.0,
        trend=Trend.BULLISH,
        latest_swing_high=None,
        previous_swing_high=None,
        latest_swing_low=None,
        previous_swing_low=None,
        higher_highs=None,
        higher_lows=None,
    )

    bos = BreakOfStructureResult(
        bullish_break=True,
        bearish_break=False,
        score=15.0,
        broken_level=None,
    )

    choch = ChangeOfCharacterResult(
        bullish_choch=False,
        bearish_choch=False,
        score=10.0,
        broken_level=None,
    )

    liquidity = LiquiditySweepResult(
        bullish_sweep=True,
        bearish_sweep=False,
        score=20.0,
        swept_level=None,
    )

    institutional = InstitutionalMoveResult(
        bullish_move=True,
        bearish_move=False,
        displacement=True,
        score=20.0,
        has_bos=True,
        has_choch=False,
        has_fvg=True,
    )

    context = AnalysisContext(
        candles=[],
        structure=structure,
        trend=trend,
        bos=bos,
        choch=choch,
        liquidity=liquidity,
        fvg=None,
        institutional_move=institutional,
        avwap=None,
        volume_profile=None,
    )

    result = InstitutionalContextEngine.analyze(context)

    assert result.score == 100.0
    assert result.bullish is True
    assert result.bearish is False
    assert result.order_block_quality == 20.0
    assert result.fair_value_gap_quality == 20.0
    assert result.liquidity_quality == 20.0
    assert result.displacement_quality == 20.0
    assert result.alignment_quality == 20.0
    assert "Bullish institutional move" in result.strengths
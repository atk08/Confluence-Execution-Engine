"""
Tests for ConfluenceScoreV2Engine.
"""

from backend.engines.confluence_score_v2_engine import (
    ConfluenceScoreV2Engine,
)
from backend.models.avwap_score import AVWAPScore
from backend.models.confluence_score_v2 import ConfluenceScoreV2
from backend.models.fair_value_gap_score import FairValueGapScore
from backend.models.liquidity_score import LiquidityScore
from backend.models.market_structure_score import (
    MarketStructureScore,
)
from backend.models.order_block_score import OrderBlockScore
from backend.models.volume_profile_score import (
    VolumeProfileScore,
)


def test_confluence_score_v2():

    market = MarketStructureScore(
        score=100.0,
        trend=20.0,
        higher_highs=15.0,
        higher_lows=15.0,
        break_of_structure=15.0,
        change_of_character=15.0,
        displacement=10.0,
        liquidity=10.0,
        reasons=[],
    )

    volume = VolumeProfileScore(
        score=100.0,
        poc_quality=20.0,
        value_area=20.0,
        hvn_lvn=20.0,
        reaction_strength=20.0,
        confluence=20.0,
        reasons=[],
    )

    avwap = AVWAPScore(
        score=100.0,
        anchor_quality=20.0,
        distance=20.0,
        trend_alignment=20.0,
        reaction_strength=20.0,
        confluence=20.0,
        reasons=[],
    )

    order_block = OrderBlockScore(
        score=100.0,
        freshness=20.0,
        displacement=20.0,
        volume=20.0,
        trend_alignment=20.0,
        proximity=20.0,
        reasons=[],
    )

    fvg = FairValueGapScore(
        score=100.0,
        freshness=20.0,
        size=20.0,
        mitigation=20.0,
        trend_alignment=20.0,
        proximity=20.0,
        reasons=[],
    )

    liquidity = LiquidityScore(
        score=100.0,
        sweep_strength=20.0,
        location=20.0,
        trend_alignment=20.0,
        continuation_probability=20.0,
        freshness=20.0,
        reasons=[],
    )

    result = ConfluenceScoreV2Engine.analyze(
        market,
        volume,
        avwap,
        order_block,
        fvg,
        liquidity,
    )

    assert isinstance(result, ConfluenceScoreV2)
    assert result.score == 100.0
    assert result.market_structure == 25.0
    assert result.volume_profile == 20.0
    assert result.avwap == 20.0
    assert result.order_block == 15.0
    assert result.fair_value_gap == 10.0
    assert result.liquidity == 10.0
"""
Tests for SignalEngine.
"""

from backend.engines.signal_engine import SignalEngine
from backend.models.confluence_score_v2 import ConfluenceScoreV2
from backend.models.trade_signal import Signal


def make_score(score: float) -> ConfluenceScoreV2:
    return ConfluenceScoreV2(
        score=score,
        market_structure=0.0,
        volume_profile=0.0,
        avwap=0.0,
        order_block=0.0,
        fair_value_gap=0.0,
        liquidity=0.0,
        reasons=[],
    )


def test_buy_signal():

    result = SignalEngine.analyze(make_score(90.0))

    assert result.signal == Signal.BUY
    assert result.confluence_score == 90.0


def test_sell_signal():

    result = SignalEngine.analyze(make_score(10.0))

    assert result.signal == Signal.SELL
    assert result.confluence_score == 10.0


def test_wait_signal():

    result = SignalEngine.analyze(make_score(55.0))

    assert result.signal == Signal.WAIT
    assert result.confluence_score == 55.0
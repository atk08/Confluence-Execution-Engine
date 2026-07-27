"""
Tests for StructureStopEngine.
"""

from backend.engines.structure_stop_engine import StructureStopEngine
from backend.models.candles import Candle
from backend.models.trade_direction import TradeDirection
from backend.tests.context_factory import build_context


def test_buy_falls_back_to_atr_when_no_swing_exists():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 99, 101, 1200),
        Candle(101, 103, 100, 102, 1500),
    ]

    context = build_context(candles)

    result = StructureStopEngine.analyze(
        context,
        TradeDirection.BUY,
    )

    assert result.source == "ATR"
    assert result.fallback_used is True
    assert result.stop_price < 102


def test_sell_falls_back_to_atr_when_no_swing_exists():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 99, 101, 1200),
        Candle(101, 103, 100, 102, 1500),
    ]

    context = build_context(candles)

    result = StructureStopEngine.analyze(
        context,
        TradeDirection.SELL,
    )

    assert result.source == "ATR"
    assert result.fallback_used is True
    assert result.stop_price > 102
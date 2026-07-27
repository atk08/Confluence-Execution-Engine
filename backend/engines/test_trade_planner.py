"""
Tests for TradePlanner.
"""

from backend.engines.trade_planner import TradePlanner
from backend.models.candles import Candle
from backend.models.execution_confidence import ExecutionConfidence
from backend.models.trade_direction import TradeDirection
from backend.tests.context_factory import build_context


def test_trade_plan_creation():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 99, 101, 1200),
        Candle(101, 103, 100, 102, 1500),
    ]

    context = build_context(candles)

    plan = TradePlanner.analyze(context)

    assert plan.direction == TradeDirection.SELL
    assert plan.confidence == ExecutionConfidence.LOW
    assert plan.confluence_score == 0.0
    assert plan.approved is True

    assert plan.entry_price == 102

    #
    # SELL trade expectations
    #

    assert plan.stop_loss > plan.entry_price
    assert plan.take_profit < plan.entry_price
    assert plan.risk_reward >= 2.0

    assert isinstance(plan.reasons, list)
    assert isinstance(plan.warnings, list)
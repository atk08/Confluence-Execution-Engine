"""
Tests for ExecutionTimingEngine.
"""

from backend.engines.execution_timing_engine import ExecutionTimingEngine
from backend.models.candles import Candle
from backend.models.execution_confidence import ExecutionConfidence
from backend.models.execution_result import ExecutionResult
from backend.models.trade_direction import TradeDirection
from backend.tests.context_factory import build_context


def test_buy_confirmation():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 103, 99, 102, 1200),
    ]

    context = build_context(candles)

    execution = ExecutionResult(
        trade_score=80.0,
        direction=TradeDirection.BUY,
        confidence=ExecutionConfidence.HIGH,
        should_trade=True,
        entry_price=102,
        stop_loss=None,
        take_profit=None,
        risk_reward=None,
        reasons=[],
        warnings=[],
    )

    result = ExecutionTimingEngine.analyze(
        context,
        execution,
    )

    assert result.ready is True
    assert result.timing_score == 100.0


def test_sell_confirmation():

    candles = [
        Candle(102, 103, 101, 102, 1000),
        Candle(102, 102, 99, 100, 1200),
    ]

    context = build_context(candles)

    execution = ExecutionResult(
        trade_score=80.0,
        direction=TradeDirection.SELL,
        confidence=ExecutionConfidence.HIGH,
        should_trade=True,
        entry_price=100,
        stop_loss=None,
        take_profit=None,
        risk_reward=None,
        reasons=[],
        warnings=[],
    )

    result = ExecutionTimingEngine.analyze(
        context,
        execution,
    )

    assert result.ready is True
    assert result.timing_score == 100.0


def test_not_enough_candles():

    candles = [
        Candle(100, 101, 99, 100, 1000),
    ]

    context = build_context(candles)

    execution = ExecutionResult(
        trade_score=80.0,
        direction=TradeDirection.BUY,
        confidence=ExecutionConfidence.HIGH,
        should_trade=True,
        entry_price=100,
        stop_loss=None,
        take_profit=None,
        risk_reward=None,
        reasons=[],
        warnings=[],
    )

    result = ExecutionTimingEngine.analyze(
        context,
        execution,
    )

    assert result.ready is False
    assert result.timing_score == 0.0
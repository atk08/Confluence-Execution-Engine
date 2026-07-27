from backend.engines.risk_engine import RiskEngine
from backend.models.candles import Candle
from backend.models.execution_confidence import ExecutionConfidence
from backend.models.execution_result import ExecutionResult
from backend.models.trade_direction import TradeDirection
from backend.tests.context_factory import build_context


def test_risk_engine_returns_values():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 99, 101, 1200),
        Candle(101, 103, 100, 102, 1500),
    ]

    context = build_context(candles)

    execution = ExecutionResult(
        trade_score=0.0,
        direction=TradeDirection.BUY,
        confidence=ExecutionConfidence.LOW,
        should_trade=True,
        entry_price=102,
        stop_loss=None,
        take_profit=None,
        risk_reward=None,
        reasons=[],
        warnings=[],
    )

    result = RiskEngine.analyze(
        context,
        execution,
    )

    assert result.entry_price == 102
    assert result.stop_loss < result.entry_price
    assert result.take_profit > result.entry_price
    assert result.risk > 0
    assert result.reward > result.risk
    assert result.risk_reward >= 2.0
    assert result.approved is True
    assert len(result.reasons) >= 1


def test_risk_engine_no_data():

    context = build_context([])

    execution = ExecutionResult(
        trade_score=0.0,
        direction=TradeDirection.BUY,
        confidence=ExecutionConfidence.LOW,
        should_trade=False,
        entry_price=None,
        stop_loss=None,
        take_profit=None,
        risk_reward=None,
        reasons=[],
        warnings=[],
    )

    result = RiskEngine.analyze(
        context,
        execution,
    )

    assert result.entry_price is None
    assert result.approved is False
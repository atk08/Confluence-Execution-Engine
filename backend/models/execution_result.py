"""
Execution Engine result.
"""

from dataclasses import dataclass

from backend.models.execution_confidence import ExecutionConfidence
from backend.models.trade_direction import TradeDirection


@dataclass(frozen=True)
class ExecutionResult:
    """
    Final trade recommendation.
    """

    trade_score: float

    direction: TradeDirection

    confidence: ExecutionConfidence

    should_trade: bool

    entry_price: float | None

    stop_loss: float | None

    take_profit: float | None

    risk_reward: float | None

    reasons: list[str]

    warnings: list[str]
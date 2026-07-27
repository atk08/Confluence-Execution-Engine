"""
Trade plan produced by the ExecutionEngine.
"""

from dataclasses import dataclass

from backend.models.execution_confidence import ExecutionConfidence
from backend.models.trade_direction import TradeDirection


@dataclass(frozen=True)
class TradePlan:
    """
    Complete trade recommendation.
    """

    direction: TradeDirection

    confidence: ExecutionConfidence

    confluence_score: float

    approved: bool

    entry_price: float | None

    stop_loss: float | None

    take_profit: float | None

    risk_reward: float | None

    reasons: list[str]

    warnings: list[str]
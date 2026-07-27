"""
Risk Engine result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RiskResult:
    """
    Result produced by the RiskEngine.
    """

    entry_price: float | None

    stop_loss: float | None

    take_profit: float | None

    risk: float | None

    reward: float | None

    risk_reward: float | None

    approved: bool

    reasons: list[str]
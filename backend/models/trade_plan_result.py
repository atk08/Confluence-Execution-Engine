from dataclasses import dataclass


@dataclass(frozen=True)
class TradePlanResult:

    direction: str

    entry: float

    stop_loss: float

    take_profit_1: float

    risk_reward: float

    reasons: list[str]
"""
Trade Signal model.
"""

from dataclasses import dataclass
from enum import Enum


class Signal(Enum):
    BUY = "BUY"
    SELL = "SELL"
    WAIT = "WAIT"


@dataclass(frozen=True)
class TradeSignal:
    """
    Final trading signal.
    """

    signal: Signal

    confidence: float

    confluence_score: float

    reasons: list[str]
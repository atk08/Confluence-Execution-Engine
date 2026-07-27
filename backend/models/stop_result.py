"""
Stop placement result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class StopResult:
    """
    Represents a calculated stop-loss placement.
    """

    stop_price: float

    source: str

    reason: str

    fallback_used: bool = False
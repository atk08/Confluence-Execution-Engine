"""
ATR Engine result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ATRResult:
    """
    Average True Range calculation result.
    """

    value: float

    period: int
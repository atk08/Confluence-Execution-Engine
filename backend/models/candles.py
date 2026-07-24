"""
Shared OHLCV candle models.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Candle:
    """
    Represents a single OHLCV candle.
    """

    open: float
    high: float
    low: float
    close: float
    volume: float
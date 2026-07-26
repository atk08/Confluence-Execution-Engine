"""
Trade direction enum.
"""

from enum import Enum


class TradeDirection(str, Enum):
    """
    Valid trade directions.
    """

    BUY = "BUY"
    SELL = "SELL"
    NEUTRAL = "NEUTRAL"
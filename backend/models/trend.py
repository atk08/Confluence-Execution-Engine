"""
Market trend states.
"""

from enum import Enum


class Trend(str, Enum):
    """
    Represents the current market trend.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    RANGING = "RANGING"
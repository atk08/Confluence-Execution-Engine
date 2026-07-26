"""
Execution confidence enum.
"""

from enum import Enum


class ExecutionConfidence(str, Enum):
    """
    Confidence level for a trade.
    """

    VERY_HIGH = "Very High"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
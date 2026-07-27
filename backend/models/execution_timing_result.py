"""
Execution Timing Engine result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionTimingResult:
    """
    Indicates whether market timing is suitable
    for entering a trade.
    """

    ready: bool

    timing_score: float

    reasons: list[str]
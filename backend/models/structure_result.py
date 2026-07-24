"""
Structure analysis result.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class StructureResult:
    """
    Generic result for any market structure analyzer.
    """

    score: float

    total_points: int

    successful_points: int

    failed_points: int
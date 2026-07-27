"""
AVWAP Score model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AVWAPScore:
    """
    Represents the quality score of an Anchored VWAP setup.
    """

    score: float

    anchor_quality: float

    distance: float

    trend_alignment: float

    reaction_strength: float

    confluence: float

    reasons: list[str]
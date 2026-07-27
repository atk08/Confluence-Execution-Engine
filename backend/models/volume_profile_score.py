"""
Volume Profile Score model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class VolumeProfileScore:
    """
    Represents the quality score of a Volume Profile setup.
    """

    score: float

    poc_quality: float

    value_area: float

    hvn_lvn: float

    reaction_strength: float

    confluence: float

    reasons: list[str]
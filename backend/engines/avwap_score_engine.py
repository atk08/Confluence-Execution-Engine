"""
AVWAP Score Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.avwap_result import AVWAPResult
from backend.models.avwap_score import AVWAPScore


class AVWAPScoreEngine(AnalysisEngine):
    """
    Scores an Anchored VWAP setup from 0–100.
    """

    name = "AVWAP Score"

    @classmethod
    def analyze(
        cls,
        avwap: AVWAPResult,
    ) -> AVWAPScore:

        if avwap.score <= 0:

            return AVWAPScore(
                score=0.0,
                anchor_quality=0.0,
                distance=0.0,
                trend_alignment=0.0,
                reaction_strength=0.0,
                confluence=0.0,
                reasons=[
                    "No valid AVWAP setup.",
                ],
            )

        anchor_quality = 20.0
        distance = 20.0
        trend_alignment = 20.0
        reaction_strength = 20.0
        confluence = 20.0

        total = (
            anchor_quality
            + distance
            + trend_alignment
            + reaction_strength
            + confluence
        )

        return AVWAPScore(
            score=total,
            anchor_quality=anchor_quality,
            distance=distance,
            trend_alignment=trend_alignment,
            reaction_strength=reaction_strength,
            confluence=confluence,
            reasons=[
                "AVWAP scored successfully.",
            ],
        )
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

        # Distance Score
        if avwap.distance_percent <= 0.25:
            distance = 20.0
        elif avwap.distance_percent <= 0.50:
            distance = 18.0
        elif avwap.distance_percent <= 1.00:
            distance = 15.0
        elif avwap.distance_percent <= 2.00:
            distance = 10.0
        else:
            distance = 5.0

        # Trend Alignment
        trend_alignment = 20.0 if (avwap.bullish or avwap.bearish) else 0.0

        # Existing AVWAP confidence
        anchor_quality = min(avwap.score, 20.0)

        # Placeholder until we have reaction data
        reaction_strength = 20.0

        # Placeholder until we have Volume Profile/FVG integration
        confluence = 20.0

        total = (
            anchor_quality
            + distance
            + trend_alignment
            + reaction_strength
            + confluence
        )

        return AVWAPScore(
            score=min(total, 100.0),
            anchor_quality=anchor_quality,
            distance=distance,
            trend_alignment=trend_alignment,
            reaction_strength=reaction_strength,
            confluence=confluence,
            reasons=[
                f"Distance from AVWAP: {avwap.distance_percent:.2f}%",
                "Trend aligned with AVWAP."
                if trend_alignment > 0
                else "Trend not aligned.",
            ],
        )
"""
Fair Value Gap Score Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.fair_value_gap_result import FairValueGapResult
from backend.models.fair_value_gap_score import FairValueGapScore


class FairValueGapScoreEngine(AnalysisEngine):
    """
    Scores a Fair Value Gap from 0-100.
    """

    name = "Fair Value Gap Score"

    @classmethod
    def analyze(
        cls,
        fvg: FairValueGapResult,
    ) -> FairValueGapScore:

        if fvg.score <= 0:

            return FairValueGapScore(
                score=0.0,
                freshness=0.0,
                size=0.0,
                mitigation=0.0,
                trend_alignment=0.0,
                proximity=0.0,
                reasons=[
                    "No Fair Value Gap detected.",
                ],
            )

        freshness = 20.0
        size = 20.0
        mitigation = 20.0
        trend_alignment = 20.0
        proximity = 20.0

        score = (
            freshness
            + size
            + mitigation
            + trend_alignment
            + proximity
        )

        return FairValueGapScore(
            score=score,
            freshness=freshness,
            size=size,
            mitigation=mitigation,
            trend_alignment=trend_alignment,
            proximity=proximity,
            reasons=[
                "Fair Value Gap scored successfully.",
            ],
        )
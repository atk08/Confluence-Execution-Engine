"""
Fair Value Gap Score Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.fair_value_gap_result import FairValueGapResult
from backend.models.fair_value_gap_score import FairValueGapScore


class FairValueGapScoreEngine(AnalysisEngine):
    """
    Scores a Fair Value Gap setup from 0–100.
    """

    name = "Fair Value Gap Score"

    @classmethod
    def analyze(
        cls,
        gap: FairValueGapResult,
    ) -> FairValueGapScore:

        if gap.score <= 0:

            return FairValueGapScore(
                score=0.0,
                freshness=0.0,
                size=0.0,
                mitigation=0.0,
                trend_alignment=0.0,
                proximity=0.0,
                reasons=[
                    "No valid Fair Value Gap setup.",
                ],
            )

        # Freshness
        freshness = 20.0 if not gap.mitigated else 5.0

        # Gap Size
        if gap.gap_size >= 10:
            size = 20.0
        elif gap.gap_size >= 5:
            size = 15.0
        elif gap.gap_size >= 2:
            size = 10.0
        else:
            size = 5.0

        # Mitigation
        if gap.fill_percent <= 10:
            mitigation = 20.0
        elif gap.fill_percent <= 30:
            mitigation = 15.0
        elif gap.fill_percent <= 60:
            mitigation = 10.0
        else:
            mitigation = 5.0

        # Trend Alignment
        trend_alignment = (
            20.0 if (gap.bullish_gap or gap.bearish_gap) else 0.0
        )

        # Placeholder until we include current price
        proximity = 20.0

        total = (
            freshness
            + size
            + mitigation
            + trend_alignment
            + proximity
        )

        reasons = []

        if gap.bullish_gap:
            reasons.append("Bullish Fair Value Gap.")

        if gap.bearish_gap:
            reasons.append("Bearish Fair Value Gap.")

        if not gap.mitigated:
            reasons.append("Gap remains unmitigated.")

        reasons.append(
            f"Gap filled {gap.fill_percent:.1f}%."
        )

        return FairValueGapScore(
            score=min(total, 100.0),
            freshness=freshness,
            size=size,
            mitigation=mitigation,
            trend_alignment=trend_alignment,
            proximity=proximity,
            reasons=reasons,
        )
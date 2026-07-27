"""
Volume Profile Score Engine.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.volume_profile_result import VolumeProfileResult
from backend.models.volume_profile_score import VolumeProfileScore


class VolumeProfileScoreEngine(AnalysisEngine):
    """
    Scores a Volume Profile setup from 0–100.
    """

    name = "Volume Profile Score"

    @classmethod
    def analyze(
        cls,
        profile: VolumeProfileResult,
    ) -> VolumeProfileScore:

        if profile.score <= 0:

            return VolumeProfileScore(
                score=0.0,
                poc_quality=0.0,
                value_area=0.0,
                hvn_lvn=0.0,
                reaction_strength=0.0,
                confluence=0.0,
                reasons=[
                    "No valid Volume Profile setup.",
                ],
            )

        # POC quality
        poc_quality = 20.0 if profile.poc is not None else 0.0

        # Value Area quality
        value_area = (
            20.0
            if (
                profile.value_area_high is not None
                and profile.value_area_low is not None
            )
            else 0.0
        )

        # Trend alignment
        hvn_lvn = 20.0 if (profile.bullish or profile.bearish) else 0.0

        # Existing engine confidence
        reaction_strength = min(profile.score, 20.0)

        # Placeholder until integrated with AVWAP/FVG
        confluence = 20.0

        total = (
            poc_quality
            + value_area
            + hvn_lvn
            + reaction_strength
            + confluence
        )

        reasons = []

        if profile.poc is not None:
            reasons.append("Point of Control identified.")

        if (
            profile.value_area_high is not None
            and profile.value_area_low is not None
        ):
            reasons.append("Value Area identified.")

        if profile.bullish:
            reasons.append("Bullish Volume Profile.")

        if profile.bearish:
            reasons.append("Bearish Volume Profile.")

        return VolumeProfileScore(
            score=min(total, 100.0),
            poc_quality=poc_quality,
            value_area=value_area,
            hvn_lvn=hvn_lvn,
            reaction_strength=reaction_strength,
            confluence=confluence,
            reasons=reasons,
        )
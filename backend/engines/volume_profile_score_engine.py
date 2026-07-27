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

        poc_quality = 20.0
        value_area = 20.0
        hvn_lvn = 20.0
        reaction_strength = 20.0
        confluence = 20.0

        total = (
            poc_quality
            + value_area
            + hvn_lvn
            + reaction_strength
            + confluence
        )

        return VolumeProfileScore(
            score=total,
            poc_quality=poc_quality,
            value_area=value_area,
            hvn_lvn=hvn_lvn,
            reaction_strength=reaction_strength,
            confluence=confluence,
            reasons=[
                "Volume Profile scored successfully.",
            ],
        )
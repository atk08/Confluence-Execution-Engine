"""
Confluence Score Engine V2.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.avwap_score import AVWAPScore
from backend.models.confluence_score_v2 import ConfluenceScoreV2
from backend.models.fair_value_gap_score import FairValueGapScore
from backend.models.liquidity_score import LiquidityScore
from backend.models.market_structure_score import MarketStructureScore
from backend.models.order_block_score import OrderBlockScore
from backend.models.volume_profile_score import VolumeProfileScore


class ConfluenceScoreV2Engine(AnalysisEngine):
    """
    Combines all scoring engines into one weighted score.
    """

    name = "Confluence Score V2"

    @classmethod
    def analyze(
        cls,
        market: MarketStructureScore,
        volume: VolumeProfileScore,
        avwap: AVWAPScore,
        order_block: OrderBlockScore,
        fvg: FairValueGapScore,
        liquidity: LiquidityScore,
    ) -> ConfluenceScoreV2:

        market_score = market.score * 0.25
        volume_score = volume.score * 0.20
        avwap_score = avwap.score * 0.20
        order_block_score = order_block.score * 0.15
        fvg_score = fvg.score * 0.10
        liquidity_score = liquidity.score * 0.10

        total = (
            market_score
            + volume_score
            + avwap_score
            + order_block_score
            + fvg_score
            + liquidity_score
        )

        reasons = [
            "Weighted confluence score calculated.",
        ]

        if avwap.score >= 80:
            reasons.append("Strong Anchored VWAP confluence.")

        if volume.score >= 80:
            reasons.append("Strong Volume Profile confluence.")

        if fvg.score >= 80:
            reasons.append("Strong Fair Value Gap confluence.")

        if market.score >= 80:
            reasons.append("Strong market structure.")

        if liquidity.score >= 80:
            reasons.append("Liquidity supports the setup.")

        if order_block.score >= 80:
            reasons.append("Order block supports the setup.")

        return ConfluenceScoreV2(
            score=round(total, 2),
            market_structure=market_score,
            volume_profile=volume_score,
            avwap=avwap_score,
            order_block=order_block_score,
            fair_value_gap=fvg_score,
            liquidity=liquidity_score,
            reasons=reasons,
        )
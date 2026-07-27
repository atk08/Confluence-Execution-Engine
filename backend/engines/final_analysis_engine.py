"""
Final Analysis Engine.

Combines analysis context into final trading output.
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.analysis_context import AnalysisContext

from backend.models.analysis_result import AnalysisResult

from backend.engines.market_structure_score_engine import (
    MarketStructureScoreEngine,
)
from backend.engines.volume_profile_score_engine import (
    VolumeProfileScoreEngine,
)
from backend.engines.avwap_score_engine import (
    AVWAPScoreEngine,
)
from backend.engines.fair_value_gap_score_engine import (
    FairValueGapScoreEngine,
)
from backend.engines.liquidity_score_engine import (
    LiquidityScoreEngine,
)

from backend.engines.confluence_score_v2_engine import (
    ConfluenceScoreV2Engine,
)

from backend.engines.signal_engine import SignalEngine

from backend.models.order_block_score import OrderBlockScore
from backend.engines.analysis_result_engine import (
    AnalysisResultEngine,
)


class FinalAnalysisEngine(AnalysisEngine):
    """
    Produces final Confluence result.
    """

    name = "Final Analysis Engine"

    @classmethod
    def analyze(
        cls,
        context: AnalysisContext,
    ) -> AnalysisResult:

        market = MarketStructureScoreEngine.analyze(context)

        volume = VolumeProfileScoreEngine.analyze(
            context.volume_profile
        )

        avwap = AVWAPScoreEngine.analyze(
            context.avwap
        )

        fvg = FairValueGapScoreEngine.analyze(
            context.fvg
        )

        liquidity = LiquidityScoreEngine.analyze(
            context.liquidity
        )

        order_block = OrderBlockScore(
            score=0.0,
            freshness=0.0,
            displacement=0.0,
            volume=0.0,
            trend_alignment=0.0,
            proximity=0.0,
            reasons=[
                "Order block analysis not connected yet.",
            ],
        )

        confluence = ConfluenceScoreV2Engine.analyze(
            market,
            volume,
            avwap,
            order_block,
            fvg,
            liquidity,
        )

        signal = SignalEngine.analyze(
            confluence
        )

        return AnalysisResultEngine.analyze(
            symbol="UNKNOWN",
            timeframe="UNKNOWN",
            confluence=confluence,
            signal=signal,
        )
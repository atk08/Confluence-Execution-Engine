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

from backend.engines.order_block_engine import (
    OrderBlockEngine,
)

from backend.engines.order_block_score_engine import (
    OrderBlockScoreEngine,
)

from backend.engines.confluence_score_v2_engine import (
    ConfluenceScoreV2Engine,
)

from backend.engines.signal_engine import (
    SignalEngine,
)

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
        symbol: str = "UNKNOWN",
        timeframe: str = "UNKNOWN",
    ) -> AnalysisResult:

        #
        # Market Structure
        #

        market = MarketStructureScoreEngine.analyze(
            context
        )


        #
        # Volume Profile
        #

        volume = VolumeProfileScoreEngine.analyze(
            context.volume_profile
        )


        #
        # Anchored VWAP
        #

        avwap = AVWAPScoreEngine.analyze(
            context.avwap
        )


        #
        # Fair Value Gap
        #

        fvg = FairValueGapScoreEngine.analyze(
            context.fvg
        )


        #
        # Liquidity
        #

        liquidity = LiquidityScoreEngine.analyze(
            context.liquidity
        )


        #
        # Order Block
        #

        order_block_result = OrderBlockEngine.analyze(
            context
        )

        order_block = OrderBlockScoreEngine.analyze(
            order_block_result
        )


        #
        # Final Confluence Score
        #

        confluence = ConfluenceScoreV2Engine.analyze(
            market,
            volume,
            avwap,
            order_block,
            fvg,
            liquidity,
        )


        #
        # Trading Signal
        #

        signal = SignalEngine.analyze(
            confluence
        )


        #
        # Current Price
        #

        current_price = (
            context.candles[-1].close
            if context.candles
            else 0.0
        )


        #
        # Market Bias
        #

        if confluence.score >= 60:
            market_bias = "BULLISH"

        elif confluence.score <= 40:
            market_bias = "BEARISH"

        else:
            market_bias = "NEUTRAL"


        #
        # Reasons
        #

        reasons = [
            *confluence.reasons,
            *signal.reasons,
            *order_block.reasons,
        ]


        #
        # Final Response
        #

        return AnalysisResultEngine.analyze(
            symbol=symbol,
            timeframe=timeframe,
            current_price=current_price,
            market_bias=market_bias,
            confluence=confluence,
            signal=signal,
            reasons=reasons,
        )
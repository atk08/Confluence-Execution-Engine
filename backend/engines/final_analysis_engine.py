"""
Final Analysis Engine.

Combines every analysis component into the final result.
"""


from backend.core.analysis_engine import AnalysisEngine


from backend.models.trade_signal import TradeSignal


from backend.engines.market_structure_score_engine import (
    MarketStructureScoreEngine,
)

from backend.engines.volume_profile_score_engine import (
    VolumeProfileScoreEngine,
)

from backend.engines.avwap_score_engine import (
    AVWAPScoreEngine,
)

from backend.engines.order_block_engine import (
    OrderBlockEngine,
)

from backend.engines.order_block_score_engine import (
    OrderBlockScoreEngine,
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

from backend.engines.directional_bias_engine import (
    DirectionalBiasEngine,
)

from backend.engines.confidence_engine import (
    ConfidenceEngine,
)

from backend.engines.setup_quality_engine import (
    SetupQualityEngine,
)

from backend.engines.signal_engine import (
    SignalEngine,
)

from backend.engines.trade_plan_engine import (
    TradePlanEngine,
)

from backend.engines.analysis_result_engine import (
    AnalysisResultEngine,
)



class FinalAnalysisEngine(AnalysisEngine):

    name = "Final Analysis Engine"



    @classmethod
    def analyze(
        cls,
        context,
        symbol: str,
        timeframe: str,
    ):


        #
        # Component Scores
        #

        market_structure = (
            MarketStructureScoreEngine.analyze(
                context
            )
        )


        volume_profile = (
            VolumeProfileScoreEngine.analyze(
                context.volume_profile
            )
        )


        avwap = (
            AVWAPScoreEngine.analyze(
                context.avwap
            )
        )


        fair_value_gap = (
            FairValueGapScoreEngine.analyze(
                context.fvg
            )
        )


        liquidity = (
            LiquidityScoreEngine.analyze(
                context.liquidity
            )
        )



        #
        # Order Block
        #

        order_block_result = (
            OrderBlockEngine.analyze(
                context
            )
        )


        order_block = (
            OrderBlockScoreEngine.analyze(
                order_block_result
            )
        )



        #
        # Confluence
        #

        confluence = (
            ConfluenceScoreV2Engine.analyze(
                market_structure,
                volume_profile,
                avwap,
                order_block,
                fair_value_gap,
                liquidity,
            )
        )



        #
        # Directional Bias
        #

        directional_bias = (
            DirectionalBiasEngine.analyze(
                context
            )
        )



        #
        # Confidence
        #

        confidence = (
            ConfidenceEngine.analyze(
                confluence,
                directional_bias,
                context,
            )
        )



        #
        # Setup Quality
        #

        setup_quality = (
            SetupQualityEngine.analyze(
                confluence,
                confidence,
            )
        )



        #
        # Signal
        #

        signal_result = (
            SignalEngine.analyze(
                confluence,
                context,
            )
        )


        signal = TradeSignal(
            signal=signal_result.signal,
            confidence=confidence.confidence,
            confluence_score=confluence.score,
            reasons=[
                *signal_result.reasons,
            ],
        )



        #
        # Trade Plan
        #

        trade_plan = (
            TradePlanEngine.analyze(
                context,
                directional_bias.bias,
            )
        )



        #
        # Current Price
        #

        current_price = (
            context.candles[-1].close
            if context.candles
            else 0
        )



        #
        # Final Reasons
        #

        reasons = []


        reasons.extend(
            confluence.reasons
        )


        reasons.extend(
            directional_bias.reasons
        )


        reasons.extend(
            confidence.reasons
        )


        reasons.append(
            f"Setup grade: {setup_quality.grade}."
        )


        reasons.append(
            f"Confirmations: {setup_quality.confirmations_count}."
        )


        reasons.append(
            f"Missing confirmations: {setup_quality.missing_count}."
        )


        #
        # Trade Plan Reasons
        #

        reasons.extend(
            trade_plan.reasons
        )


        reasons.extend(
            order_block.reasons
        )


        reasons.extend(
            liquidity.reasons
        )



        #
        # Final Result
        #

        return AnalysisResultEngine.analyze(

            symbol=symbol,

            timeframe=timeframe,

            current_price=current_price,

            market_bias=directional_bias.bias,

            confluence=confluence,

            signal=signal,

            institutional_move=context.institutional_move,

            trade_plan=trade_plan,

            reasons=reasons,
        )
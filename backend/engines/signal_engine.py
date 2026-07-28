"""
Signal Engine V3.

Converts confluence + directional context
into BUY / SELL / WAIT decisions.
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.analysis_context import AnalysisContext

from backend.models.confluence_score_v2 import (
    ConfluenceScoreV2,
)

from backend.models.trade_signal import (
    Signal,
    TradeSignal,
)


class SignalEngine(AnalysisEngine):

    name = "Signal Engine"


    MIN_CONFLUENCE = 70.0


    @classmethod
    def analyze(
        cls,
        confluence: ConfluenceScoreV2,
        context: AnalysisContext | None = None,
    ) -> TradeSignal:


        reasons = []
        warnings = []


        #
        # Backward compatibility
        #

        if context is None:

            if confluence.score >= 80:

                return TradeSignal(
                    signal=Signal.BUY,
                    confidence=confluence.score,
                    confluence_score=confluence.score,
                    reasons=[
                        "Confluence score exceeds BUY threshold."
                    ],
                )


            if confluence.score <= 20:

                return TradeSignal(
                    signal=Signal.SELL,
                    confidence=100 - confluence.score,
                    confluence_score=confluence.score,
                    reasons=[
                        "Confluence score below SELL threshold."
                    ],
                )


            return TradeSignal(
                signal=Signal.WAIT,
                confidence=50,
                confluence_score=confluence.score,
                reasons=[
                    "Confluence score is neutral."
                ],
            )


        #
        # Gather confirmations
        #

        bullish_confirmation = False
        bearish_confirmation = False


        #
        # Liquidity
        #

        if context.liquidity:


            if context.liquidity.bullish_sweep:

                bullish_confirmation = True

                reasons.append(
                    "Bullish liquidity sweep detected."
                )


            if context.liquidity.bearish_sweep:

                bearish_confirmation = True

                reasons.append(
                    "Bearish liquidity sweep detected."
                )



        #
        # Institutional move
        #

        if context.institutional_move:


            if context.institutional_move.bullish_move:

                bullish_confirmation = True

                reasons.append(
                    "Bullish institutional move confirmed."
                )


            if context.institutional_move.bearish_move:

                bearish_confirmation = True

                reasons.append(
                    "Bearish institutional move confirmed."
                )


            if not context.institutional_move.has_bos:

                warnings.append(
                    "No BOS confirmation."
                )


            if not context.institutional_move.has_choch:

                warnings.append(
                    "No CHoCH confirmation."
                )



        #
        # Direction
        #

        bias = "NEUTRAL"


        if context.trend:

            trend_text = str(
                context.trend
            ).lower()


            if "bull" in trend_text:

                bias = "BULLISH"


            elif "bear" in trend_text:

                bias = "BEARISH"



        #
        # BUY Logic
        #

        if (
            confluence.score >= cls.MIN_CONFLUENCE
            and bias == "BULLISH"
            and bullish_confirmation
        ):

            return TradeSignal(
                signal=Signal.BUY,
                confidence=confluence.score,
                confluence_score=confluence.score,
                reasons=[
                    "Bullish bias confirmed.",
                    *reasons,
                    "Strong confluence score.",
                ],
            )



        #
        # SELL Logic
        #

        if (
            confluence.score >= cls.MIN_CONFLUENCE
            and bias == "BEARISH"
            and bearish_confirmation
        ):

            return TradeSignal(
                signal=Signal.SELL,
                confidence=confluence.score,
                confluence_score=confluence.score,
                reasons=[
                    "Bearish bias confirmed.",
                    *reasons,
                    "Strong confluence score.",
                ],
            )



        #
        # WAIT
        #

        return TradeSignal(
            signal=Signal.WAIT,
            confidence=confluence.score,
            confluence_score=confluence.score,
            reasons=[
                *reasons,
                "Directional confirmation incomplete.",
            ],
        )
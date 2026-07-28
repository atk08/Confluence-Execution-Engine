"""
Confidence Engine V4.

Calculates realistic trading confidence.

Confidence is based on:
- Confluence score
- Direction
- Liquidity
- Institutional confirmation
- BOS
- CHoCH
- FVG
- Order Block

Maximum confidence is capped at 95%.
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.analysis_context import AnalysisContext

from backend.models.confluence_score_v2 import (
    ConfluenceScoreV2,
)

from backend.models.directional_bias import (
    DirectionalBias,
)

from backend.models.confidence_result import (
    ConfidenceResult,
)


class ConfidenceEngine(AnalysisEngine):

    name = "Confidence Engine"


    MAX_CONFIDENCE = 95


    @classmethod
    def analyze(
        cls,
        confluence: ConfluenceScoreV2,
        bias: DirectionalBias,
        context: AnalysisContext,
    ) -> ConfidenceResult:


        confidence = confluence.score

        confirmations = []

        missing = []

        reasons = []


        #
        # Direction
        #

        if bias.bias != "NEUTRAL":

            confidence += 5

            confirmations.append(
                f"{bias.bias.title()} directional bias"
            )

        else:

            confidence -= 5

            missing.append(
                "Clear directional bias"
            )


        #
        # Liquidity
        #

        if context.liquidity:

            if (
                context.liquidity.bullish_sweep
                or
                context.liquidity.bearish_sweep
            ):

                confidence += 5

                confirmations.append(
                    "Liquidity sweep detected"
                )

            else:

                confidence -= 5

                missing.append(
                    "Liquidity sweep"
                )


        #
        # Institutional move
        #

        if context.institutional_move:


            if (
                context.institutional_move.bullish_move
                or
                context.institutional_move.bearish_move
            ):

                confidence += 7

                confirmations.append(
                    "Institutional move confirmed"
                )

            else:

                confidence -= 7

                missing.append(
                    "Institutional move"
                )


            #
            # BOS
            #

            if context.institutional_move.has_bos:

                confidence += 3

                confirmations.append(
                    "Break of Structure confirmed"
                )

            else:

                confidence -= 3

                missing.append(
                    "BOS confirmation"
                )


            #
            # CHoCH
            #

            if context.institutional_move.has_choch:

                confidence += 3

                confirmations.append(
                    "CHoCH confirmed"
                )

            else:

                confidence -= 3

                missing.append(
                    "CHoCH confirmation"
                )


        #
        # FVG
        #

        if context.fvg:


            if (
                context.fvg.bullish_gap
                or
                context.fvg.bearish_gap
            ):

                confidence += 3

                confirmations.append(
                    "Fair Value Gap confirmation"
                )

            else:

                confidence -= 3

                missing.append(
                    "Fair Value Gap"
                )


        #
        # Order Block
        #

        if confluence.order_block > 0:

            confidence += 3

            confirmations.append(
                "Order Block confirmation"
            )

        else:

            missing.append(
                "Order Block"
            )


        #
        # Clamp result
        #

        confidence = round(
            max(
                0,
                min(
                    cls.MAX_CONFIDENCE,
                    confidence
                )
            ),
            2,
        )


        #
        # Reasons
        #

        reasons.append(
            f"Confidence calculated at {confidence}%."
        )


        reasons.extend(
            confirmations
        )


        if missing:

            reasons.append(
                "Missing confirmations:"
            )

            reasons.extend(
                missing
            )


        return ConfidenceResult(
            confidence=confidence,
            confirmations=confirmations,
            missing=missing,
            reasons=reasons,
        )
"""
Setup Quality Engine V2.

Grades the overall quality of a trading setup.

Uses:
- Confluence score
- Strong confluence components
- Confidence confirmations
- Missing confirmations
"""

from backend.core.analysis_engine import AnalysisEngine

from backend.models.confluence_score_v2 import (
    ConfluenceScoreV2,
)

from backend.models.confidence_result import (
    ConfidenceResult,
)

from backend.models.setup_quality_result import (
    SetupQualityResult,
)


class SetupQualityEngine(AnalysisEngine):

    name = "Setup Quality Engine"


    @classmethod
    def analyze(
        cls,
        confluence: ConfluenceScoreV2,
        confidence: ConfidenceResult,
    ) -> SetupQualityResult:


        confirmations = []

        warnings = []


        #
        # Count strong confluence factors
        #

        components = 0


        if confluence.market_structure >= 10:

            components += 1

            confirmations.append(
                "Market structure alignment"
            )


        if confluence.volume_profile >= 15:

            components += 1

            confirmations.append(
                "Volume Profile confirmation"
            )


        if confluence.avwap >= 15:

            components += 1

            confirmations.append(
                "Anchored VWAP confirmation"
            )


        if confluence.order_block >= 10:

            components += 1

            confirmations.append(
                "Order Block confirmation"
            )


        if confluence.fair_value_gap >= 5:

            components += 1

            confirmations.append(
                "Fair Value Gap confirmation"
            )


        if confluence.liquidity >= 5:

            components += 1

            confirmations.append(
                "Liquidity confirmation"
            )


        #
        # Add confidence confirmations
        #

        for item in confidence.confirmations:

            if item not in confirmations:

                confirmations.append(item)


        for item in confidence.missing:

            warnings.append(item)


        #
        # Grade calculation
        #

        score = confluence.score


        if score >= 85 and components >= 5:

            grade = "A+"


        elif score >= 75 and components >= 4:

            grade = "A"


        elif score >= 65 and components >= 3:

            grade = "B"


        elif score >= 50 and components >= 2:

            grade = "C"


        else:

            grade = "D"



        return SetupQualityResult(

            grade=grade,

            confirmations_count=len(confirmations),

            missing_count=len(warnings),

            confirmations=confirmations,

            warnings=warnings,

        )
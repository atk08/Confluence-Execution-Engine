"""
Analysis Result Engine.

Combines final outputs into a single result.
"""

from backend.core.analysis_engine import AnalysisEngine
from backend.models.analysis_result import AnalysisResult


class AnalysisResultEngine(AnalysisEngine):

    name = "Analysis Result Engine"


    @classmethod
    def analyze(
        cls,
        symbol: str,
        timeframe: str,
        confluence,
        signal,
        current_price: float = 0.0,
        market_bias: str = "NEUTRAL",
        institutional_move=None,
        trade_plan=None,
        reasons=None,
    ) -> AnalysisResult:


        if reasons is None:
            reasons = []


        if confluence.score >= 70:

            summary = "Strong confluence setup detected."

        elif confluence.score >= 50:

            summary = "Setup has partial confluence."

        else:

            summary = "Setup does not have enough confluence yet."


        return AnalysisResult(

            symbol=symbol,

            timeframe=timeframe,

            current_price=current_price,

            market_bias=market_bias,

            confluence=confluence,

            signal=signal,

            institutional_move=institutional_move,

            trade_plan=trade_plan,

            summary=summary,

            reasons=reasons,
        )
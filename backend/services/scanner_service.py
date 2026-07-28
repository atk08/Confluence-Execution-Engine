"""
Scanner service.

Connects API requests to analysis engine.
"""

from backend.pipelines.analysis_pipeline import AnalysisPipeline
from backend.engines.final_analysis_engine import FinalAnalysisEngine


class ScannerService:


    @staticmethod
    def scan(
        candles,
        symbol: str,
        timeframe: str,
    ):

        context = AnalysisPipeline.run(
            candles
        )


        result = FinalAnalysisEngine.analyze(
            context=context,
            symbol=symbol,
            timeframe=timeframe,
        )


        return result
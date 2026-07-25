from backend.models.candles import Candle
from backend.pipelines.analysis_pipeline import (
    AnalysisPipeline,
)


def test_analysis_pipeline():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 102, 99, 101, 1000),
        Candle(101, 103, 100, 102, 1000),
        Candle(102, 104, 101, 103, 1000),
        Candle(103, 105, 102, 104, 1000),
    ]

    context = AnalysisPipeline.run(candles)

    assert context.structure is not None
    assert context.trend is not None
    assert context.bos is not None
    assert context.choch is not None
    assert context.liquidity is not None
    assert context.fvg is not None
from backend.engines.analysis_pipeline import AnalysisPipeline
from backend.models.candles import Candle


def test_pipeline_calculates_avwap():
    candles = [
        Candle(open=100, high=110, low=90, close=100, volume=1000),
        Candle(open=100, high=120, low=100, close=110, volume=2000),
    ]

    result = AnalysisPipeline.calculate_avwap(candles)

    assert result > 0
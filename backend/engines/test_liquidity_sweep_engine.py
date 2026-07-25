from backend.engines.liquidity_sweep_engine import (
    LiquiditySweepEngine,
)
from backend.engines.structure_engine import StructureEngine
from backend.models.candles import Candle


def test_no_liquidity_sweep():

    candles = [
        Candle(100, 100, 99, 100, 1000),
        Candle(100, 105, 99, 104, 1000),
        Candle(104, 101, 97, 99, 1000),
        Candle(99, 108, 100, 107, 1000),
        Candle(107, 104, 98, 105, 1000),
        Candle(105, 112, 101, 111, 1000),
        Candle(111, 106, 102, 108, 1000),
    ]

    result = LiquiditySweepEngine.analyze(candles)

    assert result.bullish_sweep is False
    assert result.bearish_sweep is False
    assert result.score == 0.0
    assert result.swept_level is None


def test_bullish_liquidity_sweep():

    candles = [
        Candle(100, 100, 99, 100, 1000),
        Candle(100, 105, 99, 104, 1000),
        Candle(104, 101, 97, 99, 1000),
        Candle(99, 108, 100, 107, 1000),
        Candle(107, 104, 98, 105, 1000),
        Candle(105, 112, 101, 111, 1000),
        Candle(111, 114, 106, 107, 1000),
    ]

    structure = StructureEngine.analyze(candles)

    print("\nLatest Swing High:", structure.latest_swing_high)
    print("Latest Swing Low :", structure.latest_swing_low)

    result = LiquiditySweepEngine.analyze(candles)

    print("Liquidity Result :", result)

    assert result.bullish_sweep is True
    assert result.bearish_sweep is False
    assert result.score == 1.0
    assert result.swept_level is not None
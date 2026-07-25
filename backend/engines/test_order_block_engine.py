from backend.engines.order_block_engine import OrderBlockEngine
from backend.models.candles import Candle


def test_no_order_block():

    candles = [
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 101, 99, 100, 1000),
        Candle(100, 101, 99, 100, 1000),
    ]

    result = OrderBlockEngine.analyze(candles)

    assert result.bullish_block is False
    assert result.bearish_block is False
    assert result.score == 0.0


def test_find_last_bearish_candle():

    candles = [
        Candle(100, 103, 99, 102, 1000),
        Candle(102, 103, 98, 99, 1000),     # Bearish
        Candle(99, 110, 99, 109, 3000),     # Large bullish displacement
    ]

    result = OrderBlockEngine.analyze(candles)

    assert result.bullish_block is True
    assert result.bearish_block is False
    assert result.block_high == 103
    assert result.block_low == 98
    assert result.candle_index == 1


def test_small_bullish_move_is_not_displacement():

    candles = [
        Candle(100, 103, 99, 102, 1000),
        Candle(102, 106, 98, 99, 1000),     # Large bearish body
        Candle(99, 101, 99, 100, 3000),     # Small bullish body
    ]

    result = OrderBlockEngine.analyze(candles)

    assert result.bullish_block is False
from backend.engines.change_of_character_engine import (
    ChangeOfCharacterEngine,
)
from backend.models.candles import Candle


def test_no_choch_returns_false():

    candles = [
        Candle(100, 100, 99, 100, 1000),
        Candle(100, 105, 99, 104, 1000),
        Candle(104, 101, 97, 99, 1000),
        Candle(99, 108, 100, 107, 1000),
        Candle(107, 104, 98, 105, 1000),
        Candle(105, 112, 101, 111, 1000),
        Candle(111, 106, 102, 108, 1000),
    ]

    result = ChangeOfCharacterEngine.analyze(candles)

    assert result.bullish_choch is False
    assert result.bearish_choch is False
    assert result.score == 0.0
    assert result.broken_level is None
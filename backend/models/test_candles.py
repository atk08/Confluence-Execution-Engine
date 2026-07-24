from backend.models.candles import Candle


def test_create_candle():
    candle = Candle(
        open=100,
        high=110,
        low=95,
        close=108,
        volume=1500,
    )

    assert candle.open == 100
    assert candle.high == 110
    assert candle.low == 95
    assert candle.close == 108
    assert candle.volume == 1500
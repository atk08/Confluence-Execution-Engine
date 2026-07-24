from backend.providers.binance import BinanceProvider


def test_download_candles():

    candles = BinanceProvider.get_candles(
        "BTCUSDT",
        "1h",
        10,
    )

    assert len(candles) == 10
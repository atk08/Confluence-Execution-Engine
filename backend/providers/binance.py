"""
Binance market data provider.
"""

import requests

from backend.models.candles import Candle


class BinanceProvider:
    BASE_URL = "https://api.binance.com/api/v3/klines"

    @staticmethod
    def get_candles(
        symbol: str,
        interval: str,
        limit: int = 100,
    ) -> list[Candle]:

        response = requests.get(
            BinanceProvider.BASE_URL,
            params={
                "symbol": symbol,
                "interval": interval,
                "limit": limit,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        candles = []

        for item in data:
            candles.append(
                Candle(
                    open=float(item[1]),
                    high=float(item[2]),
                    low=float(item[3]),
                    close=float(item[4]),
                    volume=float(item[5]),
                )
            )

        return candles
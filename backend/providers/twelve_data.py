"""
Twelve Data market data provider.
"""

import os

from twelvedata import TDClient

from backend.models.candles import Candle


class TwelveDataProvider:
    """
    Downloads OHLCV candles from Twelve Data.
    """

    def __init__(self):
        api_key = os.getenv("TWELVE_DATA_API_KEY")

        if not api_key:
            raise ValueError(
                "TWELVE_DATA_API_KEY environment variable is not set."
            )

        self.client = TDClient(apikey=api_key)

    def get_candles(
        self,
        symbol: str,
        interval: str,
        outputsize: int = 100,
    ) -> list[Candle]:

        ts = (
            self.client
            .time_series(
                symbol=symbol,
                interval=interval,
                outputsize=outputsize,
            )
            .as_json()
        )

        candles = []

        for row in reversed(ts):
            candles.append(
                Candle(
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=float(row.get("volume") or 0),
                )
            )

        return candles
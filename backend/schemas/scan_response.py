"""
API response schemas.
"""

from dataclasses import dataclass


@dataclass
class ScanResponse:

    symbol: str

    timeframe: str

    price: float

    bias: str

    score: float

    signal: str

    confidence: float

    summary: str

    trade_plan: object | None

    reasons: list[str]
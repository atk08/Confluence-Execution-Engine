from dataclasses import dataclass


@dataclass(frozen=True)
class DirectionalBias:

    bullish_score: float

    bearish_score: float

    bias: str

    reasons: list[str]
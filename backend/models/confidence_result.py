from dataclasses import dataclass


@dataclass(frozen=True)
class ConfidenceResult:

    confidence: float

    confirmations: list[str]

    missing: list[str]

    reasons: list[str]
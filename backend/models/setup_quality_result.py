from dataclasses import dataclass


@dataclass(frozen=True)
class SetupQualityResult:

    grade: str

    confirmations_count: int

    missing_count: int

    confirmations: list[str]

    warnings: list[str]
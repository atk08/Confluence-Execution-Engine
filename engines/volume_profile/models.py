"""
Data models for the Volume Profile Engine.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class POCQualityInput:
    volume_concentration: float
    time_at_price: float
    auction_acceptance: float
    historical_reactions: float
    session_importance: float
    structural_importance: float


@dataclass
class POCIntegrityInput:
    revisits: int
    penetration_penalty: float
    acceptance_penalty: float
    rejection_bonus: float
    freshness_bonus: float


@dataclass
class InstitutionalEvidenceObject:
    identifier: str
    evidence_type: str
    price: float

    quality: float
    reliability: float | None = None
    integrity: float | None = None

    weight: float = 1.0

    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class HVNQualityInput:
    volume_concentration: float
    time_at_price: float
    historical_reactions: float
    distance_from_poc: float
    recency: float
    session_importance: float
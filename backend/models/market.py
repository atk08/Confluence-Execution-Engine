"""
Shared market data models.

These models are used throughout the Confluence Execution Engine.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PriceLevel:
    """
    Represents a single price in the market.
    """
    price: float


@dataclass(frozen=True)
class VolumeNode:
    """
    Represents a node in a volume profile.
    """
    price: float
    volume: float


@dataclass(frozen=True)
class PointOfControl:
    """
    Represents the Point of Control (POC).
    """
    price: float
    volume: float


@dataclass(frozen=True)
class VolumeProfile:
    """
    Represents a complete market auction for a single symbol,
    timeframe, and trading session.
    """

    symbol: str
    timeframe: str
    session: str

    start_time: str
    end_time: str

    point_of_control: PointOfControl

    value_area_high: float
    value_area_low: float

    total_volume: float

    high_volume_nodes: list[VolumeNode] = field(default_factory=list)
    low_volume_nodes: list[VolumeNode] = field(default_factory=list)


@dataclass
class InstitutionalAnalysis:
    """
    Represents the complete institutional analysis of an asset.
    """

    symbol: str
    timeframe: str

    volume_profile: VolumeProfile

    poc_quality: float = 0.0
    poc_integrity: float = 0.0

    hvn_quality: float = 0.0
    lvn_quality: float = 0.0

    avwap_alignment: float = 0.0
    fvg_quality: float = 0.0

    trend_score: float = 0.0
    momentum_score: float = 0.0
    volatility_score: float = 0.0
    volume_score: float = 0.0

    institutional_confidence: float = 0.0
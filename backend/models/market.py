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
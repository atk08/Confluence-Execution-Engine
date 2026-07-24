"""
Swing point model.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SwingPoint:
    """
    Represents a confirmed swing high or swing low.
    """

    index: int
    price: float
    kind: str
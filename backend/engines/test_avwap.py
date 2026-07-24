from backend.engines.avwap import AVWAPEngine
from backend.models.market import AnchoredVWAP


def test_perfect_avwap_scores_100():
    avwap = AnchoredVWAP(
        anchor_type="swing_high",
        anchor_price=100,
        current_vwap=101,
        slope=1.5,
        respect_count=10,
        aligned_with_poc=True,
        aligned_with_hvn=True,
        aligned_with_lvn=True,
    )

    assert AVWAPEngine.calculate_score(avwap) == 100.0


def test_empty_avwap_scores_zero():
    avwap = AnchoredVWAP(
        anchor_type="swing_low",
        anchor_price=100,
        current_vwap=100,
        slope=0.0,
        respect_count=0,
        aligned_with_poc=False,
        aligned_with_hvn=False,
        aligned_with_lvn=False,
    )

    assert AVWAPEngine.calculate_score(avwap) == 0.0
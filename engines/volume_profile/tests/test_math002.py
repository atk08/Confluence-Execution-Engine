from engines.volume_profile.models import POCIntegrityInput
from engines.volume_profile.math002_poc_integrity import (
    calculate_poc_integrity,
)


def test_fresh_poc():
    data = POCIntegrityInput(
        revisits=0,
        penetration_penalty=0,
        acceptance_penalty=0,
        rejection_bonus=0,
        freshness_bonus=0,
    )

    assert calculate_poc_integrity(data) == 100.0


def test_multiple_revisits():
    data = POCIntegrityInput(
        revisits=4,
        penetration_penalty=20,
        acceptance_penalty=10,
        rejection_bonus=5,
        freshness_bonus=0,
    )

    assert calculate_poc_integrity(data) == 55.0


def test_score_never_negative():
    data = POCIntegrityInput(
        revisits=50,
        penetration_penalty=100,
        acceptance_penalty=100,
        rejection_bonus=0,
        freshness_bonus=0,
    )

    assert calculate_poc_integrity(data) == 0.0
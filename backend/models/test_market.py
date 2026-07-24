from backend.models.market import (
    PointOfControl,
    VolumeNode,
    VolumeProfile,
)


def test_create_volume_profile():

    poc = PointOfControl(
        price=118250.0,
        volume=15000.0,
    )

    profile = VolumeProfile(
        symbol="BTCUSDT",
        timeframe="5m",
        session="New York",
        start_time="2026-07-23T09:30:00",
        end_time="2026-07-23T16:00:00",
        point_of_control=poc,
        value_area_high=118400.0,
        value_area_low=118100.0,
        total_volume=250000.0,
    )

    assert profile.symbol == "BTCUSDT"
    assert profile.timeframe == "5m"
    assert profile.point_of_control.price == 118250.0
    assert profile.total_volume == 250000.0
    assert profile.high_volume_nodes == []
    assert profile.low_volume_nodes == []


def test_volume_profile_with_nodes():

    poc = PointOfControl(
        price=118250.0,
        volume=15000.0,
    )

    hvn = VolumeNode(
        price=118300.0,
        volume=8000.0,
    )

    lvn = VolumeNode(
        price=118175.0,
        volume=1200.0,
    )

    profile = VolumeProfile(
        symbol="BTCUSDT",
        timeframe="5m",
        session="New York",
        start_time="2026-07-23T09:30:00",
        end_time="2026-07-23T16:00:00",
        point_of_control=poc,
        value_area_high=118400.0,
        value_area_low=118100.0,
        total_volume=250000.0,
        high_volume_nodes=[hvn],
        low_volume_nodes=[lvn],
    )

    assert len(profile.high_volume_nodes) == 1
    assert len(profile.low_volume_nodes) == 1
    assert profile.high_volume_nodes[0].price == 118300.0
    assert profile.low_volume_nodes[0].price == 118175.0
from backend.models.market import (
    InstitutionalAnalysis,
    PointOfControl,
    VolumeProfile,
)


def test_create_institutional_analysis():

    poc = PointOfControl(
        price=118250.0,
        volume=15000.0,
    )

    profile = VolumeProfile(
        symbol="BTCUSDT",
        timeframe="5m",
        session="New York",
        start_time="2026-07-23T09:30:00",
        end_time="2026-07-23T16:00:00",
        point_of_control=poc,
        value_area_high=118400.0,
        value_area_low=118100.0,
        total_volume=250000.0,
    )

    analysis = InstitutionalAnalysis(
        symbol="BTCUSDT",
        timeframe="5m",
        volume_profile=profile,
    )

    assert analysis.symbol == "BTCUSDT"
    assert analysis.timeframe == "5m"
    assert analysis.volume_profile.point_of_control.price == 118250.0

    assert analysis.poc_quality == 0.0
    assert analysis.poc_integrity == 0.0
    assert analysis.hvn_quality == 0.0
    assert analysis.lvn_quality == 0.0
    assert analysis.institutional_confidence == 0.0

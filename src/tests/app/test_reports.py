from app import ReportKiu
from tests.utils import create_trip_detail_random


def test_daily_report_kiu(session):
    trip_detail = create_trip_detail_random(session)
    departure_date = trip_detail.trip.departure_date.date()
    msg = ReportKiu(session).daily_report(departure_date.strftime("%Y-%m-%d"))
    assert f"Total Packages: {trip_detail.package_quantity}" in msg


def test_daily_report_kiu_invalid_date(session):
    create_trip_detail_random(session)
    msg = ReportKiu(session).daily_report("2022-02-01")
    assert "Total Packages: 0" in msg

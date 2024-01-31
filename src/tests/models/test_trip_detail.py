from models import TripDetail
from tests.utils import create_trip_detail_random


def test_create_trip_detail(session):
    trip_detail = create_trip_detail_random(session)
    assert trip_detail.id


def test_get_trip_detail(session):
    trip_detail = create_trip_detail_random(session)

    trip_detail_get = (
        session.query(TripDetail)
        .filter_by(
            client_id=trip_detail.client_id,
            trip_id=trip_detail.trip_id,
        )
        .first()
    )

    assert trip_detail_get.id

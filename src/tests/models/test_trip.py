from models import Trip
from tests.utils import create_trip_random


def test_create_trip(session):
    trip = create_trip_random(session)
    assert trip.plane
    assert trip.airport_from
    assert trip.airport_to


def test_get_trip(session):
    trip = create_trip_random(session)

    trip_get = (
        session.query(Trip)
        .filter_by(
            plane_id=trip.plane_id,
            airport_from_id=trip.airport_from_id,
            airport_to_id=trip.airport_to_id,
        )
        .first()
    )

    assert trip_get.id

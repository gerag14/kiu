from datetime import datetime

from app import TripManager
from schemas import TripDetailSchema, TripSchema


def test_trip_manager_create_new_trip(session):
    date_str = "2022-01-01"
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    new_trip = TripSchema(
        plane_id=1,
        airport_from_id=1,
        airport_to_id=2,
        departure_date=date_obj,
        arrive_date=date_obj,
        trip_detail=[TripDetailSchema(client_id=1, package_quantity=1)],
    )

    new_trip = TripManager(session).create_new_trip(new_trip=new_trip)
    assert new_trip
    assert new_trip.id

import random
import string

from sqlalchemy import func

from models import Airport, Client, Plane, Trip, TripDetail


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))  # noqa


def random_int(minimo=9, maximo=111):
    return random.randint(minimo, maximo)  # noqa


def create_airport_random(session):
    airport = Airport(name=random_lower_string())
    session.add(airport)
    session.commit()
    session.refresh(airport)
    return airport


def create_client_random(session):
    client = Client(username=random_lower_string())
    session.add(client)
    session.commit()
    session.refresh(client)
    return client


def create_plane_random(session):
    plane = Plane(code=random_lower_string())
    session.add(plane)
    session.commit()
    session.refresh(plane)
    return plane


def create_trip_random(session):
    airport_from = create_airport_random(session)
    airport_to = create_airport_random(session)
    plane = create_plane_random(session)
    departure_date = func.now()

    trip = Trip(
        plane=plane,
        airport_from=airport_from,
        airport_to=airport_to,
        departure_date=departure_date,
    )
    session.add(trip)
    session.commit()
    session.refresh(trip)
    return trip


def create_trip_detail_random(session):
    client = create_client_random(session)
    trip = create_trip_random(session)
    package_quantity = random_int()

    trip_detail = TripDetail(
        client=client, trip=trip, package_quantity=package_quantity
    )
    session.add(trip_detail)
    session.commit()
    session.refresh(trip_detail)
    return trip_detail

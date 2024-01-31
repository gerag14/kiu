from models import Airport
from tests.utils import create_airport_random


def test_create_airport(session):
    airport = create_airport_random(session)
    assert airport.name


def test_get_airport(session):
    airport = create_airport_random(session)

    airport_get = session.query(Airport).filter_by(name=airport.name).first()

    assert airport_get.id
    assert airport_get.name == airport.name

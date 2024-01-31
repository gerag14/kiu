from models import Plane
from tests.utils import create_plane_random


def test_create_plane(session):
    plane = create_plane_random(session)
    assert plane.code


def test_get_plane(session):
    plane = create_plane_random(session)

    plane_get = session.query(Plane).filter_by(code=plane.code).first()

    assert plane_get.id
    assert plane_get.code == plane.code

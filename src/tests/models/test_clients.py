from models import Client
from tests.utils import create_client_random


def test_create_client(session):
    client = create_client_random(session)
    assert client.username


def test_get_user(session):
    client = create_client_random(session)

    client_get = session.query(Client).filter_by(username=client.username).first()

    assert client_get.id
    assert client_get.username == client.username

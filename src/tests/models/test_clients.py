from models import Client


def test_create_user(session):
    client = Client(username="Username create test")
    session.add(client)
    session.commit()


def test_get_user(session):
    username = "Username get test"

    client = Client(username=username)
    session.add(client)
    session.commit()

    client_get = session.query(Client).filter_by(username=username).first()

    assert client_get.id
    assert client_get.username == username

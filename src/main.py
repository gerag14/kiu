from app import KiuChallenge
from db import session as Session


def run_kiu():
    session = Session()
    KiuChallenge(session).run()


if __name__ == "__main__":
    run_kiu()

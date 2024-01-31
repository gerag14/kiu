from sqlalchemy import Column, DateTime, Integer, create_engine, func
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

from config import settings

Base = declarative_base()


def connect():
    DATABASE_URL = settings.DATABASE_URL

    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()


class BaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"

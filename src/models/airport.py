from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db import BaseModel


class Airport(BaseModel):
    name = Column(String, unique=True, nullable=False)
    # TODO: add location, country, etc.
    trips_from = relationship(
        "Trip", foreign_keys="Trip.airport_from_id", back_populates="airport_from"
    )
    trips_to = relationship(
        "Trip", foreign_keys="Trip.airport_to_id", back_populates="airport_to"
    )

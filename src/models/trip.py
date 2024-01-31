from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from db import BaseModel


class Trip(BaseModel):
    plane_id = Column(Integer, ForeignKey("plane.id"), nullable=False)
    airport_from_id = Column(Integer, ForeignKey("airport.id"), nullable=False)
    airport_to_id = Column(Integer, ForeignKey("airport.id"), nullable=False)

    plane = relationship("Plane", back_populates="trips")
    airport_from = relationship(
        "Airport", foreign_keys=[airport_from_id], back_populates="trips_from"
    )
    airport_to = relationship(
        "Airport", foreign_keys=[airport_to_id], back_populates="trips_to"
    )

    trip_detail = relationship("TripDetail", back_populates="trip")

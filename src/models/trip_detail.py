from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from db import BaseModel


class TripDetail(BaseModel):
    trip_id = Column(Integer, ForeignKey("trip.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    package_quantity = Column(Integer)
    package_price = Column(Numeric(precision=10, scale=2), default=10, nullable=False)

    trip = relationship("Trip", back_populates="trip_detail")
    client = relationship("Client", back_populates="trips_detail")

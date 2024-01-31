from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db import BaseModel


class Client(BaseModel):
    username = Column(String, unique=True, nullable=False)

    trips_detail = relationship("TripDetail", back_populates="client")

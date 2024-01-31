from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db import BaseModel


class Plane(BaseModel):
    code = Column(String, unique=True, nullable=False)
    trips = relationship("Trip", back_populates="plane")

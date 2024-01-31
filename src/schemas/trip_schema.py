from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class TripDetailSchema:
    client_id: int
    package_quantity: int
    package_price: Optional[float] = 10


@dataclass
class TripSchema:
    plane_id: int
    airport_from_id: int
    airport_to_id: int
    departure_date: datetime
    arrive_date: Optional[datetime] = None
    trip_detail: List[TripDetailSchema] = field(default_factory=list)

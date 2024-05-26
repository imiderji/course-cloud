from pydantic import BaseModel, ConfigDict
from typing import Optional

class TripBase(BaseModel):
    lot_id: Optional[int]
    route_id: Optional[int]
    trip_name: Optional[str]
    trip_active: Optional[bool]

class Trip(TripBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class TripCreate(TripBase):
    pass

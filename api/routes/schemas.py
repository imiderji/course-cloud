from pydantic import BaseModel, ConfigDict
from typing import Optional

class RouteBase(BaseModel):
    route_id: Optional[int]
    route_name: Optional[str]
    route_short_name: Optional[str]
    route_active: Optional[bool]
    route_type_id: Optional[int]
    route_type_name: Optional[str]
    route_travel_time: Optional[int]
    route_color: Optional[str]

class Route(RouteBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class RouteCreate(RouteBase):
    pass

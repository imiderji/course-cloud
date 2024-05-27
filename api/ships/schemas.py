from pydantic import BaseModel, ConfigDict
from typing import Optional

class ShipBase(BaseModel):
    ship_id: Optional[int]
    ship_name: Optional[str]
    ship_class: Optional[str]
    ship_num: Optional[str]
    ship_capacity: Optional[int]
    ship_description: Optional[str]
    ship_model: Optional[str]
    shipowner_id: Optional[int]


class Ship(ShipBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class ShipCreate(ShipBase):
    pass
from pydantic import BaseModel, ConfigDict

class ShipBase(BaseModel):
    ship_id: int
    ship_name: str
    ship_class: str
    ship_num: str
    ship_capacity: int
    ship_description: str
    ship_model: str
    shipowner_id: int


class Ship(ShipBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class ShipCreate(BaseModel):
    pass
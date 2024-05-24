from pydantic import BaseModel, ConfigDict

class ShipownerBase(BaseModel):
    shipowner_id: int
    shipowner_name: str
    shipowner_inn: int
    shipowner_ogrn: int
    shipowner_contacts: str
    shipowner_url: str


class Shipowner(ShipownerBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class ShipownerCreate(BaseModel):
    pass
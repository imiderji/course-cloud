from pydantic import BaseModel, ConfigDict
from typing import Optional

class ShipownerBase(BaseModel):
    shipowner_id: Optional[int]
    shipowner_name: Optional[str]
    shipowner_inn: Optional[str]
    shipowner_ogrn: Optional[str]
    shipowner_contacts: Optional[str]
    shipowner_url: Optional[str]


class Shipowner(ShipownerBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class ShipownerCreate(ShipownerBase):
    pass
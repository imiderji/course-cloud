from pydantic import BaseModel, ConfigDict
from typing import Optional

class LotBase(BaseModel):
    lot_id: Optional[int]
    route_id: Optional[int]
    lot_name: Optional[str]
    lot_active: Optional[bool]

class Lot(LotBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

class LotCreate(LotBase):
    pass

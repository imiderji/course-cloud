from pydantic import BaseModel, ConfigDict
from typing import Optional


class BerthBase(BaseModel):
    berth_id: Optional[int]
    berth_number: Optional[int]
    berth_letter: Optional[str]


class Berth(BerthBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class BerthCreate(BerthBase):
    pass
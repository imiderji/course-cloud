from pydantic import BaseModel, ConfigDict
from typing import Optional

class RelationDockBerthBase(BaseModel):
    dock_id: Optional[int]
    berth_id: Optional[int] 


class RelationDockBerth(RelationDockBerthBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class RelationDockBerthCreate(RelationDockBerthBase):
    pass
from pydantic import BaseModel, ConfigDict

class RelationDockBerthBase(BaseModel):
    dock_id: int
    berth_id: int 


class RelationDockBerth(RelationDockBerthBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class RelationDockBerthCreate(BaseModel):
    pass
from pydantic import BaseModel, ConfigDict


class BerthBase(BaseModel):
    berth_id: int
    berth_name: str
    berth_letter: str


class Berth(BerthBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class BerthCreate(BaseModel):
    pass


class BerthUpdate(BerthCreate):
    pass
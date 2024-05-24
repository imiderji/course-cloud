from pydantic import BaseModel, ConfigDict
import datetime

class DockBase(BaseModel):
    dock_id: int
    dock_name: str
    berth_count: int
    dock_address: str
    dock_type: str
    exploitation: str
    department: str
    work_start_time: datetime.time
    work_end_time: datetime.time
    dock_description: str
    long: float
    lat: float


class Dock(DockBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class DockCreate(BaseModel):
    pass
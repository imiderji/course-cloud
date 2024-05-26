from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import time

class DockBase(BaseModel):
    dock_id: Optional[int]
    dock_name: Optional[str]
    berth_count: Optional[int]
    dock_address: Optional[str]
    dock_type: Optional[str]
    exploitation: Optional[str]
    department: Optional[str]
    work_start_time: Optional[time]
    work_end_time: Optional[time]
    dock_description: Optional[str]
    long: Optional[float]
    lat: Optional[float]


class Dock(DockBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int


class DockCreate(DockBase):
    pass
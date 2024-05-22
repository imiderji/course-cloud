import datetime
from sqlalchemy.orm import Mapped, relationship
from .base import Base
from .relation_dock_berth import RelationDockBerth


class Dock(Base):
    __tablename__ = "docks"

    dock_id: Mapped[int]
    dock_name: Mapped[str]
    berth_count: Mapped[int]
    dock_address: Mapped[str]
    dock_type: Mapped[str]
    exploitation: Mapped[str]
    department: Mapped[str]
    work_start_time: Mapped[datetime.time]
    work_end_time: Mapped[datetime.time]
    dock_description: Mapped[str]
    long: Mapped[float]
    lat: Mapped[float]

    relations_docks_berths: Mapped[list["RelationDockBerth"]] = relationship("RelationDockBerth", back_populates="relation_docks_berths")

    def __repr__(self) -> str:
        return (
            f"Dock("
            f"dock_id={self.dock_id!r}, "
            f"dock_name={self.dock_name!r}, "
            f"berth_count={self.berth_count!r}, "
            f"dock_address={self.dock_address!r}, "
            f"dock_type={self.dock_type!r}, "
            f"exploitation={self.exploitation!r}, "
            f"department={self.department!r}, "
            f"work_start_time={self.work_start_time!r}, "
            f"work_end_time={self.work_end_time!r}, "
            f"dock_description={self.dock_description!r}, "
            f"long={self.long!r}, "
            f"lat={self.lat!r})"
        )

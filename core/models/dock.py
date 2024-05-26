import datetime
from sqlalchemy.orm import Mapped, relationship, mapped_column
from .base import Base


class Dock(Base):
    __tablename__ = "docks"

    dock_id: Mapped[int] = mapped_column(nullable=True, unique=True)
    dock_name: Mapped[str] = mapped_column(nullable=True)
    berth_count: Mapped[int] = mapped_column(nullable=True)
    dock_address: Mapped[str] = mapped_column(nullable=True)
    dock_type: Mapped[str] = mapped_column(nullable=True)
    exploitation: Mapped[str] = mapped_column(nullable=True)
    department: Mapped[str] = mapped_column(nullable=True)
    work_start_time: Mapped[datetime.time] = mapped_column(nullable=True)
    work_end_time: Mapped[datetime.time] = mapped_column(nullable=True)
    dock_description: Mapped[str] = mapped_column(nullable=True)
    long: Mapped[float] = mapped_column(nullable=True)
    lat: Mapped[float] = mapped_column(nullable=True)

    relations_docks_berths = relationship("RelationDockBerth", back_populates="dock")

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

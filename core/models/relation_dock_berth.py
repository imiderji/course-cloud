from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from .dock import Dock
from .berth import Berth


class RelationDockBerth(Base):
    __tablename__ = "relations_docks_berths"

    dock_id: Mapped[int] = mapped_column(ForeignKey('docks.dock_id'))
    berth_id: Mapped[int] = mapped_column(ForeignKey('berths.berth_id'))

    dock: Mapped["Dock"] = relationship("Dock", back_populates="docks")
    berth: Mapped["Berth"] = relationship("Berth", back_populates="berths")

    def __repr__(self) -> str:
        return (
            f"RelationDockBerth("
            f"dock_id={self.dock_id!r}, "
            f"berth_id={self.berth_id!r})"
        )
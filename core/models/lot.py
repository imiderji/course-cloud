from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Lot(Base):
    __tablename__ = "lots"

    lot_id: Mapped[int] = mapped_column(nullable=True, unique=True)
    route_id: Mapped[int] = mapped_column(ForeignKey('routes.route_id'))
    lot_name: Mapped[str] = mapped_column(nullable=True)
    lot_active: Mapped[bool] = mapped_column(nullable=True)
    
    route = relationship("Route", back_populates="lots")
    trips = relationship("Trip", back_populates="lot")

    def __repr__(self) -> str:
        return (
            f"Lot("
            f"lot_id={self.lot_id!r}, "
            f"route_id={self.route_id!r}, "
            f"lot_name={self.lot_name!r}, "
            f"lot_active={self.lot_active!r})"
        )
    
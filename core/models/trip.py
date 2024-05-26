from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import ForeignKey

class Routes(Base):
    __tablename__ = "trip"

    lot_id: Mapped[int] = mapped_column(ForeignKey('lot.id'))
    route_id: Mapped[int] = mapped_column(ForeignKey('route.id'))
    trip_name: Mapped[str] = mapped_column(nullable=True)
    trip_active: Mapped[bool] = mapped_column(nullable=True)

    lot = relationship("Lot", back_populates="trips")
    route = relationship("Route", back_populates="trips")

    def __repr__(self) -> str:
        return (
            f"Trip("
            f"lot_id={self.lot_id!r}, "
            f"route_id={self.route_id!r}, "
            f"trip_name={self.trip_name!r}, "
            f"trip_active={self.trip_active!r})"
        )
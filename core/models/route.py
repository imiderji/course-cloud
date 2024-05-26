from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Route(Base):
    __tablename__ = "route"

    route_name: Mapped[str] = mapped_column(nullable=True)
    route_short_name: Mapped[str] = mapped_column(nullable=True)
    route_active: Mapped[bool] = mapped_column(nullable=True)
    route_type_id: Mapped[int] = mapped_column(nullable=True)
    route_type_name: Mapped[str] = mapped_column(nullable=True)
    route_travel_time: Mapped[int] = mapped_column(nullable=True)
    route_color: Mapped[str] = mapped_column(nullable=True)
    
    lots = relationship("Lot", back_populates="route")
    trips = relationship("Trip", back_populates="route")

    def __repr__(self) -> str:
        return (
            f"Route("
            f"route_name={self.route_name!r}, "
            f"route_short_name={self.route_short_name!r}, "
            f"route_active={self.route_active!r}, "
            f"route_type_id={self.route_type_id!r}, "
            f"route_type_name={self.route_type_name!r}, "
            f"route_travel_time={self.route_travel_time!r}, "
            f"route_color={self.route_color!r})"
        )
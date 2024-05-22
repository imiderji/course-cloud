from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Ship(Base):
    __tablename__ = "ships"

    ship_id: Mapped[int] = mapped_column(nullable=True)
    ship_name: Mapped[str] = mapped_column(nullable=True)
    ship_class: Mapped[str] = mapped_column(nullable=True)
    ship_num: Mapped[str] = mapped_column(nullable=True)
    ship_capacity: Mapped[int] = mapped_column(nullable=True)
    ship_description: Mapped[str] = mapped_column(nullable=True)
    ship_model: Mapped[str] = mapped_column(nullable=True)
    shipowner_id: Mapped[int] = mapped_column(ForeignKey('shipowners.id'))

    shipowner = relationship("Shipowner", back_populates="ships")

    def __repr__(self) -> str:
        return (
            f"Ship("
            f"ship_id={self.ship_id!r}, "
            f"ship_name={self.ship_name!r}, "
            f"ship_class={self.ship_class!r}, "
            f"ship_num={self.ship_num!r}, "
            f"ship_capacity={self.ship_capacity!r}, "
            f"ship_description={self.ship_description!r}, "
            f"ship_model={self.ship_model!r}, "
            f"shipowner_id={self.shipowner_id!r})"
        )
    
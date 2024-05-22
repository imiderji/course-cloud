from sqlalchemy.orm import Mapped, relationship
from .base import Base
from .ship import Ship


class Shipowner(Base):
    __tablename__ = "shipowners"

    shipowner_id: Mapped[int]
    shipowner_name: Mapped[str]
    shipowner_inn: Mapped[int]
    shipowner_ogrn: Mapped[int]
    shipowner_contacts: Mapped[str]
    shipowner_url: Mapped[str]

    ships: Mapped[list["Ship"]] = relationship("Ship", back_populates="shipowner")

    def __repr__(self) -> str:
        return (
            f"Shipowner("
            f"shipowner_id={self.shipowner_id!r}, "
            f"shipowner_name={self.shipowner_name!r}, "
            f"shipowner_inn={self.shipowner_inn!r}, "
            f"shipowner_ogrn={self.shipowner_ogrn!r}, "
            f"shipowner_contacts={self.shipowner_contacts!r}, "
            f"shipowner_url={self.shipowner_url!r})"
        )
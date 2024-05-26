from sqlalchemy.orm import Mapped, relationship, mapped_column
from .base import Base


class Shipowner(Base):
    __tablename__ = "shipowners"

    shipowner_id: Mapped[int] = mapped_column(nullable=True)
    shipowner_name: Mapped[str] = mapped_column(nullable=True)
    shipowner_inn: Mapped[str] = mapped_column(nullable=True)
    shipowner_ogrn: Mapped[str] = mapped_column(nullable=True)
    shipowner_contacts: Mapped[str] = mapped_column(nullable=True)
    shipowner_url: Mapped[str] = mapped_column(nullable=True)

    ships = relationship("Ship", back_populates="shipowner")

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
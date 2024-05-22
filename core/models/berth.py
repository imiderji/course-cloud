from sqlalchemy.orm import Mapped, relationship, mapped_column
from .base import Base


class Berth(Base):
    __tablename__ = "berths"

    berth_id: Mapped[int] = mapped_column(nullable=True)
    berth_name: Mapped[str] = mapped_column(nullable=True)
    berth_letter: Mapped[str] = mapped_column(nullable=True)

    relations_docks_berths = relationship("RelationsDockBerth", back_populates="berth")

    def __repr__(self) -> str:
        return (
                f"Berth("
                f"berth_id={self.berth_id!r}, " 
                f"berth_name={self.berth_name!r}, "
                f"berth_letter={self.berth_letter!r})"
            )
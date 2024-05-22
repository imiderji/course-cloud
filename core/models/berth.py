from sqlalchemy.orm import Mapped
from .base import Base


class Berth(Base):
    __tablename__ = "berths"

    berth_id: Mapped[int]
    berth_name: Mapped[str]
    berth_letter: Mapped[str]

    def __repr__(self) -> str:
        return (
                f"Berth("
                f"berth_id={self.berth_id!r}, " 
                f"berth_name={self.berth_name!r}, "
                f"berth_letter={self.berth_letter!r})"
            )
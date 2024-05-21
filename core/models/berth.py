from sqlalchemy.orm import Mapped
from .base import Base


class Berth(Base):
    berth_id: Mapped[int]
    berth_name: Mapped[str]
    berth_letter: Mapped[str]
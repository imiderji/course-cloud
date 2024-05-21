from sqlalchemy.orm import Mapped
from .base import Base


class Shipowner(Base):
    shipowner_id: Mapped[int]
    shipowner_name: Mapped[str]
    shipowner_inn: Mapped[int]
    shipowner_ogrn: Mapped[int]
    shipowner_contacts: Mapped[str]
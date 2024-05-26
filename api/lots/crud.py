from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from core.models import Lot
from .schemas import LotCreate

def get_lots(session: Session) -> list[Lot]:
    statement = select(Lot).order_by(Lot.id)
    result: Result = session.execute(statement)
    lots = result.scalars().all()
    return lots

def get_lot_columns() -> list[str]:
    return Lot.__table__.columns.keys()

def create_lot(session: Session, lot_in: LotCreate) -> Lot:
    lot = Lot(**lot_in.model_dump())
    session.add(lot)
    session.commit()
    return lot

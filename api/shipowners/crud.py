from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from core.models import Shipowner

from .schemas import ShipownerCreate


def get_shipowners(session: Session) -> list[Shipowner]:
    statement = select(Shipowner).order_by(Shipowner.id)
    result: Result = session.execute(statement)
    shipowners = result.scalars().all()
    return shipowners

def get_shipowners_columns() -> list[str]:
    return Shipowner.__table__.columns.keys()

def create_dock(session: Session, shipowners_in: ShipownerCreate) -> Shipowner:
    Shipowner = Shipowner(**shipowners_in.model_dump())
    session.add(Shipowner)
    session.commit()
    return Shipowner
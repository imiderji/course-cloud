from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from core.models import Dock

from .schemas import DockCreate


def get_docks(session: Session) -> list[Dock]:
    statement = select(Dock).order_by(Dock.id)
    result: Result = session.execute(statement)
    docks = result.scalars().all()
    return docks

def get_dock_columns() -> list[str]:
    return Dock.__table__.columns.keys()

def create_dock(session: Session, dock_in: DockCreate) -> Dock:
    Dock = Dock(**dock_in.model_dump())
    session.add(Dock)
    session.commit()
    return Dock
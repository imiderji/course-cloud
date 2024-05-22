from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from core.models import Berth

from .schemas import BerthCreate, BerthUpdate


def get_berths(session: Session) -> list[Berth]:
    statement = select(Berth).order_by(Berth.id)
    result: Result = session.execute(statement)
    berths = result.scalars().all()
    return list(berths)


def get_berth_by_note_id(session: Session, note_id: int) -> Berth | None:
    return session.get(Berth, note_id)


def get_berth_by_berth_id(session: Session, berth_id: int) -> Berth | None:
    return session.get(Berth, berth_id)


def get_berth_by_berth_name(session: Session, berth_name: str) -> Berth | None:
    return session.get(Berth, berth_name)


def get_berth_by_berth_letter(session: Session, berth_letter: str) -> Berth | None:
    return session.get(Berth, berth_letter)


def create_berth(session: Session, berth_in: BerthCreate) -> Berth:
    berth = Berth(**berth_in.model_dump())
    session.add(berth)
    session.commit()
    return berth
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from core.models import Berth

from .schemas import BerthCreate


def get_berths(session: Session) -> list[Berth]:
    statement = select(Berth).order_by(Berth.id)
    result: Result = session.execute(statement)
    berths = result.scalars().all()
    return berths


def get_berth_columns() -> list[str]:
    return Berth.__table__.columns.keys()



def create_berth(session: Session, berth_in: BerthCreate) -> Berth:
    berth = Berth(**berth_in.model_dump())
    session.add(berth)
    session.commit()
    return berth
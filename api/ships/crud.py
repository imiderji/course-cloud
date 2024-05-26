from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from core.models import Ship

from .schemas import ShipCreate


def get_ships(session: Session) -> list[Ship]:
    statement = select(Ship).order_by(Ship.id)
    result: Result = session.execute(statement)
    ships = result.scalars().all()
    return ships


def get_ships_columns() -> list[str]:
    return Ship.__table__.columns.keys()


def create_ship(session: Session, ships_in: ShipCreate) -> Ship:
    Ship = Ship(**ships_in.model_dump())
    session.add(Ship)
    session.commit()
    return Ship
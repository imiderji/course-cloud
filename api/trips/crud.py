from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from core.models import Trip
from .schemas import TripCreate

def get_trips(session: Session) -> list[Trip]:
    statement = select(Trip).order_by(Trip.id)
    result: Result = session.execute(statement)
    trips = result.scalars().all()
    return trips

def get_trip_columns() -> list[str]:
    return Trip.__table__.columns.keys()

def create_trip(session: Session, trip_in: TripCreate) -> Trip:
    trip = Trip(**trip_in.model_dump())
    session.add(trip)
    session.commit()
    return trip

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from core.models import RelationDockBerth

from .schemas import RelationDockBerthCreate


def get_relations_dock_berth(session: Session) -> list[RelationDockBerth]:
    statement = select(RelationDockBerth).order_by(RelationDockBerth.id)
    result: Result = session.execute(statement)
    relations_dock_berth = result.scalars().all()
    return relations_dock_berth

def get_relations_dock_berth_columns() -> list[str]:
    return RelationDockBerth.__table__.columns.keys()

def create_dock(session: Session, relation_dock_berth_in: RelationDockBerthCreate) -> RelationDockBerth:
    RelationDockBerth = RelationDockBerth(**relation_dock_berth_in.model_dump())
    session.add(RelationDockBerth)
    session.commit()
    return RelationDockBerth
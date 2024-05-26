from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from core.models import Route
from .schemas import RouteCreate

def get_routes(session: Session) -> list[Route]:
    statement = select(Route).order_by(Route.id)
    result: Result = session.execute(statement)
    routes = result.scalars().all()
    return routes

def get_route_columns() -> list[str]:
    return Route.__table__.columns.keys()

def create_route(session: Session, route_in: RouteCreate) -> Route:
    route = Route(**route_in.model_dump())
    session.add(route)
    session.commit()
    return route

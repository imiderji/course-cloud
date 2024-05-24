from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from core.config import settings


class DatabaseWork:
    def __init__(self, url: str):
        self.engine = create_engine(
            url=url,
        )
        self.session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_session(self):
        session = scoped_session(
            session_factory=self.session_factory,
        )
        return session


db_work = DatabaseWork(url=settings.db_url)

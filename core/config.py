from os import getenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = getenv("DB_URL")


settings = Settings()

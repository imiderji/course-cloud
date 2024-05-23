from os import getenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = getenv("DB_URL")
    tg_token: str = getenv("TG_TOKEN")


settings = Settings()

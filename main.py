import asyncio
from core.models import Base, db_work
from bot.bot import bot_poller


def init_db():
    with db_work.engine.begin() as conn:
        Base.metadata.create_all(bind=conn)


def main():
    # init_db()
    asyncio.run(bot_poller())


if __name__ == "__main__":
    main()
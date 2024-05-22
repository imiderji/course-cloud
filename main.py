from core.models import Base, db_work


def init_db():
    with db_work.engine.begin() as conn:
        Base.metadata.create_all(bind=conn)


def main():
    init_db()


if __name__ == "__main__":
    main()
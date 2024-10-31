from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "sqlite:///db.sqlite"

engine = create_engine(DATABASE_URL, echo=True)


def initdb():
    SQLModel.metadata.create_all(engine)


async def getsession():
    with Session(engine) as session:
        yield session

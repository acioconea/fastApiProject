from sqlalchemy.orm import Session
from sqlmodel import SQLModel, create_engine, Field, select

from db_model.config import settings


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


print(settings.DATABASE_URL)
engine = create_engine(settings.DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session


# Initialize the database and create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def insert_hero(hero:Hero,db:Session):
    db.add(hero)
    db.commit()
    db.refresh(hero)
    return hero

def get_heros_db(db:Session):
    query = select(Hero)
    heros=db.execute(query).fetchall()
    db.commit()
    return heros
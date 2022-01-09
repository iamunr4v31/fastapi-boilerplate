from sqlmodel import create_engine, Session, SQLModel
from app.config import DevConfig


engine = create_engine(f"{DevConfig.DATABASE}:///{DevConfig.DATABASE_URI}", **DevConfig.SQLALCHEMY_ENGINE_OPTIONS)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
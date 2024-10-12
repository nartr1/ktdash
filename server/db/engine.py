from typing import Annotated

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.settings import SETTINGS
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select

engine = create_engine(url=SETTINGS.db_url,echo=True)
Base = declarative_base()


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
SQLModel.metadata.create_all(engine)
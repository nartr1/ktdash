from typing import Annotated

from fastapi import Depends
from models.settings import SETTINGS
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import Session, SQLModel, create_engine

engine = create_engine(
    url=SETTINGS.db_url, echo=True, connect_args={"connect_timeout": 10}
)
Base = declarative_base()


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
SQLModel.metadata.create_all(engine)

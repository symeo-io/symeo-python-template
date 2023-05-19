from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.bootstrap.configuration import configuration


@contextmanager
def get_connection_session() -> Generator:
    engine = create_engine(configuration.DATABASE_URL)
    connection: sessionmaker[Session] = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    try:
        yield connection()
    finally:
        connection().close()

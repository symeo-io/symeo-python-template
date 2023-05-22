from contextlib import contextmanager
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


@contextmanager
def get_connection_session(connection_url: str) -> Generator:
    engine = create_engine(connection_url)
    connection: sessionmaker[Session] = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    try:
        yield connection()
    finally:
        connection().close()

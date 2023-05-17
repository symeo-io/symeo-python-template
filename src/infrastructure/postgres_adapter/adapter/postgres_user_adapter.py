from contextlib import contextmanager
from typing import Generator, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.bootstrap.configuration import configuration
from src.domain.models.user_model import User
from src.domain.port.port_out.user_storage_port import UserStoragePort
from src.infrastructure.postgres_adapter.entity.user_entity import UserEntity
from src.infrastructure.postgres_adapter.mapper.user_mapper import from_entity_to_domain


class PostgresUserAdapter(UserStoragePort):
    @contextmanager
    def __get_connection_session(self) -> Generator:
        engine = create_engine(configuration.DATABASE_URL)
        connection: sessionmaker[Session] = sessionmaker(
            autocommit=False, autoflush=False, bind=engine
        )
        try:
            yield connection()
        finally:
            connection().close()

    def get_user(self, user_id: str) -> Optional[User]:
        with self.__get_connection_session() as connection:
            user_entity: UserEntity = connection.query(UserEntity).filter(
                UserEntity.id == user_id
            )[0]
            if user_entity is None:
                return None
            return from_entity_to_domain(user_entity)

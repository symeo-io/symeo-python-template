from contextlib import contextmanager
from typing import Generator, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.domain.model.user_model import User
from src.domain.port.port_out.user_storage_port import UserStoragePort
from src.infrastructure.postgres_adapter.entity.user_entity import UserEntity
from src.infrastructure.postgres_adapter.mapper.user_mapper import UserMapper


class PostgresUserAdapter(UserStoragePort):
    __database_url: str

    def __init__(self, configuration_service: str):
        self.__database_url = configuration_service

    @contextmanager
    def __get_connection_session(self) -> Generator:
        engine = create_engine(self.__database_url, pool_pre_ping=True)
        connection: sessionmaker[Session] = sessionmaker(
            autocommit=False, autoflush=False, bind=engine
        )
        try:
            yield connection()
        finally:
            connection().close()

    def get_user(self, user_id: str) -> Optional[User]:
        with self.__get_connection_session() as connection:
            user_entity = (
                connection.query(UserEntity).filter(UserEntity.id == user_id).first()
            )
            if user_entity is None:
                return None
            return UserMapper.from_entity_to_domain(user_entity)

    def save_user(self, user: User) -> None:
        user_entity: UserEntity = UserMapper.from_domain_to_entity(user)
        with self.__get_connection_session() as connection:
            connection.add(user_entity)
            connection.commit()

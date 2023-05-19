from src.infrastructure.postgres_adapter.entity.user_entity import UserEntity
from tests.utils.database_connection import get_connection_session
from faker import Faker


class MockUser:
    faker = Faker()

    def mock_user_present(self, user_id: str) -> UserEntity:
        with get_connection_session() as connection:
            user_entity: UserEntity = UserEntity(id=user_id, username=self.faker.name())
            connection.add(user_entity)
            connection.commit()
        return user_entity

    @staticmethod
    def delete():
        with get_connection_session() as connection:
            connection.query(UserEntity).delete()
            connection.commit()

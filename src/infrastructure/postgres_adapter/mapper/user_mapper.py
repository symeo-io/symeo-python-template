from src.domain.model.user_model import User
from src.infrastructure.postgres_adapter.entity.user_entity import UserEntity


class UserMapper:
    @staticmethod
    def from_entity_to_domain(user_entity: UserEntity) -> User:
        return User(id=user_entity.id, username=user_entity.username)

    @staticmethod
    def from_domain_to_entity(user: User) -> UserEntity:
        return UserEntity(id=user.id, username=user.username)

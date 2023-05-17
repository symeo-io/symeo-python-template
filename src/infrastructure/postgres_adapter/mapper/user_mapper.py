from src.domain.models.user_model import User
from src.infrastructure.postgres_adapter.entity.user_entity import UserEntity


def from_entity_to_domain(user_entity: UserEntity) -> User:
    return User.from_orm(user_entity)

from typing import Optional

from src.domain.model.user_model import User
from src.domain.port.port_out.user_storage_port import UserStoragePort

from faker import Faker


class UserStoragePortMock(UserStoragePort):
    faker = Faker()

    def get_user(self, user_id: str) -> Optional[User]:
        return User(id=user_id, username=self.faker.name())

    def save_user(self, user: User):
        pass

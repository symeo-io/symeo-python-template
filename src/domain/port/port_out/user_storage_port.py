from typing import Optional

from src.domain.model.user_model import User


class UserStoragePort:
    def get_user(self, user_id: str) -> Optional[User]:
        pass

    def save_user(self, user: User):
        pass

from typing import Optional

from src.domain.models.user_model import User


class UserStoragePort:
    def get_user(self, user_id: str) -> Optional[User]:
        pass

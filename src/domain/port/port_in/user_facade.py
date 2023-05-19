from typing import Optional

from src.domain.model.user_model import User


class UserFacade:
    def get_user(self, user_id: str) -> Optional[User]:
        pass

    def create_user(self, user: User) -> Optional[User]:
        pass

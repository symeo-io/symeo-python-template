from typing import Optional

from src.domain.model.user_model import User
from src.domain.port.port_in.user_facade import UserFacade
from src.domain.port.port_out.user_storage_port import UserStoragePort


class UserService(UserFacade):
    __user_storage_port: UserStoragePort

    def __init__(self, user_storage_port: UserStoragePort):
        self.__user_storage_port = user_storage_port

    def get_user(self, user_id: str) -> Optional[User]:
        return self.__user_storage_port.get_user(user_id)

    def create_user(self, user: User) -> Optional[User]:
        self.__user_storage_port.save_user(user)
        return user

from src.domain.exception.exceptions import UserNotFoundError
from src.domain.model.user_model import User
from src.domain.port.input.user_facade import UserFacade
from src.domain.port.output.user_storage_port import UserStoragePort


class UserService(UserFacade):
    __user_storage_port: UserStoragePort

    def __init__(self, user_storage_port: UserStoragePort):
        self.__user_storage_port = user_storage_port

    def get_user(self, user_id: str) -> User:
        user = self.__user_storage_port.get_user(user_id)
        if not user:
            raise UserNotFoundError(f"User with id {user_id} not found")
        return user

    def create_user(self, user: User) -> User:
        self.__user_storage_port.save_user(user)
        return user

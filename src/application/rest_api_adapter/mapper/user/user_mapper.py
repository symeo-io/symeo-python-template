from src.application.rest_api_adapter.dto.user.get_user_dto import GetUserDTO
from src.application.rest_api_adapter.dto.user.post_user_dto import PostUserDTO
from src.application.rest_api_adapter.dto.user.user_dto import UserDTO
from src.domain.model.user_model import User


class UserMapper:
    @staticmethod
    def from_request_to_domain(user_dto: PostUserDTO):
        user = User(id=user_dto.user.user_id, username=user_dto.user.username)
        return user

    @staticmethod
    def from_domain_to_response(user: User):
        user_dto = UserDTO(user_id=user.id, username=user.username)
        get_user_dto = GetUserDTO(user=user_dto)
        return get_user_dto

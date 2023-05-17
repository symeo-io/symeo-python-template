from src.application.rest_api_adapter.dto.user.get_user_dto import GetUserDTO
from src.application.rest_api_adapter.dto.user.user_dto import UserDTO
from src.domain.models.user_model import User


class UserMapper:
    @staticmethod
    def from_domain_to_response(user: User):
        user_dto = UserDTO(user_id=user.id, username=user.username)
        get_user_dto = GetUserDTO(user=user_dto)
        return get_user_dto

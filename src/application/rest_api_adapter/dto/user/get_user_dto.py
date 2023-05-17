from pydantic.main import BaseModel

from src.application.rest_api_adapter.dto.user.user_dto import UserDTO


class GetUserDTO(BaseModel):
    user: UserDTO

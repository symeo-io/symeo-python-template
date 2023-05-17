from typing import Optional

from fastapi import APIRouter
from pydantic.error_wrappers import ValidationError

from src.application.rest_api_adapter.dto.user.get_user_dto import GetUserDTO
from src.application.rest_api_adapter.mapper.user.user_mapper import UserMapper
from src.domain.port.port_in.user_facade import UserFacade


class UserController:
    def __init__(self, user_facade: UserFacade):
        self.__user_facade = user_facade

    def build(self):
        router = APIRouter()

        @router.get("/{user_id}", status_code=200)
        def get_user(
            user_id: str,
        ) -> Optional[GetUserDTO]:
            """
            Get a specific user by id
            """
            try:
                user = self.__user_facade.get_user(user_id)
                if user:
                    return UserMapper.from_domain_to_response(user)
                return None
            except ValidationError as e:
                print(e.json())

        return router

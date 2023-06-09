from fastapi import APIRouter

from src.application.rest_api_adapter.dto.user.get_user_dto import GetUserDTO
from src.application.rest_api_adapter.dto.user.post_user_dto import PostUserDTO
from src.application.rest_api_adapter.mapper.user.user_mapper import UserMapper
from src.domain.port.input.user_facade import UserFacade


class UserController:
    def __init__(self, user_facade: UserFacade):
        self.__user_facade = user_facade

    def build(self):
        router = APIRouter()

        @router.get("/{user_id}", status_code=200)
        def get_user(
            user_id: str,
        ) -> GetUserDTO:
            """
            Get a specific user by id
            """
            return UserMapper.from_domain_to_response(
                self.__user_facade.get_user(user_id)
            )

        @router.post("/", status_code=200)
        def post_user(
            user_dto: PostUserDTO,
        ) -> GetUserDTO:
            """
            Create a user
            """
            user = self.__user_facade.create_user(
                UserMapper.from_request_to_domain(user_dto)
            )
            return UserMapper.from_domain_to_response(user)

        return router

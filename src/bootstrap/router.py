from fastapi import APIRouter

from src.application.rest_api_adapter.controllers.user_controller import UserController
from src.domain.service.user_service import UserService
from src.infrastructure.postgres_adapter.adapter.postgres_user_adapter import (
    PostgresUserAdapter,
)

api_router = APIRouter()
api_router.include_router(
    UserController(UserService(PostgresUserAdapter())).build(),
    prefix="/users",
    tags=["users"],
)

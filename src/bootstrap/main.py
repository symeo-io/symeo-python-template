import os
import sys
from typing import List, Optional

import uvicorn
from alembic.config import Config
from fastapi import APIRouter
from fastapi import FastAPI
import alembic.command
from src.application.rest_api_adapter.controller.user_controller import UserController
from src.domain.configuration.configuration_service import ConfigurationService
from src.domain.service.user_service import UserService
from src.infrastructure.postgres_adapter.adapter.postgres_user_adapter import (
    PostgresUserAdapter,
)
from src.infrastructure.postgres_adapter.utils.postgres_utils import get_postgres_url


# Run with uvicorn & gunicorn
# uvicorn src.main:bootstrap
def bootstrap(
    input_args: List[str], test_container_url: Optional[str] = None
) -> FastAPI:
    configuration_service = ConfigurationService()
    configuration_service.init_from_args(input_args)

    alembic_config_path = (
        os.path.dirname(os.path.abspath(__file__)) + "/../../alembic.ini"
    )
    alembic_config = Config(alembic_config_path)
    database_url = get_postgres_url(configuration_service, test_container_url)
    escaped_database_url = database_url.replace("%", "%%")
    alembic_config.set_section_option("alembic", "sqlalchemy.url", escaped_database_url)
    alembic_config.set_section_option(
        "alembic",
        "script_location",
        os.path.dirname(os.path.abspath(__file__))
        + "/../infrastructure/postgres_adapter/alembic",
    )
    alembic.command.upgrade(alembic_config, "head")  # Run migrations at runtime

    postgres_user_adapter: PostgresUserAdapter = PostgresUserAdapter(database_url)
    user_service: UserService = UserService(postgres_user_adapter)

    app = FastAPI(title="Your API")
    api_router = APIRouter()
    api_router.include_router(
        UserController(user_service).build(),
        prefix="/users",
        tags=["users"],
    )
    app.include_router(api_router, prefix="/api/v1")
    app.include_router(add_health_check(), tags=["tech"])
    return app


def add_health_check() -> APIRouter:
    api_router = APIRouter()

    @api_router.get("/health_check")
    def perform_health_check():
        return {"healthcheck": "Everything OK!"}

    return api_router


# Run with Poetry
def main():
    app = bootstrap(sys.argv)
    uvicorn.run(app=app, port=9999)


# Run with IDE
if __name__ == "__main__":
    properties_file = (
        os.path.dirname(os.path.abspath(__file__))
        + "/../../properties/local.example.ini"
    )
    secrets_file = (
        os.path.dirname(os.path.abspath(__file__)) + "/../../secrets/local.example.ini"
    )
    app = bootstrap([f"properties:{properties_file}", f"secrets:{secrets_file}"])
    uvicorn.run(app=app, port=9999)

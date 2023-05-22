import sys
from typing import List, Optional

import alembic.command
import uvicorn
from fastapi import FastAPI

from src.infrastructure.postgres_adapter.utils.postgres_utils import get_postgres_url
from src.application.rest_api_adapter.controller.user_controller import UserController
from src.domain.service.user_service import UserService
from src.infrastructure.postgres_adapter.adapter.postgres_user_adapter import (
    PostgresUserAdapter,
)
from src.domain.configuration.configuration_service import ConfigurationService
from fastapi import APIRouter
from alembic.config import Config


# Run with uvicorn & gunicorn
# uvicorn src.main:bootstrap
def bootstrap(
    input_args: List[str], test_container_url: Optional[str] = None
) -> FastAPI:
    configuration_service = ConfigurationService()
    configuration_service.init_from_args(input_args)

    alembic_config = Config("alembic.ini")
    database_url = get_postgres_url(configuration_service, test_container_url)
    escaped_database_url = database_url.replace("%", "%%")
    alembic_config.set_section_option("alembic", "sqlalchemy.url", escaped_database_url)
    alembic.command.upgrade(alembic_config, "head")

    app = FastAPI(title="Your API")
    api_router = APIRouter()
    api_router.include_router(
        UserController(UserService(PostgresUserAdapter(database_url))).build(),
        prefix="/users",
        tags=["users"],
    )
    app.include_router(api_router, prefix="/api/v1")
    return app


# Run with Poetry
def main():
    app = bootstrap(sys.argv)
    uvicorn.run(app=app, port=9999)


# Run with IDE
if __name__ == "__main__":
    main()

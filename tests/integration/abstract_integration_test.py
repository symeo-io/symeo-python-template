import os
import time
from abc import ABC
from pathlib import Path

from src.bootstrap.main import bootstrap
from testcontainers.postgres import PostgresContainer
from fastapi.testclient import TestClient


class AbstractIntegrationTestClass(ABC):
    PROPERTIES_PATH: Path = (
        os.path.dirname(os.path.abspath(__file__)) + "/properties/tests.ini"
    )
    SECRETS_PATH: Path = (
        os.path.dirname(os.path.abspath(__file__)) + "/secrets/tests.ini"
    )

    postgres_container = None
    app_client = None
    input_args = None
    configuration_service = None

    @classmethod
    def set_up_class(cls) -> None:
        # Start Databases
        cls.postgres_container = PostgresContainer(
            "postgres:13",
            user="postgres-test",
            password="password-test",
            dbname="symeo-python-template-test",
        )
        cls.postgres_container.start()
        time.sleep(5)

        # Start application
        cls.input_args = [
            f"properties:{cls.PROPERTIES_PATH}",
            f"secrets:{cls.SECRETS_PATH}",
        ]
        cls.app_client = TestClient(
            bootstrap(cls.input_args, cls.postgres_container.get_connection_url())
        )

    @classmethod
    def tear_down_class(cls):
        cls.postgres_container.stop()

import os
import urllib.parse
from src.domain.configuration.configuration_service import ConfigurationService


def get_postgres_url(
    configuration_service: ConfigurationService, testing_db_url: str = None
) -> str:
    if testing_db_url:
        return testing_db_url
    postgres_url = (
        "postgresql+psycopg2://"
        f"{configuration_service.get_properties().get('POSTGRES', 'postgres_username', vars=os.environ)}"
        f":{urllib.parse.quote(configuration_service.get_secrets().get('POSTGRES', 'postgres_password', vars=os.environ))}"
        f"@{configuration_service.get_properties().get('POSTGRES', 'postgres_host', vars=os.environ)}"
        f":{configuration_service.get_properties().get('POSTGRES', 'postgres_port', vars=os.environ)}"
        f"/{configuration_service.get_properties().get('POSTGRES', 'postgres_db', vars=os.environ)}"
    )
    return postgres_url

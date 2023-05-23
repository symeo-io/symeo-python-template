import urllib.parse
from src.domain.configuration.configuration_service import ConfigurationService


def get_postgres_url(
    configuration_service: ConfigurationService, testing_db_url: str = None
) -> str:
    if testing_db_url:
        return testing_db_url
    postgres_url = (
        f"postgresql+psycopg2://{configuration_service.get_properties().get('POSTGRES', 'user')}:{urllib.parse.quote(configuration_service.get_secrets().get('POSTGRES', 'password'))}@{configuration_service.get_properties().get('POSTGRES', 'host')}/{configuration_service.get_properties().get('POSTGRES', 'db')}"
    )
    return postgres_url

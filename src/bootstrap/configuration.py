import os
import urllib.parse
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Configuration:
    POSTGRES_USER: str = urllib.parse.quote(os.getenv("POSTGRES_USER", "postgres"))
    POSTGRES_PASSWORD: str = urllib.parse.quote(
        os.getenv("POSTGRES_PASSWORD", "P@ssword")
    )
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: int = int(
        os.getenv("POSTGRES_PORT", 5432)
    )  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "bdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


configuration = Configuration()

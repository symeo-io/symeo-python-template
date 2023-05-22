import os

from configparser import ConfigParser
from typing import List, Any

from src.domain.exception.exceptions import (
    MissingConfigurationArgsError,
    ConfigurationFileNotFoundError,
)


class ConfigurationService:
    def init_from_args(self, args: List[str]) -> Any:
        properties: str = self._get_placeholder_value(
            self._get_placeholder_from_args(args, "properties:")
        )
        secrets: str = self._get_placeholder_value(
            self._get_placeholder_from_args(args, "secrets:")
        )
        self._validate_input_path(properties)
        self._validate_input_path(secrets)
        self._properties: ConfigParser = ConfigParser()
        self._secrets: ConfigParser = ConfigParser()
        self._properties.read(properties)
        self._secrets.read(secrets)

    def get_properties(self) -> ConfigParser:
        return self._properties

    def get_secrets(self) -> ConfigParser:
        return self._secrets

    @staticmethod
    def _get_placeholder_value(from_arg: str) -> str:
        return from_arg.split(":")[1]

    @staticmethod
    def _get_placeholder_from_args(args: List[str], placeholder: str) -> str:
        for arg in args:
            if str(arg).startswith(placeholder):
                return arg
        raise MissingConfigurationArgsError()

    @staticmethod
    def _validate_input_path(file: str) -> None:
        if os.path.isfile(file) is False:
            raise ConfigurationFileNotFoundError(f"File {file} not found.")

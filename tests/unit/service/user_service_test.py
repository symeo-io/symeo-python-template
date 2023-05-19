import unittest

from src.domain.model.user_model import User
from src.domain.service.user_service import UserService
from tests.utils.mock.user_storage_mock import UserStoragePortMock

from faker import Faker


class UserServiceTest(unittest.TestCase):
    faker = Faker()
    __user_storage_port_mock: UserStoragePortMock
    __user_service: UserService

    def setUp(self) -> None:
        self.__user_storage_port_mock = UserStoragePortMock()
        self.__user_service = UserService(self.__user_storage_port_mock)

    def test_should_return_user(self):
        # Given
        fake_id = self.faker.name()

        # When
        user = self.__user_service.get_user(user_id=fake_id)

        # Then
        self.assertIsNotNone(user)

    def test_should_save_a_user(self):
        # Given
        user = User(id=self.faker.name(), username=self.faker.name())

        # When
        user_created = self.__user_service.create_user(user)

        # Then
        self.assertEqual(user_created, user)

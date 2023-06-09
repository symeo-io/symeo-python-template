import unittest

from faker import Faker

from src.application.rest_api_adapter.dto.user.get_user_dto import GetUserDTO
from src.application.rest_api_adapter.dto.user.post_user_dto import PostUserDTO
from src.application.rest_api_adapter.dto.user.user_dto import UserDTO
from src.domain.model.user_model import User
from tests.integration.abstract_integration_test import AbstractIntegrationTestClass


class UserControllerTest(unittest.TestCase, AbstractIntegrationTestClass):
    faker = Faker()

    @classmethod
    def setUpClass(cls) -> None:
        cls.set_up_class()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tear_down_class()

    def test_should_create_user(self):
        # Given
        fake_id = self.faker.name() + "_id_1"
        fake_username = self.faker.name() + "_name_1"
        post_user_dto = PostUserDTO(
            user=UserDTO(user_id=fake_id, username=fake_username)
        )

        # When
        response = self.app_client.post("api/v1/users/", content=post_user_dto.json())

        # Then
        self.assertEqual(
            response.json(),
            GetUserDTO(user=UserDTO(user_id=fake_id, username=fake_username)),
        )

    def test_should_return_user_present(self):
        # Given
        fake_id = self.faker.name() + "_id_2"
        fake_username = self.faker.name() + "_name_1"
        self.postgres_user_adapter.save_user(User(id=fake_id, username=fake_username))

        # When
        response = self.app_client.get(f"api/v1/users/{fake_id}")

        # Then
        self.assertEqual(response.json()["user"]["user_id"], fake_id)
        self.assertEqual(response.json()["user"]["username"], fake_username)

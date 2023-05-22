import unittest
from faker import Faker

from tests.integration.abstract_integration_test import AbstractIntegrationTestClass
from src.application.rest_api_adapter.dto.user.get_user_dto import GetUserDTO
from src.application.rest_api_adapter.dto.user.post_user_dto import PostUserDTO
from src.application.rest_api_adapter.dto.user.user_dto import UserDTO
from tests.utils.entities.mock_user import MockUser


class PostUserControllerTest(unittest.TestCase, AbstractIntegrationTestClass):
    faker = Faker()
    __mock_user: MockUser

    @classmethod
    def setUpClass(cls) -> None:
        cls.set_up_class()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tear_down_class()

    def setUp(self) -> None:
        self.__mock_user = MockUser()

    def tearDown(self) -> None:
        self.__mock_user.delete(self.postgres_container)

    def test_should_create_user(self):
        # Given
        fake_id = self.faker.name()
        fake_username = self.faker.name()
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

import unittest

from faker import Faker

from tests.integration.abstract_integration_test import AbstractIntegrationTestClass
from tests.utils.entities.mock_user import MockUser


class GetUserControllerTest(unittest.TestCase, AbstractIntegrationTestClass):
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

    def test_should_return_user_present(self):
        # Given
        fake_id = self.faker.name()
        self.__mock_user.mock_user_present(self.postgres_container, fake_id)

        # When
        response = self.app_client.get(f"api/v1/users/{fake_id}")

        # Then
        self.assertEqual(response.json()["user"]["user_id"], fake_id)
        self.assertIsNotNone(response.json()["user"]["username"])

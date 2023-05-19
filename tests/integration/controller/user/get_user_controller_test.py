import unittest

from faker import Faker

from tests.integration.app_client import test_client
from tests.utils.entities.mock_user import MockUser


class GetUserControllerTest(unittest.TestCase):
    faker = Faker()
    __mock_user: MockUser

    def setUp(self) -> None:
        self.__mock_user = MockUser()

    def tearDown(self) -> None:
        self.__mock_user.delete()

    def test_should_return_user_present(self):
        # Given
        fake_id = self.faker.name()
        self.__mock_user.mock_user_present(fake_id)

        # When
        response = test_client.get(f"api/v1/users/{fake_id}")

        # Then
        self.assertEqual(response.json()["user"]["user_id"], fake_id)
        self.assertIsNotNone(response.json()["user"]["username"])

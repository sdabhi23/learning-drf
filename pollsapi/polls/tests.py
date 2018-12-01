from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework.test import APIClient

class TestPoll(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = self.setup_user()
        self.uri = '/polls/'

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_list_anon(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 401, 'Expected Response Code 401, received {0} instead.'.format(response.status_code))

    def test_list_auth(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,'Expected Response Code 200, received {0} instead.'.format(response.status_code))

    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
            "question": "How are you?",
            "created_by": 1
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201, 'Expected Response Code 201, received {0} instead.'.format(response.status_code))
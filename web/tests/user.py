from web.models import User

from rest_framework.test import APITestCase

class UserTests(APITestCase):
    url = '/users/'
    user = None
    data = {'username': 'test@liefbase.io', 'password': 'password'}

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(**cls.data)

    def setUp(self):
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        new_user = {'username': 'test2@liefbase.io', 'password': 'password2'}
        response = self.client.post(self.url, new_user, format='json')
        
        self.assertEqual(response.status_code, 201)

    def test_create_duplicate_user(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_get_users(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_user(self):
        response=self.client.get('{}{}/'.format(self.url, self.user.id))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], self.data['username'])

    def test_update_user(self):
        # TODO implement me
        pass

    def test_partial_update_user(self):
        # TODO implement me
        pass

    def test_update_other_user(self):
        # TODO implement me
        pass

    def test_partial_pdate_other_user(self):
        # TODO implement me
        pass

    def test_delete_user(self):
        # TODO implement me
        pass

    def test_delete_other_user(self):
        # TODO implement me
        pass

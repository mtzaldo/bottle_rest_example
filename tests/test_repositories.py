from unittest import TestCase
from repositories import UsersRepository

from tests.mocks import test_db

class TestUserRepository(TestCase):
    
    def setUp(self):
        
        self.repo = UsersRepository(test_db)
        
    def test_get_return_None_when_username_is_not_in_db(self):
        username = 'im_not_a_username'
        password = 'password'
        
        expected_result = {}
        
        result = self.repo.get(username, password)
        
        self.assertEqual(expected_result, result)
        
    def test_get_returns_None_when_username_password_dont_match(self):
        username = 'user1'
        password = 'thepassword'
        
        expected_result = {}
        
        result = self.repo.get(username, password)
        
        self.assertEqual(expected_result, result)
        
    def test_get_returns_a_valid_user(self):
        username = 'user2'
        password = 'password'
        
        expected_result = {
            'id': 2,
            'username': username,
            'password': password,
        }
        
        result = self.repo.get(username, password)
        
        self.assertEqual(expected_result, result)
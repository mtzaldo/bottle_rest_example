from unittest import TestCase
from unittest.mock import MagicMock

from rest.services import TodoService

import json

class TestTodoService(TestCase):
    
    def test_get_todo_with_author_returns_a_valid_value(self):
        todo_id, user_id = 1, 3
        
        raw = '{"id": ' + str(todo_id) + ', "title": "ham bacon carnitas", "completed": false, "author": {"id": ' + str(user_id) + ', "username": "user1"}}'
        expected_result = json.loads(raw)
        
        api_raw = '{"userId": ' + str(user_id) + ', "id": ' + str(todo_id) + ', "title": "delectus aut autem", "completed": false}'
        api = MagicMock()
        api.get = MagicMock(return_value = json.loads(api_raw))
        
        repo = MagicMock()
        repo_raw = '{"id": ' + str(user_id) + ', "username": "user1", "password": "password"}'
        repo.get_by_id = MagicMock(return_value = json.loads(repo_raw))
        
        words_repo = MagicMock()
        words_repo.get = MagicMock(side_effect=self.words_repo_get)
        
        svc = TodoService(api, repo, words_repo)
        
        result = svc.get(todo_id)
            
        self.assertEqual(expected_result, result)
        
    def words_repo_get(self, w):
        words = {
            'delectus': 'ham',
            'aut': 'bacon',
            'autem': 'carnitas'
        }
        
        return words.get(w, '')
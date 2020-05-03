from unittest import TestCase
from unittest.mock import MagicMock

from services.todo_service import TodoService

import json

class TestTodoService(TestCase):
    
    def test_get_todo_with_author_retunrs_a_valid_value(self):
        raw = '{"id": 1, "title": "delectus aut autem", "completed": false, "author": {"id": 1, "username": "user1"}}'
        expected_result = json.loads(raw)
        
        api_raw = '{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}'
        api = MagicMock()
        api.get = MagicMock(return_value = json.loads(api_raw))
        
        repo = MagicMock()
        repo_raw = '{"id": 1, "username": "user1", "password": "password"}'
        repo.get_by_id = MagicMock(return_value = json.loads(repo_raw))
        
        svc = TodoService(api, repo)
        
        result = svc.get(1)
            
        self.assertEqual(expected_result, result)
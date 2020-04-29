from unittest import TestCase
from unittest.mock import patch, MagicMock

from endpoints.todo_endpoints import TodoEndpoints

import json

class TestTodoEndpoints(TestCase):
  
  def test_get_returns_404_and_empty_obj_when_no_user_found(self):
    expected_result = {}
    expected_status_code = 404
    
    app = MagicMock()
    app.route = MagicMock(return_value = None)
    
    res = MagicMock()
    
    svc = MagicMock()
    svc.get = MagicMock(return_value = expected_result)
    
    endpoint = TodoEndpoints(app, res, svc)
    
    result = endpoint.get(0)
    
    self.assertEqual(res.status, expected_status_code)
    self.assertEqual(expected_result, result)
    
  def test_get_returns_200_and_user_obj_when_user_found(self):
    json_text = '{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}'
    expected_result = json.loads(json_text)
    expected_status_code = 200
    
    app = MagicMock()
    app.route = MagicMock(return_value = None)
    
    res = MagicMock()
    
    svc = MagicMock()
    svc.get = MagicMock(return_value = expected_result)
    
    endpoint = TodoEndpoints(app, res, svc)
    
    result = endpoint.get(1)
    
    self.assertEqual(res.status, expected_status_code)
    self.assertEqual(expected_result, result)
    
    
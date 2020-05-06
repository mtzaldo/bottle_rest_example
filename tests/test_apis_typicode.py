from unittest import TestCase
from unittest.mock import MagicMock
from requests import Response

import requests, json

from rest.apis.typicode import TypicodeTodoApiClient

class TestTypiCodeTodoApiClient(TestCase):
  
  def test_get_by_id_returns_a_valid_todo(self):
    json_text= '{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": false}'
    expected_result = json.loads(json_text)
    
    response = Response()
    response.status_code = 200
    response.json = MagicMock(return_value = expected_result)
    requests.get = MagicMock(return_value = response)
    
    api = TypicodeTodoApiClient('http://fake.url')
    
    result = api.get(1)
    
    self.assertEqual(expected_result, result)
    
  def test_get_by_id_return_empty_when_the_the_obj_doesnt_exit(self):
    expected_result = {}
    
    response = Response()
    response.status_code = 404
    requests.get = MagicMock(return_value = response)
    
    api = TypicodeTodoApiClient('http://fake.url')
    
    result = api.get(0)
    
    self.assertEqual(expected_result, result)
    
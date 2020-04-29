from unittest import TestCase
from unittest.mock import patch, MagicMock, PropertyMock

from endpoints.user_endpoints import UserEndpoints

class TestUserEndpoints(TestCase):
  
  def test_login_returns_404_and_false_when_no_user_found(self):
    expected_result = 'false'
    expected_status_code = 404
    
    app = MagicMock()
    app.route = MagicMock(return_value = None)
    
    res = MagicMock()
    
    req = MagicMock()
    req.json = {'username': 'user1', 'password': 'password1'}
    
    svc = MagicMock()
    svc.login = MagicMock(return_value = False)
    
    endpoint = UserEndpoints(app, req, res, svc)
    
    result = endpoint.login()
    
    self.assertEqual(res.status, expected_status_code)
    self.assertEqual(expected_result, result)
    
  def test_login_returns_404_and_false_when_no_password_from_request(self):
    expected_result = 'false'
    expected_status_code = 404
    
    app = MagicMock()
    app.route = MagicMock(return_value = None)
    
    res = MagicMock()
    
    req = MagicMock()
    req.json = {'username': 'user1'}
    
    endpoint = UserEndpoints(app, req, res, None)

    result = endpoint.login()
    
    self.assertEqual(res.status, expected_status_code)
    self.assertEqual(expected_result, result)
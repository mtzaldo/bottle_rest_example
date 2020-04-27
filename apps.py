from bottle import Bottle, run, request, response

from endpoints.post_endpoints import PostEndpoints
from endpoints.todo_endpoints import TodoEndpoints
from services.todo_service import TodoService

from services.post_service import PostService
from apis.typecode.todo_api import TypeCodeTodoApiClient
from apis.typecode.post_api import TypeCodePostApiClient

from repositories.users_repository import UsersRepository
from services.user_service import UserService
from endpoints.user_endpoints import UserEndpoints

import db
import settings

class TodoApp(Bottle):
    
    def __init__(self):
        super().__init__()
        api = TypeCodeTodoApiClient(settings.TYPECODE_URI)
        service = TodoService(api)
        endpoints = TodoEndpoints(self, service)
                
class PostApp(Bottle):
    
    def __init__(self):
        super().__init__()
        api = TypeCodePostApiClient(settings.TYPECODE_URI)
        service = PostService(api)
        endpoints = PostEndpoints(self, service)

class UserApp(Bottle):
    def __init__(self):
        super().__init__()
        repo = UsersRepository(db)
        service = UserService(repo)
        endpoints = UserEndpoints(self, request, response, service)
        
from bottle import Bottle, run, request, response

from endpoints.post_endpoints import PostEndpoints
from endpoints.todo_endpoints import TodoEndpoints
from services.todo_service import TodoService

from services.post_service import PostService
from apis.typicode.todo_api import TypicodeTodoApiClient
from apis.typicode.post_api import TypicodePostApiClient

from repositories.users_repository import UsersRepository
from services.user_service import UserService
from endpoints.user_endpoints import UserEndpoints

import db
import settings

class TodoApp(Bottle):
    
    def __init__(self):
        super().__init__()
        api = TypicodeTodoApiClient(settings.TYPECODE_URI)
        repo = UsersRepository(db)
        service = TodoService(api, repo)
        endpoints = TodoEndpoints(self, response, service)
                
class PostApp(Bottle):
    
    def __init__(self):
        super().__init__()
        api = TypicodePostApiClient(settings.TYPECODE_URI)
        service = PostService(api)
        endpoints = PostEndpoints(self, service)

class UserApp(Bottle):
    def __init__(self):
        super().__init__()
        repo = UsersRepository(db)
        service = UserService(repo)
        endpoints = UserEndpoints(self, request, response, service)
        
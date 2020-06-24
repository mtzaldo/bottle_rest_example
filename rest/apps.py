from bottle import Bottle, request, response

from services import TodoService, PostService, UserService
from endpoints import TodoEndpoints, PostEndpoints, UserEndpoints
from repositories import UsersRepository, WordsRepository
from apis.typicode import TypicodeTodoApiClient, TypicodePostApiClient

import db
import settings


class TodoApp(Bottle):

    def __init__(self):
        super().__init__()
        api = TypicodeTodoApiClient(settings.TYPECODE_URI)
        users_repo = UsersRepository(db)
        # repository handling the db open/close itself
        words_repo = WordsRepository(settings.REPLACEMENTS_DB)
        service = TodoService(api, users_repo, words_repo)

        TodoEndpoints(self, response, service)


class PostApp(Bottle):

    def __init__(self):
        super().__init__()
        api = TypicodePostApiClient(settings.TYPECODE_URI)
        service = PostService(api)

        PostEndpoints(self, service)


class UserApp(Bottle):

    def __init__(self):
        super().__init__()
        repo = UsersRepository(db)
        service = UserService(repo)

        UserEndpoints(self, request, response, service)

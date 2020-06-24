class TodoEndpoints:

    def __init__(self, app, res, service):
        self.app = app
        self.service = service
        self.response = res

        # init routes
        self.app.route('/', ['GET'], self.all)
        self.app.route('/<id:int>', ['GET'], self.get)

    def all(self):
        return self.service.all()

    def get(self, id):
        result = self.service.get(id)

        status_code = 404 if result == {} else 200
        self.response.status = status_code

        return result


class PostEndpoints:

    def __init__(self, app, service):
        self.app = app
        self.service = service

        # init routes
        self.app.route('/', ['GET'], self.all)
        self.app.route('/<id:int>', ['GET'], self.get)

    def all(self):
        return self.service.all()

    def get(self, id):
        return self.service.get(id)


class UserEndpoints:

    def __init__(self, app, req, res, svc):
        self.app = app
        self.service = svc
        self.request = req
        self.response = res

        # init routes
        self.app.route('/login', ['POST'], self.login)

    def login(self):
        username = self.request.json.get('username', '')
        password = self.request.json.get('password', '')

        success = False

        if username and password:
            success = self.service.login(username, password)

        status_code = 200 if success else 404

        self.response.status = status_code

        return str(success).lower()

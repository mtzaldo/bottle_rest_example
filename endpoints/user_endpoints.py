class UserEndpoints:
    
    def __init__(self, app, req, res, svc):
        self.app = app
        self.service = svc
        self.request = req
        self.response = res
        
        #init routes
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
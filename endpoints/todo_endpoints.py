class TodoEndpoints:
    
    def __init__(self, app, res, service):
        self.app = app
        self.service = service
        self.response = res
        
        #init routes
        self.app.route('/', ['GET'], self.all)
        self.app.route('/<id:int>', ['GET'], self.get)
        
    def all(self):
        return self.service.all()
    
    def get(self, id):
        result = self.service.get(id)
        
        status_code = 404 if result == {} else 200
        self.response.status = status_code
        
        return result
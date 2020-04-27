class TodoEndpoints:
    
    def __init__(self, app, service):
        self.app = app
        self.service = service
        
        #init routes
        self.app.route('/', ['GET'], self.all)
        self.app.route('/<id:int>', ['GET'], self.get)
        
    def all(self):
        return self.service.all()
    
    def get(self, id):
        return self.service.get(id)
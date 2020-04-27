class TodoService:
    
    def __init__(self, api):
        self.api = api
        
    def all(self):
        return self.api.all()
    
    def get(self, id):
        return self.api.get(id)
class TodoService:
    
    def __init__(self, api, repo):
        self.api = api
        self.repo = repo
        
    def all(self):
        return self.api.all()
    
    def get(self, id):
        todo = self.api.get(id)
        userId = todo.get('userId', 0)
        author = self.repo.get_by_id(userId) if userId else {}
        
        value = {}
        
        if author:
            del author['password']        
            del todo['userId']
            
            value = todo
            value['author'] = author
        
        return value
from functools import reduce

class TodoService:
    
    def __init__(self, api, repo, words_repo):
        self.api = api
        self.repo = repo
        self.words_repo = words_repo
        
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
            title = value.get('title', '')
            
            value['author'] = author
            value['title'] = self.clean_title(title)
            
        return value
        
    def clean_title(self, title):
        
        def get_replacement(w):
            s = self.words_repo.get(w)
            return s if s else w
        
        title_splitted = title.split(' ')
        new_title = reduce(lambda t, w: f'{t} {get_replacement(w)}', title_splitted, '')
        
        return new_title.strip()
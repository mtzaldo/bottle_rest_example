import requests

class TypicodeTodoApiClient:
    
    PATH = 'todos'
    
    def __init__(self, base_uri):
        self.base_uri = base_uri
        
    def all(self):
        uri = f'{self.base_uri}/{self.PATH}'
        res = requests.get(uri)
        
        return res.text if res.ok else []
    
    def get(self, id):
        uri = f'{self.base_uri}/{self.PATH}/{id}'
        res = requests.get(uri)
        
        return res.json() if res.ok else {}
        
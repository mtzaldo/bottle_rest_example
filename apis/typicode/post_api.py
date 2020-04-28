import requests

class TypicodePostApiClient:
    
    PATH = 'posts'
    
    def __init__(self, base_uri):
        self.base_uri = base_uri
        
    def all(self):
        uri = f'{self.base_uri}/{self.PATH}'
        res = requests.get(uri)
        
        return res.text
    
    def get(self, id):
        uri = f'{self.base_uri}/{self.PATH}/{id}'
        res = requests.get(uri)
        
        return res.json()
        
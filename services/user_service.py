class UserService:
    def __init__(self, repo):
        self.repo = repo
        
	
    def login(self, username, password):
        return True if self.repo.get(username, password) else False
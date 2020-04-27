class UsersRepository:
    
    def __init__(self, db):
        self.db = db
        
    def get(self, username, password):
        
        res = list(
            	filter(
                    lambda u: u.get('username') == username and u.get('password') == password, 
                    self.db.users
                )
        )
        
        return res[0] if len(res) else None
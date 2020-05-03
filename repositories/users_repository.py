class UsersRepository:
    
    def __init__(self, db):
        self.db = db
        
    def get(self, username, password):
        
        iter = filter(
                lambda u: u.get('username') == username and u.get('password') == password, 
                self.db.users
            )
            
        user = next((u for u in iter), {})
        
        return user.copy()
        
    def get_by_id(self, id):
        
        iter = filter(
                lambda u: u.get('id', 0) == id, 
                self.db.users
            )
        
        user = next((u for u in iter), {})
        
        return user.copy()
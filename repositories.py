import sqlite3

class WordsRepository:
    
    def __init__(self, dbfile):
        self.dbfile = dbfile
        
    def get(self, word):
        
        db = sqlite3.connect(self.dbfile)
        db.row_factory = sqlite3.Row
        
        row = None
        
        try:
            row = db.execute('SELECT replacement FROM replacements WHERE word = ?;', (word,)).fetchone()
            #if autocommit: db.commit()
        except sqlite3.IntegrityError:
            db.rollback()
            #raise HTTPError(500, "Database Error", e)
        finally:
            db.close()
        
        return row['replacement'] if row else None
        
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
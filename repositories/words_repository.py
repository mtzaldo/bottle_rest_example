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
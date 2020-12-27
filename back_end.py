import sqlite3

class Database:

    def __init__(self , db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS wish (id INTEGER PRIMARY KEY , wish text , date text , target text , status text)")
        self.conn.commit()
        
    def insert(self , wish , date , target , status):
        self.cur.execute("INSERT INTO wish VALUES (NULL , ? , ? , ? , ?)" , (wish , date , target , status))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM wish")
        rows = self.cur.fetchall()
        return rows

    def search(self , wish = "" , date = "" , target = "" , status = ""):
        self.cur.execute("SELECT * FROM wish WHERE wish = ? OR date = ? OR target = ? OR status = ?" , (wish , date , target , status))
        rows = self.cur.fetchall()
        return rows

    def delete(self , id):
        self.cur.execute("DELETE FROM wish WHERE id = ?" , (id,))
        self.conn.commit()

    def update(self , id , wish , date , target , status):
        self.cur.execute("UPDATE wish SET wish = ? , date = ? , target = ? , status = ? WHERE id = ?" , (wish , date , target , status , id))
        self.conn.commit()

    #connect()
    #insert("Selsai kuliah" , "11 August 2020" , "2023" , "Incomplete")
    #delete(2)
    #update(1 , "Python" , "11 August 2020" , "1 September 2020" , "Incomplete")
    #print(view())
    #print(search(wish = "Python"))
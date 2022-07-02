import sqlite3 

class DB:

    def sqlite_connection(self):
        try:
            con = sqlite3.connect('USERS.db')
        except sqlite3.OperationalError:
            print('Error')
        return con

    def create_login_table(self):
        con = self.sqlite_connection() 
        cur = con.cursor()
        try: 
            cur.execute('''CREATE TABLE IF NOT EXISTS LOGIN (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,    
                            USER_NAME TEXT NOT NULL, 
                            PASSWORD TEXT NOT NULL) 
                        ''')
            con.commit()  
            print()
        except sqlite3.OperationalError:
            print('Table already exist')
            
    def insert_user(self,nombre,contrasena):
        self.create_login_table()
        con = self.sqlite_connection() 
        cur = con.cursor()
        try:
            cur.execute('INSERT INTO LOGIN VALUES(NULL,?, ?)',
                        (nombre,
                        contrasena,
                        )
            )
            con.commit()
            print('Data inserted correctly')
        except sqlite3.OperationalError:
            print('Error on insert data')    
            con.close()
from persistence import DB

db=DB()

class Users:

    def insert_data_user(self,nombre,contrasena):
        db.insert_user(nombre,contrasena)
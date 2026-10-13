import sqlite3

class cnSqlite:
    def __init__(self):
        self.config = "database.db"
    def EjecutaSQL(self,sql,datos):
        pass
    def GetSQL(self,sql,datos):
        pass

class clUsuario(cnSqlite):
    def __init__(self,id=None,username=None,password=None):
        super().__init__()
        self.id = id
        self.username = username 
        self.password = password
    def Verificar(self):
        return True
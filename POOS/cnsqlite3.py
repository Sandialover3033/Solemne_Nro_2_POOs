import sqlite3

class cnSqlite:
    def __init__(self):
        self.config = "c:/proyectos/poos/ejemplo.db"

    def Ejecutar(self,sql,datos):
        with sqlite3.connect(self.config) as conn:
            cursor = conn.cursor()
            cursor.execute(sql,datos)
            conn.commit()
            cursor.close()

    def BuscaById(self,sql,id):
        with sqlite3.connect(**self.config) as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, (id))
            fila = cursor.fetchone()
            return fila 

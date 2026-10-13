import sqlite3

class SqlITE:
    def __init__(self, cursor=None):
        conexion = sqlite3.connect("C:\Users\amoal\Desktop\Ejemplo\DBInforme.db")

        cursor = conexion.cursor()
        cursor.execute()

        cursor.close()
        conexion.commit()
        conexion.close()

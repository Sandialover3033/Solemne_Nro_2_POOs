import sqlite3

class sqlite3:
    def __init__(self, cursor=None):
        ##
        ##"C:\Users\amoal\Desktop\PROYECTOP\Solemne_Nro_2_POOs\DBInforme.db"
        self.config = "C:\Users\amoal\Desktop\PROYECTOP\Solemne_Nro_2_POOs\DBInforme.db"

    def ejecutar(self,Instruccion,Valor):
        with sqlite3.connect(self.config) as conectar:
            cursor = conectar.cursor()
            cursor.execute(Instruccion,Valor)
            conectar.commit()
            cursor.close()

    def buscar(self,Instruccion,ID):
        with sqlite3.connect(self.config) as conectar:
            cursor = conectar.cursor()
            cursor.execute(Instruccion,ID)
            resultado = cursor.fetchone()
            return resultado
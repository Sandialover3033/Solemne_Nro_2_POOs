import sqlite3

class SqlITE:
    def __init__(self, cursor=None):
        ##
        ##"C:\Users\amoal\Desktop\PROYECTOP\Solemne_Nro_2_POOs\DBInforme.db"
        self.config = "C:\Users\amoal\Desktop\PROYECTOP\Solemne_Nro_2_POOs\DBInforme.db"

    def Consulta(self,Instruccion,Valor):
        with sqlite3.connect(self.config) as Conectar:
            cursor = Conectar.cursor()
            cursor.execute(Instruccion,Valor)
            cursor.close()

    def Buscar(self,Instruccion,Valor):
        with sqlite3.connect(self.config) as Conectar:
            cursor = Conectar.cursor()




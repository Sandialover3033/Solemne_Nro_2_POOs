import sqlite3
conexion = sqlite3.connect("C:/Users/THN_LAB/Desktop/Ej/EI.db")

cursor = conexion.cursor()
cursor.execute(" INSERT INTO ACORDABLE (ID,FONO) VALUES (5,47823) ")

cursor.close()
conexion.commit()
conexion.close()


#class Sql:
    #def __init__(self):
        #self.config = "C:\Users\THN_LAB\Downloads\projecto.sqbpro"


weqasdasd
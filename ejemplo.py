import sqlite3

# Conectar a la base de datos (si no existe, se crea automáticamente)
conexion = sqlite3.connect("U:/SGM/poos.db")

# Crear un objeto cursor para ejecutar consultas SQL
cursor = conexion.cursor()

cursor.execute("SELECT * FROM venta")
version = cursor.fetchone()

print("Versión de SQLite:", version)

# Cerrar el cursor y la conexión para liberar recursos
cursor.close()
conexion.close()
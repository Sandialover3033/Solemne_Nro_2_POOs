import sqlite3

class UsuarioRepositorio:
    def __init__(self):
        self.config = "c:/proyectos/poos/ejemplo.db"

    def guardar(self, usuario):
        with sqlite3.connect(self.config) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Usuario (id,username,password) VALUES (?, ?, ?)",
                (usuario.id, usuario.username, usuario.password))
            conn.commit()
            cursor.close()

    def modificar(self, usuario):
        with sqlite3.connect(self.config) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE usuario SET username=?, password=? WHERE id=? ",
                (usuario.username, usuario.password, usuario.id))
            conn.commit()
            cursor.close()       

from cnsqlite3 import cnSqlite

class UsuarioRepositorio(cnSqlite):

    def guardar(self, usuario):
        sql = "INSERT INTO Usuario (id,username,password) VALUES (?, ?, ?)"
        datos = [usuario.id, usuario.username, usuario.password]
        super().Ejecutar(sql,datos)

    def modificar(self, usuario):
        sql = "UPDATE Usuario SET username=?, password=? WHERE id=?"
        datos = [usuario.username, usuario.password, usuario.id]
        super().Ejecutar(sql,datos)

    def eliminar(self, usuario):
        sql = "DELETE FROM Usuario WHERE id=?"
        datos = [usuario.id]
        super().Ejecutar(sql,datos)

    def buscar_por_id(self, idusuario):
        sql = "SELECT id, username, password FROM Usuario WHERE id=?"
        datos = [idusuario]
        fila = super().BuscaById(sql,datos)
        if fila is None: return None
        return fila

    
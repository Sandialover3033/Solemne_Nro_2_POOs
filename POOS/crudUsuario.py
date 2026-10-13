from usuario import Usuario
from usuario_repositorio_v2 import UsuarioRepositorio

oU = Usuario()
oUR = UsuarioRepositorio()

oU.id = 2
oU.username = "otrousuario"
oU.password = "321"

oUR.guardar(oU)
class Ejemplo:
    def __init__(self,codigo=None,descripcion=None,estado=None):
        self.codigo = codigo
        self.descripcion = descripcion
        self.estado = estado
        self.nomestado = False

    @property
    def estado(self):
        return self.estado
    
    @estado.setter
    def estado(self,nuevo):
        if nuevo==0:
            self.nomestado = False
        else:
            self.nomestado = True

# con los comandos @property y @___.setter 
# se puede controlar cuando se le asigna un valor a una propiedad 
# en el ejemplo, se configura el valor de una propiedad cuando se cambia el valor a otra propiedad 

oEjemplo = Ejemplo()
oEjemplo.estado = 1
print( oEjemplo.nomestado )
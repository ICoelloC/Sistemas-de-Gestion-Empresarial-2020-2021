from Personaje import Personaje


class Alien(Personaje):
    def __init__(self, nombre=""):
        super().__init__(nombre)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} ==> Nombre: {1}"
        return msg.format(clase, self.nombre)

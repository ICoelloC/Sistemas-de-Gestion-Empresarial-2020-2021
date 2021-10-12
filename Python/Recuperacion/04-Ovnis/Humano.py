from Personaje import Personaje
import random


class Humano(Personaje):
    def __init__(self, nombre="", pos_x=0, mundo=None):
        super().__init__(nombre, pos_x, mundo)

    def moverse(self):
        self.pos_x = random.randrange(-200, 200)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} ==> Nombre: {1}, Posicion: {2}"
        return msg.format(clase, self.nombre, self.pos_x)

import random
from Alien import Alien


class Ovni:
    def __init__(self, nombre="", pos_x=0, mundo=None):
        self.nombre = nombre
        self.pos_x = pos_x
        self.aliens = []
        self.mundo = mundo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, value):
        self.__pos_x = value

    @property
    def aliens(self):
        return self.__aliens

    @aliens.setter
    def aliens(self, value):
        self.__aliens = value

    @property
    def mundo(self):
        return self.__mundo

    @mundo.setter
    def mundo(self, value):
        self.__mundo = value

    def add_alien(self, alien):
        self.__aliens.append(alien)

    def moverse(self):
        self.pos_x = random.randrange(-200, 200)

    def abducir(self, persona):
        persona = Alien(persona.nombre)
        self.aliens.append(persona)

    def __str__(self):
        clase = type(self).__name__
        msg = "{1} ==> Nombre: {1}, Posicion: {2}\n\tAliens: \n"
        for a in self.aliens:
            msg += "\t\t" + a.__str__() + "\n"
        return msg.format(clase, self.nombre, self.pos_x)

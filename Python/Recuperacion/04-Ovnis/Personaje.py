class Personaje:
    def __init__(self, nombre="", pos_x=0, mundo=None):
        self.nombre = nombre
        self.pos_x = pos_x
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
    def mundo(self):
        return self.__mundo

    @mundo.setter
    def mundo(self, value):
        self.__mundo = value

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} ==> Nombre: {1}, Posicion: {2}"
        return msg.format(clase, self.nombre, self.pos_x)

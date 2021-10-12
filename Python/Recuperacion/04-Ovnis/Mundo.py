import random


class Mundo:
    def __init__(self, nombre=""):
        self.nombre = nombre
        self.objetos = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def objetos(self):
        return self.__objetos

    @objetos.setter
    def objetos(self, value):
        self.__objetos = value

    def add_objeto(self, nuevo_objeto):
        self.__objetos.append(nuevo_objeto)

    def quedan_humanos(self):
        supervivientes = False
        i = 0
        while not supervivientes and i < len(self.objetos):
            obj = self.objetos[i]
            if type(obj).__name__ == "Humano":
                supervivientes = True
                i += 1
        return supervivientes

    def comprobar_peligros_cerca(self):
        for o in self.objetos:
            if type(o).__name__ == "Humano":
                abducido = self.comprobar_peligro_persona(o)
                if abducido:
                    self.objetos.remove(o)

    def comprobar_peligro_persona(self, persona):
        for o in self.objetos:
            if type(o).__name__ == "Ovni" and abs(persona.pos_x - o.pos_x) == 0:
                prob = random.randrange(0, 100)
                if prob <= 20:
                    print(persona.nombre, " no ha sido abducida, se ha salvado por el 20% de probabilidad")
                    return False
                else:
                    print(persona.nombre, " ha sido abducido")
                    o.abducir(persona)
                    return True

    def actualizar_estado(self):
        self.comprobar_peligros_cerca()

    def ordenar_objetos(self):
        self.__objetos.sort(key=lambda objeto: objeto.pos_x)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} ==> Nombre: {1}\nObjetos: \n"
        for obj in self.objetos:
            msg += obj.__str__() + "\n"
        return msg.format(clase, self.nombre)

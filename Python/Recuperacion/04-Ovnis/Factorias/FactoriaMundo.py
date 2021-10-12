import random

from Factorias import FactoriaOvni
from Humano import Humano
from Mundo import Mundo


def crear_mundo(nombre_mundo="Mundo 1", num_humanos=7, num_ovnis=1):
    m = Mundo(nombre_mundo)
    for i in range(num_humanos):
        m.add_objeto(Humano("Humano #" + str(i), random.randrange(-200, 200), m))
    for i in range(num_ovnis):
        m.add_objeto(
            FactoriaOvni.crear_ovni("Ovni #" + str(i), random.randrange(1, 6), random.randrange(-200, 200), m))
    return m

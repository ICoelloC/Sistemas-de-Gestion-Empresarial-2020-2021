from Alien import Alien
from Ovni import Ovni


def crear_ovni(nombre_ovni, num_aliens, pos_x=0, mundo=None):
    p = Ovni(nombre_ovni, pos_x, mundo)
    for a in range(num_aliens):
        p.add_alien(Alien("alien #" + str(a)))
    return p

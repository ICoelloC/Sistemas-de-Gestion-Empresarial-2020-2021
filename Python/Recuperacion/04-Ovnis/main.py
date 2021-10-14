from Factorias import FactoriaMundo
from Utilidades import *

mundo = FactoriaMundo.crear_mundo("Mundo #1", 40, 10)


def simulacion(ubicacion):
    resumen = ""
    resumen += ubicacion.__str__()
    for objeto in ubicacion.objetos:
        objeto.moverse()
        mundo.actualizar_estado()
        resumen = ubicacion.__str__()
    return resumen


if __name__ == "__main__":
    bitacora = ""
    parar = input("Deseas parar (S o s para parar): ")
    seguir = parar not in ["S", "s"]
    while seguir and mundo.quedan_humanos():
        bitacora += simulacion(mundo)
        escribir_fichero(bitacora)
        parar = input("Deseas parar (S o s para parar): ")
        if parar in ["S", "s"]:
            seguir = False

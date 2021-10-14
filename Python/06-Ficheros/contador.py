from io import open
import sys

with open("contador.txt", "a+") as fichero:
    fichero.seek(0)
    contenido = fichero.readline()

    if len(contenido) == 0:
        contenido = "0"
        fichero.write(contenido)

# Vamos a intentar transformar el texto a un número
try:
    contador = int(contenido)

    # En función de lo que el usuario quiera...
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1

    print(contador)

    with open("contador.txt", "w") as fichero:
        fichero.write( str(contador) )
except:
    print("Error: Fichero corrupto.")
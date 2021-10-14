#!/usr/bin/env python
def crear_lista():
    numero = int(input("Número de palabras de la lista:"))

    if numero < 1:
        print("Error. Debe ser un número >= 1")
        return -1
    else:
        lista = []
        for i in range(numero):
            print("Palabra ", str(i + 1) + ": ", end="")
            palabra = input()
            lista.append(palabra)
        return lista

def borrar_repetidos(lista):
    #Vamos a eliminar los elementos repetidos
    for i in range(len(lista)-1,-1,-1): #La recorremos de forma inversa porque eliminamos repetidos
        if lista[i] in lista[:i]:
            del(lista[i])
    return lista

def elementos_comunes(lista1, lista2):
    return [i for i in lista1 if i in lista2]

def elementos_solo_una_lista(lista1,lista2):
    return [i for i in lista1 if i not in lista2]

primera = crear_lista()
primera = borrar_repetidos(primera)
print("Primera lista sin repetidos: ", primera)
segunda = crear_lista()
segunda = borrar_repetidos(segunda)
print("Segunda lista sin repetidos: ", segunda)
comunes = elementos_comunes(primera,segunda)
print("Palabras que aparecen en las dos listas: ", comunes)
elementosSoloPrimera = elementos_solo_una_lista(primera, segunda)
print("Palabras que aparecen sólo en la primera: ", primera)
elementosSoloSegunda = elementos_solo_una_lista(segunda, primera)
print("Palabras que aparecen sólo en la segunda: ", segunda)



#!/usr/bin/env python

# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
def iniciales(cadena):
    lista=cadena.split(" ")
    return "".join(palabra[0] for palabra in lista)

# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.
def capitalizar(cadena):
    lista = cadena.split(" ")
    return "".join(palabra.capitalize() + " " for palabra in lista)

# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.
def palabras_comienzan_a(cadena):
    lista = cadena.split(" ")
    return "".join(
        palabra + " "
        for palabra in lista
        if palabra.startswith("a") or palabra.startswith("A")
    )

cad=input("Cadena:")
print(iniciales(cad))
print(capitalizacion(cad))
print(palabras_comienzan_a(cad))

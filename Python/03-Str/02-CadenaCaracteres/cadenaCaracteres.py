#!/usr/bin/env python
cad1=input("Cadena 1:")
cad2=input("Cadena 2:")
if cad1.find(cad2)>-1:
    print ("cad2 es subcadena de cad1")
else:
    print ("cad2 no es subcadena de cad1")

print(min(cad1, cad2))
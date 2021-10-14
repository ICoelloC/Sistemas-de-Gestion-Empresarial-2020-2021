from io import open

with open('personas.txt','r', encoding="utf8") as fichero:
    lineas = fichero.readlines()
personas = []
for linea in lineas:
    # Borramos los saltos de línea y separamos
    campos = linea.replace("\n", "").split(";")
    persona = {"id":campos[0], "nombre":campos[1],
               "apellido":campos[2], "nacimiento":campos[3]}
    personas.append(persona)

for p in personas:
    print("(id={}) {} {} => {} ".format( p['id'], p['nombre'],
                                         p['apellido'], p['nacimiento']) )
def escribir_fichero(mundo):
    with open('bitacora.txt', 'w') as f:
        f.write(mundo.__str__()+"\n\n")

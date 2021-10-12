def escribir_fichero(mundo):
    f = open('bitacora.txt', 'w')
    f.write(mundo.__str__()+"\n\n")
    f.close()

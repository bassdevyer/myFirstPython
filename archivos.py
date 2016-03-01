def crearArchivo():
    archivo=open("datos.txt", "w")
    archivo.close()

def escribirArchivo():
    #modo a = append
    archivo = open('datos.txt', 'a')
    archivo.write("Miguel Torres\n")
    archivo.write("9203929393")
    archivo.close()


#crearArchivo()
escribirArchivo()
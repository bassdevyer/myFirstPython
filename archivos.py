def crearArchivo():
    archivo=open("datos.txt", "w")
    archivo.close()

def escribirArchivo():
    #modo a = append
    archivo = open('datos.txt', 'a')
    archivo.write("Miguel Torres\n")
    archivo.write("9203929393")
    archivo.close()

def leerArchivo():
    archivo = open("datos.txt", "r")
    linea = archivo.readline()
    while linea != "":
        print(linea)
        linea = archivo.readline()
    archivo.close()

#crearArchivo()
#escribirArchivo()
leerArchivo()
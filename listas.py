lista = ["Sara", "Pedro", 98, 76]
lista2 = ["Juan", 'David', 89]

print(len(lista))


for elemento in lista:
    print(elemento)

listaf = lista + lista2

print(listaf)

#Busqueda
if(55 in lista):
    print("Sí")
else:
    print("No")


#Manejar una lista por porciones
lista = ["Sara", "Pedro", 98, 76, "Juan", 'David', 89]

print(lista[1:4])

print(lista[1:])

print(lista[:4])
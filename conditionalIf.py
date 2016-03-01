edad = 19
pago = False

#Los parentesis son opcionales
if(edad > 18):
    print('Sí es mayor de edad')
    if pago == True:
        print('Entonces eres mayor y pagaste')
    else:
        print("Eres mayor de edad y no pagaste")
else:
    #La identacion es parte básica de python
    print("No es mayor de edad")

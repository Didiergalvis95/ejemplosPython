#Emule las operaciones basicas a eleccion del usuario

#sumar
sumar = lambda n1, n2: n1 + n2

#restar
restar = lambda n1, n2: n1 - n2

#multiplicar
multiplicar = lambda n1, n2: n1 * n2

#dividir
dividir|= lambda n1, n2: n1 / n2

#Menu para elegir la operacion

opcion = 1

while opcion != 0:
    opcion = int(input("Ingresa la opcion deseada: "))
    if opcion == 1:
        sumar(5, 10)
    elif opcion == 2:
        restar(5, 10)
    elif opcion == 3:
        multiplicar(5, 10)
    elif opcion == 4:
        dividir(5, 10)
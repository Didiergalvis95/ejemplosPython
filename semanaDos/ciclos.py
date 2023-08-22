print("Departamento de confección:")
print("1. Ingresar producto a fabricar.")
print("2. Mostrar inventario en fabrica.")
print("0. Salir.")
opcion = int(input("Ingresa una opcion: "))
listaProductos=[]

while opcion != 0:
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        productos = input("ingrese un producto: ")
        listaProductos.append(productos)
    elif opcion == 2:
        print(f"Este es el inventario: ")
        for producto in listaProductos:
            print(producto)
    elif opcion == 0:
        print("Hasta pronto!!!")
    else:
        print("Opcion invalida!!!")
    

# Desarrolla un algoritmo que permita agregar, eliminar y mostrar una lista de compras.

lista = ["papa", "yuca", "platano", "arroz", "leche", "huevos", "sal"]
print(lista)

opcion = int(input("¿Qué desea hacer con la lista de compras?:\n 1. Agregar\n 2. Eliminar\n 3. Mostrar\n"))

if opcion == 1:
    nuevo = input("Ingrese el nuevo elemento: ")
    lista.append(nuevo)
    print("Lista actualizada:", lista)

elif opcion == 2:
    print("Lista actual:", lista)
    eliminar = input("Ingrese el elemento que desea eliminar: ")
    if eliminar in lista:
        lista.remove(eliminar)
        print("Lista actualizada:", lista)
    else:
        print("Ese elemento no está en la lista.")

elif opcion == 3:
    print("Lista de compras:", lista)

else:
    print("Opción inválida.")

# Escribe un algoritmo que verifique si un elemento específico existe en una lista

lista = [2,5,7,2,6,8]

print(lista)
verificar = int(input("ingrese el numero que desea verificar: "))

resultado = verificar in lista

if resultado == True:
    print("el elemento esta en la lista")

else:
    print("el elemento no esta en la lista")
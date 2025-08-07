# Diseña un algoritmo que imprima la tabla de multiplicar de un número hasta 10

numero = int(input("ingrese un numero para mostrar su tabla de multiplicar: "))

for i in range (1,11):
    mult = numero * i 
    print(f"{numero} * {i} = {mult}")
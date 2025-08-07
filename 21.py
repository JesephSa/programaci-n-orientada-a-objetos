# Desarrolla un algoritmo que determine si un número dado es primo (solo divisible por 1
# y por sí mismo).

numero = int(input("ingrese un numero: "))

def primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            print("el numero no es primo")
            return
    print("el numero es primo")

primo(numero)

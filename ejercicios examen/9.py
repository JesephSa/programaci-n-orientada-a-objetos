# Desarrolla un algoritmo que simule el lanzamiento de un dado y devuelva un número
# aleatorio entre 1 y 6.
import random
x = "si"

while x == "si":
    numero = random.randint(1,6)

    if numero == 1:
        print("numero 1")

    elif numero == 2:
        print("numero 2")

    elif numero == 3:
        print("numero 3")

    elif numero == 4:
        print("numero 4")

    elif numero == 5:
        print("numero 5")

    elif numero == 6:
        print("numero 6")

    x = input("quiere volver a jugar (si/no)")
    print("\n")

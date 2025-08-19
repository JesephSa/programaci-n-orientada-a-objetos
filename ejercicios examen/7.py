# Escribe un algoritmo que verifique si hay asientos disponibles en un evento y reserve uno

disponibles = 6

if disponibles > 0:
    print("hay asientos disponibles")
    disponibles -= 1
    print("asiento reservado")
    print(f"quedan {disponibles} asientos disponibles")

else:
    print("no hay asientos disponibles")
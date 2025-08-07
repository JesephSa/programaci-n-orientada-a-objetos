# Implementa un algoritmo que clasifique a una persona en "Niño"(13),
# "Adolescente"(18), "Adulto" (+18) o "Adulto mayor"(65) según su edad.

edad = int(input("ingrese su edad: "))

if edad <= 13:
    print("usted es un niño")

elif edad <= 18:
     print("usted es un adolecente")

elif edad > 18 and edad < 65:
     print("usted es un adulto")

else:
     print("usted es adulto mayor")
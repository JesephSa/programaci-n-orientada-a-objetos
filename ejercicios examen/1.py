# Desarrolla un algoritmo que calcule la propina y el total a pagar en un restaurante, dado
# el monto de la cuenta y el porcentaje de propina.

monto = float(input("ingrese el monto de la cuenta: "))
propina = float (input("ingrese el porcentaje de la propina: "))

cuenta = monto * (propina / 100)
total = monto + cuenta

print(f"monto de la cuenta: {monto} \n Propina: {cuenta} \n Total a pagar: {total}")


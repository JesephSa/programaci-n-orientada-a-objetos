# # Crea un algoritmo que calcule el pago mensual de un préstamo, dado el monto, la tasa
# # de interés anual y el número de meses.

monto = float(input("ingrese el monto total del prestamo: "))
t_interes= float(input("ingrese la tasa de interes: "))
meses = int(input("ingrese el numero de meses del prestamo: "))

interes_total = monto * (t_interes / 100) *(meses / 12)
pago = (monto + interes_total) / meses

print(f"el pago mensual del prestamo es de ${pago}")
# Diseña un algoritmo que calcule el precio final de un producto después de aplicar un
# descuento.

neto = float(input("ingrese el precio neto del producto: "))
descuento = float(input("ingrese el porcentaje del descuento: "))

calculo= neto * (descuento / 100)
total = neto - calculo

print(f"el precio neto del producto es de ${neto}\n el descuento es del {descuento}% \n el precio final es de ${total} ")
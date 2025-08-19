#Diseña un algoritmo que calcule el costo total de un viaje, sumando el costo del
# combustible, el peaje y el alojamiento.

combustible = float(input("ingrese el costo del combustible: "))
num_peaje = int(input("ingrese el numero de peajes durante el viaje: "))
peaje = float(input("ingrese el costo del peaje: "))
alojamiento = float(input("ingrese el costo del alojamiento: "))

total = combustible + (num_peaje * peaje) + alojamiento

print(f"el costo del viaje es de ${total}")
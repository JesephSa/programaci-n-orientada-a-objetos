# . Desarrolla un algoritmo que verifique si la temperatura de una habitación está dentro de
# un rango aceptable (por ejemplo, entre 20°C y 25°C).

t_habitacion = float(input("ingrese la temperatura de la habitacion: "))

if t_habitacion >= 20 and t_habitacion <=25:
    print("rango aceptable de temperatura")

elif t_habitacion < 20:
    print("rango menor de temperatura")

else:
    print("rango mayor de temperatura")
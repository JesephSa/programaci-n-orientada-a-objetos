# Implementa un algoritmo que convierta una temperatura de grados Celsius a
# Fahrenheit.

celsius = float(input("ingrese la temperatura en grados celcius para convertilo en grados fahrenheit: "))

formula = (celsius * 9/5) + 32

print(f"{celsius}° celsius son {formula}° fahrenheit")
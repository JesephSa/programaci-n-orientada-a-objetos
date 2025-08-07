# Escribe un algoritmo que calcule el IMC de una persona a partir de su peso (kg) y altura (metros).

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

print(f"su indice de masa corporal es {imc}")
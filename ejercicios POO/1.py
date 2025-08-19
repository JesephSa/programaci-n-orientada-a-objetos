#Crea una clase Racional que permita trabajar con números racionales (fracciones). Incluye los siguientes métodos: constructores (por defecto y parametrizado), accedentes, leer(), suma, resta, multiplicación, división.

class racional:
    def __init__(self, numerador = 0, denominador = 1):
        self.numerador = numerador
        self.denominador= denominador

    def leer (self):
        self.numerador = int(input("Ingrese el numerador: "))
        self.denominador = int(input("Ingrese el denominador: "))

    def suma (self, fraccion):
        num = self.numerador *fraccion.denominador + fraccion.numerador * self.denominador
        den = self.denominador * fraccion.denominador
        return racional(num,den)
    
    def resta (self, fraccion):
        num = self.numerador *fraccion.denominador - fraccion.numerador * self.denominador
        den = self.denominador * fraccion.denominador
        return racional(num,den)
    
    def multiplicacion (self, fraccion):
        num = self.numerador * fraccion.numerador
        den = self.denominador * fraccion.denominador
        return racional(num,den)
    
    def division (self, fraccion):
        num = self.numerador * fraccion.denominador
        den = self.denominador * fraccion.numerador
        return racional(num,den)
    
    def mostrar (self):
        return f"{self.numerador}/{self.denominador}"

r1 = racional(3,4)
r2 = racional(5,6)

print(f"R1 = {r1.mostrar()}")
print(f"R2 = {r2.mostrar()}")
print(f"Sumar = {r1.suma(r2).mostrar()}")
print(f"Restar = {r1.resta(r2).mostrar()}")
print(f"Multiplicar = {r1.multiplicacion(r2).mostrar()}")
print(f"Dividir = {r1.division(r2).mostrar()}")


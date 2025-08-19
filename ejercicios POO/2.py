#Crea una clase Cuenta (bancaria) con atributos para el número de cuenta (un entero largo), el DNI del cliente (otro entero largo), el saldo actual y el interés anual que se aplica a la cuenta (porcentaje). Define en la clase los siguientes métodos:
# — Constructor por defecto y constructor con DNI, saldo e interés
# - Accedentes y mutadores. Para el número de cuenta no habrá mutador.
# - actualizarSaldo(): actualizará el saldo de la cuenta aplicándole el interés diario (interés anual dividido entre 365 aplicado al saldo actual).
# - ingresar(double): permitirá ingresar una cantidad en la cuenta.
# - retirar(double): permitirá sacar una cantidad de la cuenta (si hay saldo). –
# - Método que nos permita mostrar todos los datos de la cuenta.

class Cuenta:
    contador = 1
    def __init__(self, dni =0, saldo=0.0, interesA= 0.0):
        self.numerocuenta = Cuenta.contador
        Cuenta.contador +=1
        self.dni = dni
        self.saldo = saldo
        self.interesA = interesA

    #getters
    def getnumeroCuenta(self):
        return self.numerocuenta
    
    def getdni(self):
        return self.dni
    
    def getsaldo(self):
        return self.saldo
    
    def getinteresA (self):
        return self.interesA
    
    #setters
    def setdni(self, dni):
        self.dni = dni

    def setsaldo(self, saldo):
        self.saldo = saldo

    def setinteresA(self, interes):
        self.interesA = interes

    def actualizarsaldo(self):
        interesD = self.interesA / 365 / 100
        self.saldo += self.saldo * interesD

    def ingresar(self, cantidad):
        self.saldo += cantidad

    def retirar (self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("No hay saldo suficiente")

    def mostrar (self):
        return(f"Numero de cuenta: {self.numerocuenta}\n DNI: {self.dni} \n Saldo: {self.saldo} \n Interes anual: {self.interesA}%")

Cuenta1 = Cuenta(123456, 1000, 3.5) 
print(Cuenta1.mostrar())

Cuenta1.ingresar(500)

Cuenta1.retirar(200)

Cuenta1.actualizarsaldo()

print(Cuenta1.mostrar())
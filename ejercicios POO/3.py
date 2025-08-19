#Crea las siguientes clases :
# - Motor: con métodos para arrancar el motor y apagarlo.
# - Rueda: con métodos para inflar la rueda y desinflarla. Ventana: con métodos para abrirla y cerrarla.
# - Puerta: con una ventana y métodos para abrir la puerta y cerrar la puerta.
# - Coche: con un motor, cuatro ruedas y dos puertas; con los métodos que te parezcan adecuados

class motor:
    def arrancar (self):
        print("El motor está arrancando...")

    def apagar (self):
        print("El motor se está apagando...")

class rueda:
    def inflar (self):
        print("Se está inflando la rueda...")

    def desinflar (self):
        print("La rueda se está desinflando...")

class ventana:
    def abrir(self):
        print("La ventana se está abriendo...")

    def cerrar(self):
        print("La ventana se está cerrando...")

class puerta:
    def __init__(self):
        self.ventana = ventana()

    def abrir(self):
        print("La puerta está abierta...")

    def cerrar(self):
        print("La puerta está cerrada...")

class coche:
    def __init__(self):
        self.motor = motor()
        self.ruedas = [rueda() for i in range(4)]
        self.puertas= [puerta() for i in range(2)]

    def arrancar(self):
        self.motor.arrancar()

    def apagar(self):
        self.motor.apagar()

    def inflar(self):
        for i, rueda in enumerate(self.ruedas, 1):
            print(f"Rueda {i}: ",end="")
            rueda.inflar()

    def abrirp(self):
        for i, puerta in enumerate(self.puertas, 1):
            print(f"Puerta {i}: ",end="")
            puerta.abrir()

    def cerrarp(self):
        for i, puerta in enumerate(self.puertas,1):
            print(f"Puerta {i}: ",end="")
            puerta.cerrar()

mi_coche= coche()

mi_coche.arrancar()

mi_coche.inflar()

mi_coche.abrirp()
mi_coche.puertas[0].ventana.abrir()
mi_coche.puertas[1].ventana.abrir()

mi_coche.apagar()
#ZeroDivisionError
try:
    numero = 239
    division= 0
    print(numero//division)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

#IndexError
try:
    lista=["pedro","luna","armando"]
    print(lista[10])
except IndexError:
    print("Error: No esta en el rango")

#NameError
try:
    print(edad)
except NameError:
    print("Error: no se ha definido")

#TypeError
try:
    resultado = (1,3,4,5)+10
except TypeError:
    print("Error: no se puede sumar eso")

#ModuleNotFoundError
try:
    import matematicas
except ModuleNotFoundError:
    print("Error: El modulo no existe")

# OverflowError
try:
    numero = 4.23**12345678765432
except OverflowError:
    print("Error: numero demasiado grande")

# KeyError
try:
    inventario = {"arroz":12, "Platano":8, "Frijoles":21}
    print(inventario["lentejas"])
except KeyError:
    print("Error: Lo buscado no está en el inventario")

#excepcion multiple
try:
    archivo = open('archivo_no_encontrado', 'r')
    contenido = archivo.read()
    resultado = 20/0
except FileNotFoundError:
    print("Error: No se encontro el archivo")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

# Escribir archivo
with open("saludo.txt", "w") as f:
    f.write("Hola mundo\n")
    f.write("Python es genial\n")

# Leer archivo
with open("saludo.txt", "r") as f:
    for linea in f:
        print(linea.strip())
# Escribe un algoritmo que tome una lista de canciones y devuelva una lista de
# reproducción en orden aleatorio.
import random
canciones = ["En su nota", "Chambonea", "Ensendia", "Una Aventura", "No dice na", "Despues de las 12"]

random.shuffle(canciones)

print(canciones)
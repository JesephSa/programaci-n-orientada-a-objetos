# Implementa un algoritmo que encuentre los elementos comunes entre dos listas

a = [1,2,5,3,9]
b = [9,8,7,6,3]

comun = set(a) & set(b)

if comun: 
    print(f"tiene elementos comunes: {comun}")

else:
    print("no tiene elementos comunes")

# Crea un algoritmo que tome una lista de nombres y fechas de cumpleaños y los organice
# por mes.

cumpleaños = [
    ("sofia","2005-04-12"),
    ("Luis", "2003-12-30"),
    ("Carlos", "1999-04-07"),
    ("María", "2001-02-05"),
    ("Isabella","2008-08-06")
]

c_mes = {}

for nombre, fecha in cumpleaños:
    mes = int(fecha.split("-")[1]) #devuelve las subcadenas de la lista 

    if mes not in c_mes:
        c_mes[mes] = []

    c_mes[mes].append(nombre)

for mes in sorted(c_mes):
    print(f"Mes {mes}: {c_mes[mes]}")
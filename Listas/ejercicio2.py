nombres = []
apellidos = []

for i in range(3):
    nombre = input(f"Ingrese nombre N° {i+1}: ")
    nombres.append(nombre)

for i in range(3):
    apellido = input(f"Ingrese Apellido N° {i+1}: ")
    apellidos.append(apellido)

print("Listado ordenado de Nombre y apellido")
for i in range(3):
    if i < 3:
        print(f"-{nombres[i]} {apellidos[i]}")
        
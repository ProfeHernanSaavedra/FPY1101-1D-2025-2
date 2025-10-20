agenda = {}

for i in range(3):
    nombre = input("Ingrese nombre del contacto: ")
    telefono = int(input("Ingrese número de telefono: "))
    agenda[nombre] = telefono

print("Agenda Telefonica")
for nombre,telefono in agenda.items():
    print(nombre,":",telefono)
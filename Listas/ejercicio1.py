nombres = [] # definicion de lista llamada nombres

for i in range(3):
    nombre = input(f"Ingrese nombre N°{i+1}: ")
    nombres.append(nombre)

mayor = nombres[0]
for nombre in nombres:
    if len(nombre) > len(mayor):
        mayor = nombre

print("Nombres ingresados: ",nombres)
print("Nombre con mas caracteres : ",mayor)


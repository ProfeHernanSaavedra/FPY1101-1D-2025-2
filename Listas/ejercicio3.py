nombres = []

while True:
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

    seguir = input("¿Desea agregar otro nombre? (si/no): ").lower()
    if seguir == "no":
        break

menor = nombres[0]
for nom in nombres:
    if len(nom) < len(menor):
        menor = nom

nombres.remove(menor)
print(f"Se elimino '{menor}' ya que es el nombre mas corto")
print("Lista final: ",nombres)

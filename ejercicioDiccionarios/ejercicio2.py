empresa = {
    "nombre" : "MOP",
    "ciudad" : "Valparaiso",
    "rubro" : "Infraestructura"
 }

clave = input("Ingrese la clave que desea buscar: ")

if clave in empresa:
    print("La clave existe!!")
else:
    print("La clave no existe!!")

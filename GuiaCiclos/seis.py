texto = input("Ingrese un texto: ")
vocales = "aeiouáéíóú"

contador = 0

for c in texto.lower():
    if c in vocales:
        contador = contador + 1

print("Cantidad de vocales " , contador)


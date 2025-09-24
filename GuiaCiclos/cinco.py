contador = 0
suma = 0
while True:
    num = input("Ingrese un número o 'fin' para terminar: ")
    if num.lower() == "fin":
        break
    try:
        num = float(num)
        suma = suma + num
        contador = contador + 1
    except ValueError:
        print("El numero ingresado no es válido, vuelva a ingresar")

if contador > 0 :
    prom = suma / contador
    print("El promedio es: ",prom)
else:
    print("No se ingresaro numeros válidos")


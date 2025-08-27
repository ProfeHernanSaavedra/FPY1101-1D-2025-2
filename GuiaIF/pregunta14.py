print("Menu")
print("****")
print("1. Suma")
print("2. Resta")
print("3. Multiplicar")
print("4. Dividir")

op = int(input("Ingrese opcion: "))
print("Ingrese dos numeros")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))


if op == 1:
    print("Sumar")
    suma = num1 + num2
    print("suma: ", suma)
elif op == 2:
    print("Restar")
    resta = num1 - num2
    print("resta : ",resta)
elif op == 3:
    print("Multiplicar")
    multi = num1 * num2
    print("Multiplcar : ",multi)

elif op == 4:
    print("Dividir")
    div = num1 / num2
    print("Dividir : ",div)

else:
    print("Opción no válida!")
num = int(input("Ingrese un número entero: "))

if num == 0:
    print("tiene 1 digito")
else:
    digitos = 0
    while num > 0:
        digitos = digitos + 1
        num //= 10 # cantidad entera de dividir por 10 el digito
        print(num)
    print("Cantidad de dígitos : ",digitos)

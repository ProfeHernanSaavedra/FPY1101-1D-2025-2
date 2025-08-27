num1 = int(input("Ingrese número 1: "))
num2 = int(input("Ingrese número 2: "))
num3 = int(input("Ingrese número 3: "))

# mayor = num1

# if num2 > mayor:
#     mayor = num2

# if num3 > mayor:
#     mayor = num3

#print("Mayor es : ",mayor)

if num1 > num2 and num1 > num3:
    print("El numero mayor es ",num1)
else:
    if num2 > num1 and num2 > num3:
        print("El mayor es ",num2)
    else:
        print(f"El mayor es {num3}")
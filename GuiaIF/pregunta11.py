import random as rd

#num = int(input("Ingrese un número: "))

num = rd.randint(1,100)

print(num)
if num >= 10 and num <= 50:
    print("Dentro del rango entre 10-50")
else:
    print("Fuera de rango entre 10-50")
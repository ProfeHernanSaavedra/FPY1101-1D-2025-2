import random as rand

numSecreto = rand.randint(1,3)

num = int(input("Ingrese un número entre 1 y 3: "))
print(numSecreto)
if num > numSecreto:
    print("El numero que ingresaste es mayor")
else:
    if num < numSecreto:
        print("el numero ingresaste es menor")
    else:
        if num == numSecreto:
            print("Adiviniaste es igual!!")
        
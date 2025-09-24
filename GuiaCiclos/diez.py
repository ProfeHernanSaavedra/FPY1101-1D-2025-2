N = int(input("Ingrese termino de la serie de Fibonacci: "))

a = 0
b = 1
contador = 0
while contador < N :
    print(a,end=" ")

    siguiente = a + b
    a = b
    b = siguiente

    contador = contador + 1
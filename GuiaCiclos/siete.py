sumaPares = 0
sumaImpares = 0
cantidadNum = int(input("Ingrese cantidad de numeros: "))

for i in range(1,cantidadNum+1):
    if i%2 == 0:
        sumaPares = sumaPares + i
    else:
        sumaImpares = sumaImpares + i

print("Suma pares: ",sumaPares) 
print("Suma impares: ",sumaImpares) 
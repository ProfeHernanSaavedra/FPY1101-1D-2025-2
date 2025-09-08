contPar = 0
contImPar = 0
mayorCien = False
par = False

num1 = int(input("Ingrese numero: "))
num2 = int(input("Ingrese numero: "))
num3 = int(input("Ingrese numero: "))

suma = num1+num2+num3

if num1%2==0 :
    contPar = contPar + 1
else:
    contImPar = contImPar + 1

if num2%2 ==0 :
    contPar = contPar + 1
else:
    contImPar = contImPar + 1

if num3%2 ==0 :
    contPar = contPar + 1
else:
    contImPar = contImPar + 1

#suma de los numeros > 100
if suma > 100:
    mayorCien = True
    if suma%2 ==0 :
        par = True


print(f"Se ingresaron {contPar} números par(es)")
print(f"Se ingresaron {contImPar} números impar(es)")

if mayorCien == True:
    print("La suma es mayor a 100")
else:
    print("La suma no es mayor a 100")

if par == True:
    print("La suma es par")
else:
    print("La suma impar")

print()
print("----OTRA FORMA----")
print("---SUMA 100-------")
if suma > 100:
    print("La suma es mayor a 100")
    if suma%2 == 0 :
        print("La suma es par")
    else:
        print("La suma es impar")
else:
    print("La suma no es mayor a 100")
    if suma%2 == 0 :
        print("La suma es par")
    else:
        print("La suma es impar")

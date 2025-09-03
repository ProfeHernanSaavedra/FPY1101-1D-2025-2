# string o cadena de caracteres
# h  o  l  a
# 0  1  2  3
#palabra = "hola" --> palabra[0] = h
#palabra = "hola" --> palabra[3] = a
# palabra [0:3] --> hol
#palabra[1:2] --> o
# palabra = "hola"
# print(palabra[0:3])
# print(palabra[1:2])

# num = 55/30 ---> división normal
# num2 = 55//30 ---> división absoluta , entrega el entero
# print(round(num)) ---> redondea el resultado de la división
# print(num)
# print(num2)

horaIngreso = input("Ingrese hora de ingreso en formato hh:mm: ")
horaSalida = input("Ingrese hora de salida en formato hh:mm: ")

h1 = int(horaIngreso[0:2])
m1 = int(horaIngreso[3:5])
# print(h1)
# print(m1)
h2 = int(horaSalida[0:2])
m2 = int(horaSalida[3:5])

#convertir a minutos
min1 = h1 *60 + m1
min2 = h2 * 60 + m2

totalMin = min2 - min1
print(totalMin)
if totalMin <= 0:
    print("Hora Inválida")
elif totalMin <= 10:
    print("Total a pagar $0")
elif totalMin < 30:
    print("Total a pagar $0")
else:
    #calcular
    bloques = totalMin // 30  #3.33---> 3 
    if totalMin %30 != 0:
        bloques = bloques + 1
    total = bloques *700
    print("Total a pagar es : $",total)



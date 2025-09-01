dia = int(input("Ingrese dia: "))
mes = int(input("Ingrese mes: "))
año = int(input("Ingrese año: "))

#validar año y mes
if año < 1900 or año >2100 or mes <1 or mes >12 or dia < 1:
    valido = False
else:

    #determinar si el año bisiesto
    if (año % 400 == 0 ) or (año % 4 ==0 and año % 100 != 0):
        bisiesto = True
    else:
        bisiesto = False
    
    # determinar dias máximos del mes
    if mes == 2:
        if bisiesto:
            maxDias = 29
        else:
            maxDias = 28
    else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            maxDias = 31
        else:
            maxDias = 30
    
    # validar el dia
    if dia <= maxDias:
        valido = True
    else:
        valido = False

if valido:
    print("Fecha válida")
else:
    print("Fecha inválida")
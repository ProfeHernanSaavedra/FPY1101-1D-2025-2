ladoA = float(input("Ingrese lado a: "))
ladoB = float(input("Ingrese lado b: "))
ladoC = float(input("Ingrese lado c: "))

if ladoA <= 0 or ladoB <= 0 or ladoC <=0 :
    print("No es triángulo")

else:
    if ladoA == ladoB and ladoB == ladoC:
        print("Tipo: Equilátero")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Tipo: Isósceles")
    else:
        print("Tipo: Escaleno")

    if ladoA**2 == (ladoB**2 + ladoC**2) or ladoB**2 == (ladoA**2 + ladoC**2) or ladoC**2 == (ladoB**2 + ladoA**2):
        print("Rectangulo")




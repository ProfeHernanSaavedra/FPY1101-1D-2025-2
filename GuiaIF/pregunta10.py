temperatura = float(input("Ingrese temperatura en °C: "))

if temperatura < 0 :
    print("Congelado")
elif temperatura >=0 and temperatura <= 20 :
    print("Frío")
elif temperatura >=21 and temperatura <= 30:
    print("Agradable")
else:
    print("Caluroso")

    
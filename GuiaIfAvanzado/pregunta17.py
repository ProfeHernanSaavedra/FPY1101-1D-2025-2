print("Plan Base $12.000 inlcuye 100 min y 5 GB")
print("****************************************")

minutos = int(input("Ingrese minutos: "))
gb = float(input("Ingrese GB: "))
roaming = int(input("Ingrese si uso roaming (1-si) (0-no): "))

total = 12000

extra_min = minutos - 100
if extra_min < 0:
    extra_min = 0

extra_gb = gb - 5
if extra_gb <= 0:
    gb_cobrados = 0
else:
    entero = int(extra_gb)
    if extra_gb > entero:
        gb_cobrados = entero + 1
    else:
        gb_cobrados = entero

#excedentes
total = total + (extra_min * 50)
total = total + (gb_cobrados * 1000)

# roaming
if roaming == 1 and (minutos > 0 or gb > 0):
    total = total + 7000

print("Total a pagar : $",total)


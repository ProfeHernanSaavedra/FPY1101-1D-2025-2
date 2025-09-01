consumo = int(input("Ingrese KWh de consumo: "))

if consumo > 0 and consumo <= 100:
    total = consumo * 120
elif consumo >=101 and consumo <= 300:
    total = consumo * 150
else:
    total = consumo *200

if total > 60000:
    desc = total *0.1
    total = total - desc

if total < 5000:
    total = 5000

print("Su total a pagar es: $",total)    
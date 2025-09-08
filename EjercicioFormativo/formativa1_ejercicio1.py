# n1 30 , n2 40 , n3 30
nota1= float(input("Ingrese nota de la EA1: "))
nota2= float(input("Ingrese nota de la EA2: "))
nota3= float(input("Ingrese nota de la EA3: "))
prom = nota1*0.3+nota2*0.4+nota3*0.3
# 0.3  ---> 30/100 = 0.3
print("El promedio de presentación final es: ",round(prom,1))

notaEx = float(input("Ingrese nota del examen: "))

promFinal = prom*0.6+notaEx*0.4

print("Su promedio final es: ",round(promFinal,1))


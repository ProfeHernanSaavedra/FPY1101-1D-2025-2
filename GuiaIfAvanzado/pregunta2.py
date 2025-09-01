print("USM")
nota1 = int(input("Ingres nota 1 (0-100): "))
nota2 = int(input("Ingres nota 2 (0-100): "))
nota3 = int(input("Ingres nota 3 (0-100): "))

promedio = (nota1+nota2+nota3)/3

if promedio >= 60 and nota1 >= 50 and nota2 >= 50 and nota3 >= 50:
    print("Eximido")

elif promedio >= 55 and promedio <= 59:
    print("Recuperativa")

elif nota1 < 40 or nota2 < 40 or nota3 < 40:
    print("Reprobado directo")

else:
    print("Reprobado") 

print()
print("DUOC")
nota1 = float(input("Ingrese nota 1 (1-7): "))
nota2 = float(input("Ingrese nota 2 (1-7): "))
nota3 = float(input("Ingrese nota 3 (1-7): "))

promedio = nota1*0.3+nota2*0.3+nota3*0.4

if promedio >= 4 and nota1 >= 4 and nota2 >= 4 and nota3 >= 4:
    print("Aprobado")

elif nota1 < 4 or nota2 < 4 or nota3 < 4:
    print("Reprobado directo")

else:
    print("Reprobado") 
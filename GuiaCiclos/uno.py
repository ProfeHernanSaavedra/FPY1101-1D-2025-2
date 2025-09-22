n = int(input("Ingrese un número entero: "))
suma = 0

for i in range(1,n+1):
    print(i)
    suma = suma + i # suma +=i

print(f"la suma del 1 al {n} es: {suma}")

#for i in range(1,3+1):  el 3 + 1 es pq llega al 2 si coloco 3
#    print(i)
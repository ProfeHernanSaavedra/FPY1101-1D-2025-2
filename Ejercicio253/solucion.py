deuda = 100000 #deuda inicial

while True:
    print("---MENU---")
    print("1. Pagar Tarjeta de Crédito")
    print("2. Simular Compra")
    print("3. Salir")
    try:
        opc = int(input("Seleccione su opción: "))
   
        if opc == 1 :
            monto = int(input("Ingrese monto a pagar: "))
            if deuda == 0:
                print("No tiene deuda")
            elif monto < 0:
                print("El monto no puede ser menor que cero")
            elif monto > deuda:
                print("El monto no puede ser mayor que la deuda")
            else:
                deuda = deuda - monto
                print("El monto ahora de la deuda es: $",deuda)
        elif opc == 2:
            print("Simular compra")
            cantidadCompras = int(input("Ingrese cantidad de compras: "))
            if cantidadCompras <= 0 :
                print("La cantida de compras debe ser mayor a cero")
            else:
                for i in range(cantidadCompras):
                    monto= int(input(f"Ingrese el monto de la compra {i+1}: "))
                    if monto <0 :
                        print("El monto no puede ser negativo")
                    else:
                        deuda = deuda + monto
                        print(f"Compra {i+1} realizada. Deuda actual ${deuda}")

        elif opc == 3:
            print("Gracias por usar la tarjeta MasterPlop!")
            break
    except ValueError:
        print("Debe ingresar un valor numerico")    

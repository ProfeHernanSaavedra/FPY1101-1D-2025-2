pikachu = 0
otaku = 0
pulpo = 0
anguila = 0
while True:
    print("Seleccion opcion")
    print("1. Pikachu Roll ($4500)")
    print("2. Otaku Roll ($5000)")
    print("3. Pulpo Venenoso Roll ($5200)")
    print("4. Anguila Eléctrica Roll ($4800)")
    print("5. Finalizar pedido")

    try:
        opcion = int(input("Ingrese su opción: (1-5)"))

    except ValueError:
        print("Debe ingresar un número entre 1 y 5")
        continue

    if opcion == 1:
        pikachu = pikachu + 1 #--> esto es lo mismo--> picachi += 1
        print("Has agregado un Pikachu Roll")
    elif opcion == 2:
        otaku = otaku + 1
        print("Has agregado un Otaku Roll")
    elif opcion == 3:
        pulpo = pulpo + 1
        print("Has agregado un Pulpo Venenoso Roll")
    elif opcion == 4:
        anguila = anguila + 1 
        print("Has agregado un Anguila Eléctrica Roll")
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Intente nuevamente")

subtotal = (pikachu * 4500) + (otaku * 5000) + (pulpo*5200) + (anguila*4800)
#print(subtotal)
codigo_Valido = False
if subtotal > 0:
    print("Posee código de descuento: ")
    resp  =input("Si (s) o No (n):  ").lower()

    if resp == "s":
        while True:
            codigo = input("Ingrese código: ")
            if codigo == "soyotaku":
                descuento = subtotal * 0.1
                codigo_Valido = True
                break
            else:
                print("Código no válido")
                opcion_codigo = input("Teclee X para salir o cualquier tecla para reintentar").lower()
                if opcion_codigo == "x":
                    break

total = subtotal - descuento
print("*******************************")
print("         DETALLE PEDIDO        ")
print("*******************************")
print("Pikachu Roll: ",pikachu)
print("Otaku Roll: ", otaku)
print("Pulpo venenoso Roll: ",pulpo)
print("Anguila Eléctrica Roll: ",anguila)
print("*******************************")
print("Sub total por pagar es: $",subtotal)
if codigo_Valido:
    print("Descuento por código $",descuento)
else:
    print("Descuento $0")
print("TOTAL: $ ",total)
print("********************************")

opcion_repetir = input("Desea realizar otro pedido? (S/N): ").lower()
if opcion_repetir == "s":
    print("Reinicie el sistema")
else:
    print("Gracias por comprar en sushy Py!")

    
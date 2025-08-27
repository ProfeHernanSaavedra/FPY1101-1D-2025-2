montoCompra = int(input("Ingrese monto de compra: $"))

descuento = 0

if montoCompra > 100000:
    descuento = montoCompra *0.2
    total = montoCompra - descuento
else:
    if montoCompra >50000 and montoCompra <= 100000:
        descuento = montoCompra *0.1
        total = montoCompra - descuento
    else:
        total = montoCompra

#total = montoCompra - descuento

print("El Valor de la boleta es: $",montoCompra)
print("El descuento es:          $",descuento)
print("                          ------------")
print("El total a pagar es:     $",total)
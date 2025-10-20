bodega = {
    "martillo" : 12,
    "clavos" : 250,
    "pintura" : 8
}

bodega["martillo"] = bodega["martillo"] - 2
bodega["clavos"] = bodega["clavos"] - 50

if "lijas" not in bodega:
    bodega["lijas"] = 20

print("Stock total")
for clave,valor in bodega.items():
    print(clave,":",valor)
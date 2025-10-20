empleado ={
    "nombre":"Juan",
    "cargo":"Programador",
    "sueldo":800000
}

print("Nombre es: ",empleado["nombre"])
print("Cargo es: ",empleado["cargo"])
print("Sueldo es :$",empleado["sueldo"])

# si el sueldo fuera "sueldo":"800000"
#total = int(empleado["sueldo"]) * 10
#print(total)

#empleado["departamento"] = input("Ingrese departamento: ")

depto = input("Ingrese departamento: ")
empleado["departamento"] = depto

print("\nDatos del diccionario")
for clave,valor in empleado.items():
    print(clave,":",valor)



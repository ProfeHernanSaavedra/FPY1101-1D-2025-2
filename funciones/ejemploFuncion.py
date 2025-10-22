import funciones as fn
#ejecutando o llamando a la función
fn.saludo()
fn.saludo2("Juan")
print(fn.sumar())
print(fn.restar(7,4))
num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese numero 2: "))
print(f"La resta de {num1} - {num2} = {fn.restar(num1,num2)}" )
fn.saludo3(mensaje="Buen dia",nombre="Pedro")
usuario1= None 
usuario2=None 
usuario3=None
contrasena1= None 
contrasena2=None 
contrasena3= None

sesionIniciada = False

while True:
    print("----MENU----")
    print("1. Iniciar Sesión")
    print("2. Registrar usuario")
    print("3. Salir")

    try:
        opcion = int(input("Seleccione la opción: "))
    except:
        print("Error, debe ingresa un número")
        continue

    if opcion == 1:
        if usuario1 is None and usuario2 is None and usuario3 is None:
            print("Debe ingresar un usuario antes de iniciar sesion")
            continue
        usuario = input("Ingrese usuario: ")
        contrasena = input("Ingrese contraseña: ")

        if(usuario == usuario1 and contrasena == contrasena1) or \
        (usuario == usuario2 and contrasena == contrasena2) or \
        (usuario == usuario3 and contrasena == contrasena3):
            print("Inicio de sesión correcta! ")
            sesionIniciada = True

            while sesionIniciada:
                print("---MENU DE USUARIO---")
                print("1. Realizar Llamada")
                print("2. Enviar correo electrónico")
                print("3. Cerrar Sesión")

                try:
                    opcion2 = int(input("Seleccione una opción: "))

                except:
                    print("Error debe ingresar un número!")
                    continue

                if opcion2 == 1:
                    celular = input("Ingrese número de celular(9 dígitos, comience con 9): ")
                    if len(celular) == 9 and celular.isdigit() and celular.startswith("9"):
                        print("Llamandpo al celular : " ,celular)
                    else:
                        print("Error!, número celular no es correcto")
                
                elif opcion2 == 2:
                    correo = input("Ingrese su correo: ")
                    valido = False
                    for caracter in correo:
                        if caracter == "@":
                            valido = True
                    if valido:
                        mensaje = input("Ingrese el mensaje de correo: ")
                        print(f"Correo enviado a {correo} con mensaje: {mensaje}")
                    else:
                        print("Error!, correo no válido")
                elif opcion2 == 3:
                    print("Cerrar Sesión")
                    sesionIniciada = False
                else:
                    print("Opción no válida")
        else:
            print("Usuario o contraseña incorrectos!")
    
    elif opcion == 2:
        nuevoUsuario = input("Ingrese nuevo usuario: ")
        nuevaContraseña = input("Ingrese nueva contraseña: ")

        if usuario1 is None:
            usuario1 = nuevoUsuario
            contrasena1 = nuevaContraseña
        elif usuario2 is None:
            usuario2 = nuevoUsuario
            contrasena2 = nuevaContraseña
        elif usuario3 is None:
            usuario3 = nuevoUsuario
            contrasena3 = nuevaContraseña
        else:
            print("Error al ingresar usuarios, máximo 3")

    elif opcion == 3:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")





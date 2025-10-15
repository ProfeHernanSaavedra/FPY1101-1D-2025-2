usuarios = []
contrasenas = []

while True:
    print("---MENU---")
    print("1. Iniciar sesión")
    print("2. Registrar usuarios")
    print("3. Eliminar usuario")
    print("4. Salir")
    op = int(input("Elija su opción: "))

    if op == 1:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")

        #buscar usuario
        i = 0
        encontrado = False
        while i < len(usuarios):
            if usuarios[i] == usuario and contrasenas[i] == contrasena:
                encontrado = True
                break
            i = i + 1 # i += 1

        if encontrado:
            print("Inicio de sesión exitosa!")
        else:
            print("Usario o contraseña incorrectos!")
        
    elif op == 2:
        usuario = input("Nuevo usuario: ")
        #verificar si existe usuario en la lista de usuarios
        existe = False
        i = 0
        while i < len(usuarios):
            if usuarios[i] == usuario:
                existe = True
                break
            i = i + 1
        if existe:
            print("Usuario ya existe")
            continue
        usuarios.append(usuario)
        contrasena = input("Contraseña: ")
        contrasenas.append(contrasena)
        print("Usuario registrado correctamente!")

    elif op == 3:
        usuario = input("Usuario a eliminar: ")
        contrasena = input("Confirme contraseña para eliminar: ")

        i = 0
        eliminado = False
        while i < len(usuarios):
            if usuarios[i] == usuario and contrasenas[i] == contrasena:
                #eliminar
                usuarios.pop(i)
                contrasenas.pop(i)
                eliminado = True
                break
            i = i + 1
        if eliminado:
            print("Usuario eliminado correctamente")
        else:
            print("No se puedo eliminar el usuario, ya que no coinciden o no existe usuario/contraseña")
        
    elif op == 4:
        print("Gracias....")
        break
    else:
        print("Opción no válida")
while True:
    try:
        nota = float(input("Ingrese una nota entre 1 y 7: "))
    
        if nota >= 1 and nota <= 7:
            print("nota válida")
            break
        else:
            print("Nota inválida, vuelva a ingresar")
    except ValueError:
        print("Debe ingresar números, vuelva a intentar")
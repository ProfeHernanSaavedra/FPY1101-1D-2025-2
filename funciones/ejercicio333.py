def validar_lista_numeros(texto):
    valido = False
    while not valido:
        lista = texto.split()
        numeros = []
        valido = True  # asumimos que es válida, pero comprobamos
        for x in lista:
            if x.isdigit() or (x.startswith('-') and x[1:].isdigit()):
                numeros.append(int(x))
            else:
                valido = False
                break

        if valido == False:
            print("Entrada inválida. Ingrese solo números enteros separados por espacios.")
            texto = input("Ingrese nuevamente: ")
        else:
            return numeros



def separar_pares_impares(lista):
    """
    Recibe una lista de números y devuelve dos listas:
    una con los pares y otra con los impares.
    """
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares


def mostrar_resultados(pares, impares):
    """
    Muestra los resultados en pantalla de forma ordenada.
    """
    print("\n===== RESULTADOS =====")
    print("Números pares:  ", pares)
    print("Números impares:", impares)


# Programa principal
texto_usuario = input("Ingrese una lista de números enteros separados por espacios: ")
lista_numeros = validar_lista_numeros(texto_usuario)
pares, impares = separar_pares_impares(lista_numeros)
mostrar_resultados(pares, impares)

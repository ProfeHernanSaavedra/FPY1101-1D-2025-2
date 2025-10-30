# Evaluación formativa 4: Listas, diccionarios, funciones
# Solución en Python
# Requisitos implementados según enunciado:
# - Diccionario base de turistas
# - Funciones: turistas_por_pais(pais), turistas_por_mes(mes), eliminar_turista()
# - Menú principal con validaciones y mensajes especificados
import funcionesFormativo as fn


while True:
    print("\nMENU PRINCIPAL")
    print("1.- Turistas por pais.")
    print("2.- Turista por mes.")
    print("3.- Eliminar turista.")
    print("4.- Salir.")

    opcion = int(input("Ingrese opción: "))
    if opcion == 1:
        pais = input("\nIngrese pais a buscar: ")
        fn.turistas_por_pais(pais)
    elif opcion == 2:
        mes = fn.pedir_mes_valido()
        porcentaje = fn.turistas_por_mes(mes)
        print(f"El número de turistas equivale al {porcentaje} % del total.")
    elif opcion == 3:
        fn.eliminar_turista()
    elif opcion == 4:
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opción válida!!")




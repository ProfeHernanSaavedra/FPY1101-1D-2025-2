turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],  # corregido separador en fecha
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}


def turistas_por_pais(pais):
    """Muestra la lista de nombres de turistas de un país dado (case-insensitive)."""
    pais_normalizado = pais.strip().lower()
    lista_nombres = []

    for datos in turistas.values():
        pais_turista = datos[1].strip().lower()
        if pais_turista == pais_normalizado:
            lista_nombres.append(datos[0])

    if lista_nombres:
        print(lista_nombres)
    else:
        print("No hay turistas de ese pais.")

def turistas_por_mes(mes:int) -> float:
    """Retorna el % (1 decimal) de turistas cuya fecha (dd-mm-aaaa) cae en el mes dado."""
    total = len(turistas)
    #print(total)
    if total == 0:
        return 0.0
    contador_mes = 0
    for datos in turistas.values():
        fecha = datos[2]
        try:
            partes = fecha.split("-")  # dd-mm-aaaa
            if len(partes) >= 2 and int(partes[1]) == mes:
                contador_mes += 1
        except ValueError:
            continue
    return round((contador_mes / total) * 100, 1)

def eliminar_turista():
    """Pide un nombre y elimina el primer match (case-insensitive)."""
    nombre_objetivo = input("Ingrese nombre del turista a eliminar: ").strip().lower()
    id_a_eliminar = None
    for k, v in turistas.items():
        if v[0].strip().lower() == nombre_objetivo:
            id_a_eliminar = k
            break
    if id_a_eliminar is not None:
        del turistas[id_a_eliminar]
        print("Turista eliminado con exito.")
    else:
        print("Turista no encontrado. No se pudo eliminar.")

def pedir_mes_valido():
    """Solicita un mes 1..12 hasta que sea válido."""
    while True:
        try:
            mes = int(input("Ingrese mes a buscar: "))
            if 1 <= mes <= 12:
                return mes
            else:
                print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
        except ValueError:
            print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
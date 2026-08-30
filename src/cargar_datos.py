import csv


def leer_datos(ruta_archivo):
    """
    Lee un archivo CSV y lo convierte
    en una lista de diccionarios.
    """
    datos = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            datos.append(fila)

    return datos


def mostrar_resumen(datos):
    """
    Muestra un resumen de los datos.
    """
    print("\n--- RESUMEN DE DATOS DE TRANSPORTE ---")

    cantidad = len(datos)

    print(f"Cantidad total de registros: {cantidad}")

    if cantidad == 0:
        print("No hay datos para analizar.")
        return

    distancias = []

    for registro in datos:
        distancia = float(registro["distancia_km"])
        distancias.append(distancia)

    promedio = sum(distancias) / len(distancias)
    maximo = max(distancias)
    minimo = min(distancias)

    print(f"Distancia promedio: {promedio:.2f} km")
    print(f"Distancia máxima: {maximo:.2f} km")
    print(f"Distancia mínima: {minimo:.2f} km")


# Programa principal

if __name__ == "__main__":
    archivo = "data/transportes.csv"

    datos = leer_datos(archivo)

    mostrar_resumen(datos)
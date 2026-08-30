# Gestión de cultivos en Cartago
# Clase 2 - Inteligencia Artificial

cultivos = [
    {
        "nombre": "Café",
        "hectareas": 5,
        "produccion_toneladas": 3.2
    },
    {
        "nombre": "Caña",
        "hectareas": 10,
        "produccion_toneladas": 8.5
    },
    {
        "nombre": "Maíz",
        "hectareas": 3,
        "produccion_toneladas": 1.8
    },
    {
        "nombre": "Plátano",
        "hectareas": 4,
        "produccion_toneladas": 4.8
    },
    {
        "nombre": "Aguacate",
        "hectareas": 6,
        "produccion_toneladas": 5.4
    }
]


def calcular_rendimiento(cultivo):
    """
    Calcula la producción por hectárea de un cultivo.
    """
    return cultivo["produccion_toneladas"] / cultivo["hectareas"]


def mostrar_cultivos(lista_cultivos):
    """
    Muestra el nombre y rendimiento de cada cultivo.
    """
    print("\n--- RENDIMIENTO DE LOS CULTIVOS ---")

    for cultivo in lista_cultivos:
        rendimiento = calcular_rendimiento(cultivo)

        print(
            f"{cultivo['nombre']}: "
            f"{rendimiento:.2f} toneladas/hectárea"
        )


def cultivo_mayor_rendimiento(lista_cultivos):
    """
    Retorna el nombre del cultivo con mayor rendimiento.
    """
    mayor = lista_cultivos[0]

    for cultivo in lista_cultivos:
        if calcular_rendimiento(cultivo) > calcular_rendimiento(mayor):
            mayor = cultivo

    return mayor["nombre"]


# Programa principal
if __name__ == "__main__":

    mostrar_cultivos(cultivos)

    mayor_rendimiento = cultivo_mayor_rendimiento(cultivos)

    print(
        f"\nEl cultivo con mayor rendimiento es: "
        f"{mayor_rendimiento}"
    )

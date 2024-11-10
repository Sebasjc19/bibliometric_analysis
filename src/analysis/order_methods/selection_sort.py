# -----------------------------------------------------------------------------
# Metodo tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/selection-sort-algorithm-2/
# Python program for implementation of Selection Sort
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

def selection_sort(arr, key):
    n = len(arr)
    for i in range(n - 1):

        # Asume que la posición actual tiene el elemento mínimo
        min_idx = i

        # Itera a través de la porción no ordenada para encontrar el mínimo
        for j in range(i + 1, n):
            if key(arr[j]) < key(arr[min_idx]):
                # Actualiza min_idx si se encuentra un elemento más pequeño
                min_idx = j

        # Mueve el elemento mínimo a su posición correcta
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def obtener_tiempo_ordenamiento(publicaciones: list, key):
    tiempo_inicio = time.time()
    selection_sort(publicaciones.copy(), key)
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicio

if __name__ == "__main__":
    publicaciones = data_unification.obtener_publicaciones_unificadas()

    # -------------Ordenar por año
    key = lambda publicacion: publicacion.year
    print("Tiempo de ordenacion por año: " + str(obtener_tiempo_ordenamiento(publicaciones, key)))

    # --------------Ordenar por titulo
    key = lambda publicacion: publicacion.title
    print("Tiempo de ordenacion por titulo: " + str(obtener_tiempo_ordenamiento(publicaciones, key)))

    # --------------Ordenar por primer autor
    key = lambda publicacion: publicacion.first_author
    print("Tiempo de ordenacion por primer autor: " + str(obtener_tiempo_ordenamiento(publicaciones, key)))

    # -------------Ordenar por journal
    key = lambda publicacion: publicacion.journal
    print("Tiempo de ordenacion por journal: " + str(obtener_tiempo_ordenamiento(publicaciones, key)))

    # -------------Ordenar por publisher
    key = lambda publicacion: publicacion.publisher
    print("Tiempo de ordenacion por publisher: " + str(obtener_tiempo_ordenamiento(publicaciones, key)))

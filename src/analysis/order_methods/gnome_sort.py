# -----------------------------------------------------------------------------
# Metodo tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/gnome-sort-a-stupid-one/
#
# Python program to implement Gnome Sort
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

# Función para ordenar la lista dada usando el algoritmo Gnome Sort
def gnomeSort(arr, n, llave):
    index = 0 # Inicializa el índice en 0
    while index < n: # Continúa mientras el índice sea menor que la longitud de la lista
        if index == 0: # Si estamos en el primer elemento, avanzamos
            index = index + 1
        # Si el elemento actual es mayor o igual que el anterior, avanzamos
        if llave(arr[index]) >= llave(arr[index - 1]):
            index = index + 1
        else:
            # Intercambiamos los elementos si están en el orden incorrecto
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1 # Retrocedemos para verificar el nuevo elemento en la posición anterior

    return arr


def obtener_tiempo_ordenamiento(publicaciones: list, llave):
    tiempo_inicio = time.time()
    gnomeSort(publicaciones,len(publicaciones), llave)
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicio

if __name__ == '__main__':
    publicaciones = data_unification.obtener_publicaciones_unificadas()

    # -------------Ordenar por año
    llave = lambda publicacion: publicacion.year
    print("Tiempo de ordenacion por año: " + str(obtener_tiempo_ordenamiento(publicaciones, llave)))

    # --------------Ordenar por titulo
    llave = lambda publicacion: publicacion.title
    print("Tiempo de ordenacion por titulo: " + str(obtener_tiempo_ordenamiento(publicaciones, llave)))

    # --------------Ordenar por primer autor
    llave = lambda publicacion: publicacion.first_author
    print("Tiempo de ordenacion por primer autor: " + str(obtener_tiempo_ordenamiento(publicaciones, llave)))

    # -------------Ordenar por journal
    llave = lambda publicacion: publicacion.journal
    print("Tiempo de ordenacion por journal: " + str(obtener_tiempo_ordenamiento(publicaciones, llave)))

    # -------------Ordenar por publisher
    llave = lambda publicacion: publicacion.publisher
    print("Tiempo de ordenacion por publisher: " + str(obtener_tiempo_ordenamiento(publicaciones, llave)))

# -----------------------------------------------------------------------------
# Metodo tomados de studytonight.com: https://www.studytonight.com/python-programs/python-program-for-binary-insertion-sort
#
# Python program to implement binary insertion sort
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time


def binary_insertion_sort(array, llave):
    # Recorre cada elemento del array, comenzando desde el segundo elemento
    for i in range(1, len(array)):
        temp = array[i] # Almacena el elemento actual
        # Busca la posición en la que se debe insertar el elemento usando búsqueda binaria
        pos = binary_search(array, temp, 0, i, llave) + 1

        # Desplaza los elementos hacia la derecha para hacer espacio
        for k in range(i, pos, -1):
            array[k] = array[k - 1]

        array[pos] = temp # Inserta el elemento en la posición encontrada



def binary_search(array, key, strt, end, llave):
    # Caso base: si el rango es reducido a 1, determina la posición de inserción
    if end - strt <= 1:
        if llave(key) < llave(array[strt]):
            return strt - 1 # Inserta antes del índice strt
        else:
            return strt # Inserta en el índice strt

    # Encuentra el índice medio
    middle = (strt + end) // 2
    # Recursión hacia la mitad superior o inferior según la comparación
    if llave(array[middle]) < llave(key):
        return binary_search(array, key, middle, end, llave) # Busca en la mitad superior
    elif llave(array[middle]) > llave(key):
        return binary_search(array, key, strt, middle, llave) # Busca en la mitad inferior
    else:
        return middle # Si hay coincidencia, devuelve el índice medio


def obtener_tiempo_ordenamiento(publicaciones: list, llave):
    tiempo_inicio = time.time()
    binary_insertion_sort(publicaciones.copy(), llave)
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

# -----------------------------------------------------------------------------
# Metodo tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/heap-sort/

# heap Sort
# Python program for implementation of heap Sort

# To heapify a subtree rooted with node i
# which is an index in arr[].
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

def heapify(arr, n, i,llave):
    # Inicializa el índice más grande como raíz
    largest = i

    # Índice del hijo izquierdo = 2*i + 1
    l = 2 * i + 1

    # Índice del hijo derecho = 2*i + 2
    r = 2 * i + 2

    # Si el hijo izquierdo es mayor que la raíz
    if l < n and llave(arr[l]) > llave(arr[largest]):
        largest = l

    # Si el hijo derecho es mayor que el mayor hasta ahora
    if r < n and llave(arr[r]) > llave(arr[largest]):
        largest = r

    # Si el mayor no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Llama recursivamente a heapify en el subárbol afectado
        heapify(arr, n, largest, llave)


# Función principal para realizar el ordenamiento por montículos (heap sort)
def heapSort(arr,llave):
    n = len(arr)

    # Construye el heap (reorganiza el array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i,llave)

    # Extrae un elemento del heap uno por uno
    for i in range(n - 1, 0, -1):
        # Mueve la raíz al final
        arr[0], arr[i] = arr[i], arr[0]

        # Llama a heapify en el heap reducido
        heapify(arr, i, 0,llave)



def obtener_tiempo_ordenamiento(publicaciones: list, llave):
    tiempo_inicio = time.time()
    heapSort(publicaciones.copy(), llave)
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

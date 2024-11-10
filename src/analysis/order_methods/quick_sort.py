# -----------------------------------------------------------------------------
# Metodo tomados de medium.com: https://vmlogger.medium.com/quick-sort-understanding-and-implementing-in-python-419f4ed3c4f2

# Quick sort
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

def quick_sort(arr,llave):
    # Si el array tiene 1 o menos elementos, ya está ordenado
    if len(arr) <= 1:
        return arr


    pivot = arr[-1] # Selecciona el último elemento como pivote
    smaller, equal, larger = [], [], [] # Inicializa listas para los elementos menores, iguales y mayores que el pivote

    # Recorre todos los elementos en el array
    for num in arr:
        if llave(num) < llave(pivot):
            smaller.append(num) # Agrega a 'smaller' si es menor que el pivote
        elif llave(num) == llave(pivot):
            equal.append(num)  # Agrega a 'equal' si es igual al pivote
        else:
            larger.append(num)  # Agrega a 'larger' si es mayor que el pivote

    # Recursivamente ordena los subarrays y los concatena
    return quick_sort(smaller,llave) + equal + quick_sort(larger,llave)


def obtener_tiempo_ordenamiento(publicaciones: list, llave):
    tiempo_inicio = time.time()
    tamanio_lista = len(publicaciones)
    quick_sort(publicaciones.copy(), llave)
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

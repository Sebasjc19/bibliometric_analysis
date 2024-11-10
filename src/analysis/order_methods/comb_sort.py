# -----------------------------------------------------------------------------
# Metodo tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/comb-sort/
# Python program for implementation of CombSort
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

# Calcula el siguiente gap a partir del actual
def getNextGap(gap):
    # Reduce el gap por un factor de reducción
    gap = (gap * 10)//13
    if gap < 1: # Asegura que el gap sea al menos 1
        return 1
    return gap

# Función para ordenar arr[] usando Comb Sort
def combSort(arr,key):
    n = len(arr)

    gap = n # Inicializa el gap
    swapped = True # Para asegurar que el bucle se ejecute

    # Ejecuta el bucle mientras el gap sea mayor que 1 o haya intercambios
    while gap !=1 or swapped == 1:

        gap = getNextGap(gap) # Encuentra el siguiente gap

        swapped = False # Reinicia swapped para verificar intercambios
        # Compara elementos con el gap actual
        for i in range(0, n-gap):
            if key(arr[i]) > key(arr[i + gap]):
                arr[i], arr[i + gap]=arr[i + gap], arr[i] # Intercambia elementos
                swapped = True # Marca que ocurrió un intercambio

def obtener_tiempo_ordenamiento(publicaciones: list, key):
    tiempo_inicio = time.time()
    combSort(publicaciones.copy(), key)
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicio

if __name__ == '__main__':
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

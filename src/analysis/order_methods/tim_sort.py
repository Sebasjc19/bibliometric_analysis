# -----------------------------------------------------------------------------
# Metodos tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/timsort/
# Python3 program to perform basic timSort
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

MIN_MERGE = 32 # Tamaño mínimo de una corrida para la ordenación
def calcMinRun(n):
    """Devuelve la longitud mínima de una corrida entre 32 y 64."""
    r = 0
    # Mantiene el registro de los bits menos significativos
    while n >= MIN_MERGE:
        r |= n & 1 # Comprueba si el número es impar
        n >>= 1 # Desplaza n a la derecha para analizar el siguiente bit
    return n + r # Devuelve el tamaño de la corrida ajustado

# Función de ordenación por inserción modificada para usar una función clave
def insertionSort(arr, left, right, key):
    """Ordena un subarreglo usando el algoritmo de ordenación por inserción."""
    for i in range(left + 1, right + 1): # Comienza desde el segundo elemento
        j = i
        # Realiza la comparación usando la función clave
        while j > left and key(arr[j]) < key(arr[j - 1]):
            # Intercambia elementos si están en el orden incorrecto
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1 # Mueve hacia atrás para continuar la comparación

# Función de mezcla modificada para usar una función clave
def merge(arr, l, m, r, key):
    """Combina dos subarreglos en uno ordenado."""
    len1, len2 = m - l + 1, r - m # Longitudes de los subarreglos
    left, right = [], [] # Inicializa los subarreglos
    # Copia los elementos del subarreglo izquierdo
    for i in range(0, len1):
        left.append(arr[l + i])
    # Copia los elementos del subarreglo derecho
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l # Inicializa índices para los subarreglos y el arreglo principal
    # Mezcla los subarreglos en orden
    while i < len1 and j < len2:
        if key(left[i]) <= key(right[j]):
            arr[k] = left[i] # Coloca el elemento menor en el arreglo principal
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1 # Avanza el índice del arreglo principal
    # Copia los elementos restantes del subarreglo izquierdo
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    # Copia los elementos restantes del subarreglo derecho
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

# Implementación de Timsort con función clave
def timSort(arr, key):
    """Ordena un arreglo usando el algoritmo Timsort."""
    n = len(arr) # Obtiene la longitud del arreglo
    minRun = calcMinRun(n) # Calcula la longitud mínima de una corrida

    # Ordena subarreglos individuales del tamaño RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1) # Encuentra el final del subarreglo
        insertionSort(arr, start, end, key) # Ordena el subarreglo usando inserción

    size = minRun # Inicializa el tamaño de mezcla
    # Mezcla los subarreglos ordenados
    while size < n:
        for left in range(0, n, 2 * size): # Itera a través de los subarreglos
            mid = min(n - 1, left + size - 1) # Encuentra el punto medio
            right = min((left + 2 * size - 1), (n - 1))# Encuentra el final derecho
            if mid < right: # Asegura que haya elementos para mezclar
                merge(arr, left, mid, right, key) # Mezcla los subarreglos
        size = 2 * size # Duplica el tamaño para la siguiente iteración


def obtener_tiempo_ordenamiento(publicaciones: list, key):
    tiempo_inicio = time.time()
    timSort(publicaciones.copy(), key)
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicio

if __name__ == "__main__":
    publicaciones = data_unification.obtener_publicaciones_unificadas()

    #-------------Ordenar por año
    key = lambda publicacion: publicacion.year
    print("Tiempo de ordenacion por año: "+str(obtener_tiempo_ordenamiento(publicaciones,key)))

    # --------------Ordenar por titulo
    key = lambda publicacion: publicacion.title
    print("Tiempo de ordenacion por titulo: "+str(obtener_tiempo_ordenamiento(publicaciones,key)))

    # --------------Ordenar por primer autor
    key = lambda publicacion: publicacion.first_author
    print("Tiempo de ordenacion por primer autor: " + str(obtener_tiempo_ordenamiento(publicaciones, key)))

    # -------------Ordenar por journal
    key = lambda publicacion: publicacion.journal
    print("Tiempo de ordenacion por journal: " + str(obtener_tiempo_ordenamiento(publicaciones, key)))

    #-------------Ordenar por publisher
    key = lambda publicacion: publicacion.publisher
    print("Tiempo de ordenacion por publisher: "+str(obtener_tiempo_ordenamiento(publicaciones,key)))



"""
    #--------------Ordenar por titulo

    print("Titulo"+'-' * 40 + "Inicio")

    tiempo_inicio = time.time()
    timSort(publicaciones.copy(), key=lambda publicacion: publicacion.title)
    tiempo_final = time.time()
    print(tiempo_final - tiempo_inicio)

    print('-' * 40 + "Fin")

    #--------------Ordenar por primer autor

    print("Primer autor"+'-' * 40 + "Inicio")

    tiempo_inicio = time.time()
    timSort(publicaciones.copy(), key=lambda publicacion: publicacion.first_author)
    tiempo_final = time.time()
    print(tiempo_final - tiempo_inicio)

    print('-' * 40 + "Fin")

    #-------------Ordenar por journal

    print("Journal"+'-' * 40 + "Inicio")

    tiempo_inicio = time.time()
    timSort(publicaciones.copy(), key=lambda publicacion: publicacion.journal)
    tiempo_final = time.time()
    print(tiempo_final - tiempo_inicio)

    print('-' * 40 + "Fin")

    #-------------Ordenar por publisher

    print("Publisher"+'-' * 40 + "Inicio")

    tiempo_inicio = time.time()
    timSort(publicaciones.copy(), key=lambda publicacion: publicacion.publisher)
    tiempo_final = time.time()
    print(tiempo_final - tiempo_inicio)

    print('-' * 40 + "Fin") """
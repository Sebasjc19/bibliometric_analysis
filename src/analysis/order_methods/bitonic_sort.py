# -----------------------------------------------------------------------------
# Metodo tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/bitonic-sort/

# bitonic Sort
# Python program for implementation of heap Sort

# Python program for Bitonic Sort. Note that this program
# works only when size of input is a power of 2.
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

# La función compAndSwap intercambia a[i] y a[j] si están en el
# orden incorrecto, dependiendo de la dirección de ordenamiento (ascendente o descendente).
def compAndSwap(a, i, j, dire,llave):
    if (dire == 1 and llave(a[i]) > llave(a[j])) or (dire == 0 and llave(a[i]) < llave(a[j])):
        a[i], a[j] = a[j], a[i]


# La función bitonicMerge ordena recursivamente una secuencia bitónica.
# Si dir = 1, la ordena en orden ascendente; de lo contrario (dir = 0), la ordena en orden descendente.
# La secuencia a ordenar comienza en la posición de índice low y
# el parámetro cnt es el número de elementos a ordenar.
def bitonicMerge(a, low, cnt, dire, llave):
    if cnt > 1: # Solo continua si hay más de un elemento
        k = cnt // 2 # Divide la secuencia en dos mitades
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire,llave) # Compara y intercambia elementos
        bitonicMerge(a, low, k, dire,llave) # Ordena la primera mitad
        bitonicMerge(a, low + k, k, dire,llave) # Ordena la segunda mitad


# La función bitonicSort genera una secuencia bitónica ordenando
# recursivamente sus dos mitades en órdenes de ordenamiento opuestos,
# y luego llama a bitonicMerge para combinarlas en el mismo orden.
def bitonicSort(a, low, cnt, dire,llave):
    if cnt > 1: # Solo continua si hay más de un elemento
        k = cnt // 2 # Divide la cantidad en dos
        bitonicSort(a, low, k, 1,llave) # Ordena la primera mitad en orden ascendente
        bitonicSort(a, low + k, k, 0, llave) # Ordena la segunda mitad en orden descendente
        bitonicMerge(a, low, cnt, dire, llave) # Combina ambas mitades en el mismo orden


def obtener_tiempo_ordenamiento(publicaciones: list, llave):
    tiempo_inicio = time.time()
    bitonicSort(publicaciones.copy(),0,len(publicaciones),1, llave)
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

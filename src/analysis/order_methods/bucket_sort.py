# -----------------------------------------------------------------------------
# Metodo tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/bucket-sort-2/

# Bucket Sort
# Este algoritmo fue modificado ajustandolo al contexto de las publicaciones cientificas
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j].year > key.year:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(publications):
    # Encuentra el año mínimo y máximo
    min_year = min(pub.year for pub in publications)
    max_year = max(pub.year for pub in publications)

    # Calcula el rango y número de cubos
    range_of_years = max_year - min_year + 1
    buckets = [[] for _ in range(range_of_years)]

    # Distribuye las publicaciones en cubos basados en el año
    for pub in publications:
        bi = pub.year - min_year  # Asigna al cubo correspondiente
        buckets[bi].append(pub)

    # Ordena cada cubo utilizando Insertion Sort
    for bucket in buckets:
        insertion_sort(bucket)

    # Combina todos los cubos en la lista de publicaciones
    sorted_publications = []
    for bucket in buckets:
        sorted_publications.extend(bucket)  # Usa extend para añadir los elementos

    return sorted_publications


def obtener_tiempo_ordenamiento(publicaciones: list):
    tiempo_inicio = time.time()
    bucket_sort(publicaciones.copy())
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicio

if __name__ == '__main__':
    publicaciones = data_unification.obtener_publicaciones_unificadas()

    # -------------Ordenar por año
    print("Tiempo de ordenacion por año: " + str(obtener_tiempo_ordenamiento(publicaciones)))


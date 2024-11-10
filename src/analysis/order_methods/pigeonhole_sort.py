# -----------------------------------------------------------------------------
# Metodo tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/pigeonhole-sort/

# Python program to implement Pigeonhole Sort
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

def pigeonhole_sort(publications):
    # Encuentra el año mínimo y máximo
    my_min = min(pub.year for pub in publications)
    my_max = max(pub.year for pub in publications)
    size = my_max - my_min + 1  # Calcula el rango de años

    # Creamos los pigeonholes
    holes = [[] for _ in range(size)]

    # Llena los pigeonholes con las publicaciones
    for pub in publications:
        holes[pub.year - my_min].append(pub) # Asigna la publicación al agujero correspondiente

    # Reordena las publicaciones en función de su año
    i = 0
    for hole in holes:
        for pub in hole:
            publications[i] = pub # Asigna las publicaciones ordenadas de vuelta a la lista
            i += 1



def obtener_tiempo_ordenamiento(publicaciones: list):
    tiempo_inicio = time.time()
    pigeonhole_sort(publicaciones.copy())
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicio

if __name__ == '__main__':
    publicaciones = data_unification.obtener_publicaciones_unificadas()
    print("Tiempo de ordenacion por año: " + str(obtener_tiempo_ordenamiento(publicaciones)))


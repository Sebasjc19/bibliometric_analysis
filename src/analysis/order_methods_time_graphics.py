import os

from src.analysis.order_methods.binary_insertion_sort import obtener_tiempo_ordenamiento as biinsoobtior
from src.analysis.order_methods.bitonic_sort import obtener_tiempo_ordenamiento as bisoimobtior
from src.analysis.order_methods.bucket_sort import obtener_tiempo_ordenamiento as busorobtior
from src.analysis.order_methods.comb_sort import obtener_tiempo_ordenamiento as cosoobtior
from src.analysis.order_methods.gnome_sort import obtener_tiempo_ordenamiento as gnsoobtior
from src.analysis.order_methods.heap_sort import obtener_tiempo_ordenamiento as hesoobtior
from src.analysis.order_methods.pigeonhole_sort import obtener_tiempo_ordenamiento as pisoobtior
from src.analysis.order_methods.quick_sort import obtener_tiempo_ordenamiento as qusoobtior
from src.analysis.order_methods.radix_sort import obtener_tiempo_ordenamiento as rasoobtior
from src.analysis.order_methods.selection_sort import obtener_tiempo_ordenamiento as sesoobtior
from src.analysis.order_methods.tim_sort import obtener_tiempo_ordenamiento as tisoobtior
from src.analysis.order_methods.tree_sort import obtener_tiempo_ordenamiento as trsoobtior
from src.utils import graphics_util, sqlite_util

ruta_imagenes = os.path.join(os.path.dirname(__file__), '../../static/images')

publicaciones = sqlite_util.obtener_publicaciones_objeto()

# Función para obtener los tiempos de los algoritmos de ordenamiento
def obtener_tiempos_de_ejecucion(publicaciones, llave):
    if llave == (lambda publicacion: publicacion.year):
        return {
            'Binary Insertion Sort': biinsoobtior(publicaciones.copy(), llave),
            'Bitonic Sort': bisoimobtior(publicaciones.copy(), llave),
            'Bucket Sort': busorobtior(publicaciones.copy()),  # No usa llave
            'Comb Sort': cosoobtior(publicaciones.copy(), llave),
            'Gnome Sort': gnsoobtior(publicaciones.copy(), llave),
            'Heap Sort': hesoobtior(publicaciones.copy(), llave),
            'Pigeonhole Sort': pisoobtior(publicaciones.copy()),  # No usa llave
            'Quick Sort': qusoobtior(publicaciones.copy(), llave),
            'Radix Sort': rasoobtior(publicaciones.copy()),  # No usa llave
            'Selection Sort': sesoobtior(publicaciones.copy(), llave),
            'Tim Sort': tisoobtior(publicaciones.copy(), llave),
            'Tree Sort': trsoobtior(publicaciones.copy(), llave),
        }
    else:
        return {
            'Binary Insertion Sort': biinsoobtior(publicaciones.copy(), llave),
            'Bitonic Sort': bisoimobtior(publicaciones.copy(), llave),
            'Comb Sort': cosoobtior(publicaciones.copy(), llave),
            'Gnome Sort': gnsoobtior(publicaciones.copy(), llave),
            'Heap Sort': hesoobtior(publicaciones.copy(), llave),
            'Quick Sort': qusoobtior(publicaciones.copy(), llave),
            'Selection Sort': sesoobtior(publicaciones.copy(), llave),
            'Tim Sort': tisoobtior(publicaciones.copy(), llave),
            'Tree Sort': trsoobtior(publicaciones.copy(), llave),
        }



# Función genérica para obtener tiempos y graficar según una llave de ordenamiento
def graficar_tiempo_ordenamiento_por_llave(llave, titulo, ruta_guardado):
    tiempos_ejecucion = obtener_tiempos_de_ejecucion(publicaciones, llave)

    # Imprimir resultados en consola
    for algoritmo, tiempo in tiempos_ejecucion.items():
        print(f"{algoritmo}: {tiempo} segundos")

    # Graficar los tiempos
    graphics_util.realizar_graficos(tiempos_ejecucion, titulo,"Algoritmos de ordenamiento","Tiempo de ejecución (segundos)", "barra", ruta_guardado)

def graficar_tiempo_ejecucion_anio():
    llave = lambda publicacion: publicacion.year
    graficar_tiempo_ordenamiento_por_llave(llave, 'Algoritmos de ordenamiento según año de publicación', ruta_imagenes+"/tiempo_ejecucion_ordenamiento_anio.png")

def graficar_tiempo_ejecucion_titulo():
    # Metodos para hallar el tiempo de ejecución de ordenamiento por año
    llave = lambda publicacion: publicacion.title
    graficar_tiempo_ordenamiento_por_llave(llave, 'Algoritmos de ordenamiento según titulo de publicación', ruta_imagenes+"/tiempo_ejecucion_ordenamiento_titulo.png")

def graficar_tiempo_ejecucion_primer_autor():
    # Metodos para hallar el tiempo de ejecución de ordenamiento por año
    llave = lambda publicacion: publicacion.first_author
    graficar_tiempo_ordenamiento_por_llave(llave, 'Algoritmos de ordenamiento según primer autor de publicación', ruta_imagenes+"/tiempo_ejecucion_primer_autor.png")

def graficar_tiempo_ejecucion_journal():
    # Metodos para hallar el tiempo de ejecución de ordenamiento por año
    llave = lambda publicacion: publicacion.journal
    graficar_tiempo_ordenamiento_por_llave(llave, 'Algoritmos de ordenamiento según revista científica de publicación', ruta_imagenes+"/tiempo_ejecucion_journal.png")

def graficar_tiempo_ejecucion_publisher():
    # Metodos para hallar el tiempo de ejecución de ordenamiento por año
    llave = lambda publicacion: publicacion.publisher
    graficar_tiempo_ordenamiento_por_llave(llave, 'Algoritmos de ordenamiento según publisher de publicación', ruta_imagenes+"/tiempo_ejecucion_publisher.png")


if __name__ == '__main__':
    graficar_tiempo_ejecucion_titulo()
    graficar_tiempo_ejecucion_publisher()




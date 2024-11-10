# -----------------------------------------------------------------------------
# Metodo tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/radix-sort/

# Python program for implementation of Radix Sort
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

# Una función para realizar un conteo de arr[] según el dígito representado por exp.
def countingSort(arr, exp1):

    n = len(arr) # Longitud del array

    # El array de salida que contendrá el array ordenado
    output = [0] * (n)

    # Inicializa el array count con ceros
    count = [0] * (10)

    # Almacena la cuenta de ocurrencias en count[]
    for i in range(0, n):
        index = arr[i].year // exp1 # Obtiene el dígito correspondiente al exponente actual
        count[index % 10] += 1  # Incrementa la cuenta de ese dígito

    # Cambia count[i] para que ahora contenga la posición real de este dígito en el array de salida
    for i in range(1, 10):
        count[i] += count[i - 1]  # Suma acumulativa

    # Construye el array de salida
    i = n - 1 # Comienza desde el final del array original
    while i >= 0:
        index = arr[i].year // exp1 # Obtiene el dígito correspondiente
        output[count[index % 10] - 1] = arr[i] # Coloca el elemento en su posición correcta
        count[index % 10] -= 1 # Decrementa la cuenta
        i -= 1

    # Copia el array de salida a arr[], de modo que arr ahora contenga números ordenados
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Método para realizar el ordenamiento Radix
def radixSort(arr):

    # Encuentra el número máximo para saber cuántos dígitos tiene
    max1 =  max(pub.year for pub in arr)

    # Realiza el ordenamiento por conteo para cada dígito
    exp = 1 # Inicializa el exponente
    while max1 / exp >= 1:
        countingSort(arr, exp) # Ordena usando el dígito actual
        exp *= 10 # Aumenta el exponente (10^i) para el siguiente dígito



def obtener_tiempo_ordenamiento(publicaciones: list):
    tiempo_inicio = time.time()
    radixSort(publicaciones.copy())
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicio

if __name__ == '__main__':
    publicaciones = data_unification.obtener_publicaciones_unificadas()

    # -------------Ordenar por año
    llave = lambda publicacion: publicacion.year
    print("Tiempo de ordenacion por año: " + str(obtener_tiempo_ordenamiento(publicaciones)))

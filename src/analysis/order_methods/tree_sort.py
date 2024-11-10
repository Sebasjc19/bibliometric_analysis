# -----------------------------------------------------------------------------
# Metodo tomados de GeeksForGeeks.org: https://www.geeksforgeeks.org/tree-sort/

# Python3 program to
# implement Tree Sort

# Class containing left and
# right child of current
# node and key value
# -----------------------------------------------------------------------------
from src.analysis import data_unification
import time

class Node:

    def __init__(self, item=0):
        self.key = item # Asigna el valor del nodo
        self.left, self.right = None, None # Inicializa los hijos izquierdo y derecho


# Root of BST
root = Node()

# Inicialización de la raíz del BST
root = None


# Función principal que llama a insertRec()
def insert(key, llave):
    global root
    root = insertRec(root, key, llave) # Inserta el nuevo nodo en el árbol


# Función recursiva para insertar una nueva clave en el BST
def insertRec(root, key, llave):
    # Si el árbol está vacío, retorna un nuevo nodo

    if (root == None):
        root = Node(key)
        return root

    # De lo contrario, recorre el árbol
    if (llave(key) < llave(root.key)):
        root.left = insertRec(root.left, key, llave) # Inserta en el subárbol izquierdo
    elif (llave(key) > llave(root.key)):
        root.right = insertRec(root.right, key, llave) # Inserta en el subárbol derecho

    # Retorna la raíz del árbol (o subárbol)
    return root


# Función para hacer un recorrido en orden del BST
def inorderRec(root):
    if (root != None):
        inorderRec(root.left) # Recorre el subárbol izquierdo
        print(root.key, end=" ") # Imprime la clave del nodo actual
        inorderRec(root.right) # Recorre el subárbol derecho

# Función para insertar múltiples elementos en el BST
def treeins(arr, llave):
    for i in range(len(arr)):
        insert(arr[i], llave) # Inserta cada elemento del arreglo en el BST


def obtener_tiempo_ordenamiento(publicaciones: list, llave):
    tiempo_inicio = time.time()
    treeins(publicaciones.copy(), llave)
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

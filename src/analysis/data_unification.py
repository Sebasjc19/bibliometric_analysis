import bibtexparser
import pandas as pd
import os

from src.model.publication import publication

publicaciones_unificadas = []
publicaciones_repetidas_o_sin_identificador = []
contador = 0
identificadores = set()  # Set para evitar duplicados basados en DOI, ISBN o ISSN


# Función para leer el archivo BibTeX
def leer_bibtex(file_path):
    with open(file_path, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    df_bibtex = pd.DataFrame(bib_database.entries)
    return df_bibtex

# Función para recorrer recursivamente una carpeta y procesar archivos .bib
def leer_archivos(carpeta_base):
    for carpeta_raiz, subdirectorios, archivos in os.walk(carpeta_base):
        for archivo in archivos:
            ruta_completa = os.path.join(carpeta_raiz, archivo)
            if archivo.endswith(".bib"):
                procesar_archivos_bibtex(ruta_completa, carpeta_raiz)
    return publicaciones_unificadas

def procesar_archivos_bibtex(ruta_completa, carpeta_raiz):
    global contador
    bibtex_df = leer_bibtex(ruta_completa)
    # Mostrar las columnas del DataFrame
    # print(bibtex_df.columns)

    database = carpeta_raiz.split("/")[-1] #base de datos

    # Mostrar las entradas procesadas
    for index, row in bibtex_df.iterrows():
        #Variables de verificacion de duplicado
        doi = str(row.get('doi'))
        isbn = str(row.get('isbn'))
        issn = str(row.get('issn'))
        titulo = str(row.get('title'))

        #Limpiado de datos
        autor = str(row.get('author')).split(',')[0] # primer autor del producto
        anio = str(row.get('year')) # año de publicación
        abstract = str(row.get('abstract')) # abstract
        journal = str(row.get('journal')) # journal
        publisher = str(row.get('publisher')) # publisher
        tipo = str(row.get('ENTRYTYPE')) # tipo de producto (artículos, conferencias, capítulos de libro)
        # afiliación del primer autor
        # cantidad de citaciones por artículo presentadas de manera ordenada.

        # Identificador único (puede ser DOI, ISBN, ISSN o titulo)
        identificador = doi or isbn or issn or titulo
        # Verificar si ya existe en el set de identificadores
        pub = publication(
            doi, isbn, issn, titulo, autor, anio, abstract, journal, publisher, tipo, database
        )
        if identificador not in identificadores:
            # Agregar al set de identificadores
            identificadores.add(identificador)

            # Crear un objeto de tipo Publication y añadirlo a unified_data
            #pub = publication(
            #    doi, isbn, issn, titulo, autor, anio, abstract, journal, publisher, tipo, database
            #)
            publicaciones_unificadas.append(pub)
        else:
            publicaciones_repetidas_o_sin_identificador.append(pub)
            contador = contador + 1

def imprimir_publicaciones_por_base_de_datos(base_datos):
    publicaciones_filtradas = [pub for pub in publicaciones_unificadas if pub.database == base_datos]
    if publicaciones_filtradas:
        for pub in publicaciones_filtradas:
            print(f"Título: {pub.title}")
            print(f"Autor Principal: {pub.first_author}")
            print(f"Año: {pub.year}")
            print(f"Journal: {pub.journal}")
            print(f"Publisher: {pub.publisher}")
            print(f"Tipo: {pub.type}")
            print(f"DOI: {pub.doi}")
            print(f"ISBN: {pub.isbn}")
            print(f"ISSN: {pub.issn}")
            print(f"Base de Datos: {pub.database}")
            print("-" * 40)
    else:
        print(f"No se encontraron publicaciones para la base de datos '{base_datos}'.")

def unificar_publicaciones():
    ruta_data = '../../data/'
    return leer_archivos(ruta_data)
if __name__ == '__main__':
    #ruta_data = '../../data/'
    #leer_archivos(ruta_data)
    publicaciones = unificar_publicaciones()
    print("cantidad publicaciones filtradas: ", len(publicaciones))
    print("Cantidad publicaciones sin un posible identificador o repetidas", contador)
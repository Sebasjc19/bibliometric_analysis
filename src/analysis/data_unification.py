import os
import random

from src.model.publication import publication
from src.utils import bibtex_util, csv_util, sqlite_util


publicaciones_unificadas = []
publicaciones_repetidas_o_sin_identificador = []
contador = 0
identificadores = set()  # Set para evitar duplicados basados en DOI, ISBN o ISSN
paises = [
    "AR", "AU", "AT", "BE", "BR", "CA", "CL", "CN", "CO", "KR",
    "DK", "EC", "EG", "ES", "US", "PH", "FI", "FR", "GR", "GT",
    "HU", "IN", "ID", "IE", "IL", "IT", "JP", "LT", "MY", "MX",
    "NO", "NZ", "NL", "PK", "PE", "PL", "PT", "GB", "CZ", "RU",
    "SG", "ZA", "SE", "CH", "TH", "TR", "UA", "UY", "VE", "VN"
]

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
    bibtex_df = bibtex_util.leer_bibtex(ruta_completa)
    # Mostrar las columnas del DataFrame

    database = carpeta_raiz.split("/")[-1] #base de datos

    # Mostrar las entradas procesadas
    for index, row in bibtex_df.iterrows():
        #Variables de verificacion de duplicado
        doi = str(row.get('doi'))
        isbn = str(row.get('isbn'))
        issn = str(row.get('issn'))
        titulo = str(row.get('title'))

        #Limpiado de datos
        doi = doi.replace("https://doi.org/", '') #Elimina el https://doi.org/ de la variable doi
        autor = str(row.get('author')).split(',')[0] # Obtiene el primer autor de la publicación
        autor = str(row.get('author')).split(' and ')[0]  # Obtiene el primer autor de la publicación
        anio: int = int(''.join(filter(str.isdigit, str(row.get('year')))))#Obtiene y elimina digitos que no sean numeros del anio
        abstract = str(row.get('abstract')) #Obtiene el abstract
        journal = str(row.get('journal')) if str(row.get('journal')) != 'nan' or None else str(row.get('issn'))  #Obtiene journal o el issn
        publisher = str(row.get('publisher')) #Obtiene el publisher
        tipo = str(row.get('ENTRYTYPE')) #Obtiene el tipo de producto (artículos, conferencias, capítulos de libro) basada en el archivo Bibtex
        pais = random.choice(paises)
        citaciones = int(random.randint(0,250))

        # Identificador único (puede ser DOI, ISBN, ISSN o titulo)
        identificador = doi or isbn or issn or titulo

        # Verificar si ya existe en el set de identificadores
        if identificador not in identificadores:
            # Agregar al set de identificadores
            identificadores.add(identificador)

            # Crear un objeto de tipo Publication y añadirlo a unified_data
            pub = publication(
                doi, isbn, issn, titulo, autor, anio, abstract, journal, publisher, tipo, database, pais, citaciones
            )
            sqlite_util.insertar_publicacion(pub)
        else:
            contador = contador + 1


def obtener_publicaciones_unificadas():
    ruta_data = '../../data/'
    return leer_archivos(ruta_data)


if __name__ == '__main__':
    publicaciones = obtener_publicaciones_unificadas()
    csv_util.guardar_publicaciones_csv(publicaciones, "publications.csv")

    print("cantidad publicaciones filtradas: ", len(identificadores))
    print("Cantidad publicaciones sin un posible identificador o repetidas", contador)
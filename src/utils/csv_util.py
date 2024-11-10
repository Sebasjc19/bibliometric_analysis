# Función para guardar lista de objetos publication en un archivo CSV
import csv

def guardar_publicaciones_csv(publications, filename):
    # Nombres de las columnas para el archivo CSV
    fieldnames = ['doi', 'isbn', 'issn', 'title', 'first_author', 'year', 'abstract', 'journal', 'publisher', 'type', 'database', 'country', 'citations']

    # Abrir el archivo en modo de escritura
    with open("../../results/"+filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Escribir la cabecera
        writer.writeheader()

        # Escribir cada objeto como fila
        for publication in publications:
            writer.writerow({
                'doi': publication.doi,
                'isbn': publication.isbn,
                'issn': publication.issn,
                'title': publication.title,
                'first_author': publication.first_author,
                'year': publication.year,
                'abstract': publication.abstract,
                'journal': publication.journal,
                'publisher': publication.publisher,
                'type': publication.type,
                'database': publication.database
            })
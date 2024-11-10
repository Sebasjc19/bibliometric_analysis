


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
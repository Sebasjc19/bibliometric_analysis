import sqlite3


from src.model import publication
from src.model.publication import publication
import os

ruta_db = os.path.join(os.path.dirname(__file__), '../database/publicaciones.db')

def inicializar_bd():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()

    # Crear la tabla de publicaciones
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS publications (
        id INTEGER PRIMARY KEY,
        doi TEXT,
        isbn TEXT,
        issn TEXT,
        title TEXT,
        first_author TEXT,
        year INTEGER,
        abstract TEXT,
        journal TEXT,
        publisher TEXT,
        type TEXT,
        database TEXT,
        country TEXT,
        citations INTEGER
    )
    ''')
    conn.commit()

def insertar_publicacion(publication: publication):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
            INSERT INTO publications (doi, isbn, issn, title, first_author, year, abstract, journal, publisher, type, database, country, citations)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)
        ''', (publication.doi, publication.isbn, publication.issn, publication.title, publication.first_author,
              publication.year, publication.abstract, publication.journal, publication.publisher,
              publication.type, publication.database, publication.country, publication.citations))
    conn.commit()

def obtener_abstracts():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT abstract FROM publications
    where abstract is not 'nan' or null''')
    return cursor.fetchall()


def obtener_publicaciones_anio():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT year, COUNT(*) as total_products
    FROM publications
    GROUP BY year
    ORDER BY year DESC
    ''')
    return cursor.fetchall()

def obtener_tipo_publicaciones_frecuentes():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT type, COUNT(*) as total_products
    FROM publications
    GROUP BY type
    ORDER BY total_products DESC
    ''')
    return cursor.fetchall()

def obtener_jorunals_frecuentes():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT case
        when journal is 'nan' then 'desconocido'
            else journal end,
    COUNT(*) as total_products
    FROM publications
    GROUP BY journal
    ORDER BY total_products DESC
    ''')
    return cursor.fetchall()

def obtener_publishers_frecuentes():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT case
    when publisher = 'nan' then 'desconocido'
        else publisher end as publisher, COUNT(*) as total_products
    FROM publications
    GROUP BY publisher
    ORDER BY total_products DESC
    ''')
    return cursor.fetchall()

def obtener_bds_frecuentes():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT database, COUNT(*) as total_products
    FROM publications
    GROUP BY database
    ORDER BY total_products DESC
    ''')
    return cursor.fetchall()

def obtener_autores_frecuentes():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT case 
        when first_author is 'nan' then 'desconocido' 
        else first_author end as primer_autor,
    COUNT(*) as total_products
    FROM publications
    GROUP BY first_author
    ORDER BY total_products DESC
    ''')
    return cursor.fetchall()


def obtener_publicaciones_objeto():
    with sqlite3.connect(ruta_db) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM publications')

        lista = []
        for row in cursor.fetchall():
            # Omite el primer campo (id) ya que no está en el constructor de Publication
            publicacion = publication(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                      row[11], row[12], row[13])
            lista.append(publicacion)

    return lista

def obtener_cantidad_publicaciones():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT count(*) FROM publications''')
    return cursor.fetchall()[0][0]

def obtener_journals_top_10():
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT journal, COUNT(*) as total_articles
    FROM publications
    WHERE journal is not 'nan' and journal is not ''
    GROUP BY journal
    ORDER BY total_articles DESC
    LIMIT 10
    ''')
    return cursor.fetchall()

def obtener_articulos_top_15(journal):
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT doi, title, citations, first_author, country
    FROM publications
    WHERE journal = ? and journal is not 'nan' and journal is not ''
    ORDER BY citations DESC
    LIMIT 15
    ''', (journal,))
    return cursor.fetchall()







# Función para leer el archivo BibTeX
import bibtexparser
import pandas as pd


def leer_bibtex(file_path):
    with open(file_path, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    df_bibtex = pd.DataFrame(bib_database.entries)
    return df_bibtex
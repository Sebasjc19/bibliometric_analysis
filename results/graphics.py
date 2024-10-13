import bibtexparser
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from src.analysis.data_unification import leer_bibtex, procesar_archivos_bibtex


# -------------------------------CARGAR Y PARSEAR BIBTEX ---------------------------------------
# Leer el archivo .bibtex
with open('../data/sciencedirect/ScienceDirect_citations_1728436385153.bib') as bibtex_file:
    bib_database = procesar_archivos_bibtex('../data/')

# Ver los datos extraídos
entries = bib_database.entries


# ------------------- CONTAR ENTRADAS ----------------------------
# Obtener los años de las publicaciones
years = [entry['year'] for entry in entries if 'year' in entry]

# Contar las publicaciones por año
publications_per_year = Counter(years)

#----------- GRAFICAR ---------------------
# Datos para el gráfico
years = list(publications_per_year.keys())
counts = list(publications_per_year.values())

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x=years, y=counts, palette='viridis')
plt.title('Publicaciones por Año')
plt.xlabel('Año')
plt.ylabel('Número de Publicaciones')
plt.xticks(rotation=45)
plt.show()
import matplotlib.pyplot as plt
import networkx as nx
from wordcloud import WordCloud

from src.utils import sqlite_util


def realizar_graficos(datos, titulo, xlabel, ylabel, tipo_grafico, ruta_guardado):
    # Verificar el tipo de datos y extraer datos x y y
    if isinstance(datos, dict):
        categorias = list(datos.keys())
        frecuencias = list(datos.values())
    else:  # Se asume que es una lista de tuplas
        categorias = [dato[0] for dato in datos]
        frecuencias = [dato[1] for dato in datos]

    # Limitar a los primeros 15 datos (o todos si hay menos de 15)
    categorias_limited = categorias[:15][::-1]
    frecuencias_limited = frecuencias[:15][::-1]

    plt.figure(figsize=(10, 6))

    if tipo_grafico == 'barra':
        plt.bar(categorias_limited, frecuencias_limited, color='skyblue')
    elif tipo_grafico == 'linea':
        plt.plot(categorias_limited, frecuencias_limited, marker='o', color='b', linestyle='-', linewidth=2)
    else:
        raise ValueError("Tipo de gráfico no reconocido. Usa 'barra' o 'linea'.")

    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()  # Ajuste automático del gráfico para evitar solapamiento
    plt.savefig(ruta_guardado)
    #plt.show()


def generar_nube_palabras(frecuencias, ruta_guardado):

    nube_palabras = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(frecuencias)

    plt.figure(figsize=(10, 5))
    plt.imshow(nube_palabras, interpolation='bilinear')
    plt.axis('off')  # Ocultar los ejes
    plt.title('Nube de Palabras de Palabras Clave')
    plt.savefig(ruta_guardado)

def generar_grafo(journals):
    G = nx.Graph()

    for journal, _ in journals:
        # Agregar un nodo para cada journal
        G.add_node(journal)

        # Obtener los 15 artículos más citados para cada journal
        articulos = sqlite_util.obtener_articulos_top_15(journal)

        for doi, title, citations, first_author, country in articulos:
            # Crear un nodo para cada artículo
            G.add_node(doi, title=title, citations=citations)

            # Crear una conexión entre el journal y el artículo
            G.add_edge(journal, doi)

            # Crear un nodo para el país y conectar con el artículo
            G.add_node(country)
            G.add_edge(doi, country)

    return G


def dibujar_grafo(journals, ruta_guardado):
    G = generar_grafo(journals)

    # Crear diccionarios para almacenar nodos por tipo
    nodos_journals = []
    nodos_articles = []
    nodos_countries = []

    # Clasificar nodos en journals, artículos y países
    for nodo in G.nodes():
        if nodo in [j[0] for j in journals]:  # Si el nodo está en la lista de journals
            nodos_journals.append(nodo)
        elif isinstance(nodo, str) and len(nodo) == 2:  # Asumir que los países son códigos de dos letras
            nodos_countries.append(nodo)
        else:
            nodos_articles.append(nodo)

    # Asignar tamaños de nodos basados en su grado
    node_sizes = [G.degree(nodo) * 100 for nodo in G.nodes()]

    # Asignar colores a cada tipo de nodo
    color_map = []
    for nodo in G.nodes():
        if nodo in nodos_journals:
            color_map.append('skyblue')
        elif nodo in nodos_countries:
            color_map.append('lightgreen')
        else:
            color_map.append('salmon')

    # Dibujar el grafo
    pos = nx.spring_layout(G, k=0.5)  # Ajusta 'k' para mejorar el espaciado
    plt.figure(figsize=(15, 15))
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=color_map)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='black')
    plt.title("Relación entre journals, artículos y países")
    plt.savefig(ruta_guardado)
    plt.clf()

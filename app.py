from flask import Flask, render_template
from src.utils import graphics_util, sqlite_util
from src.analysis import data_analysis, order_methods_time_graphics
import os




app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/datos_bibliometricos')
def datos_bibliometricos():
    # Genera los gráficos aquí o llama a tus métodos

    #Autores con mas cantidad de articulos
    data = sqlite_util.obtener_autores_frecuentes()
    graphics_util.realizar_graficos(data, "Autores con mas cantidad de publicaciones", "Autores de publicaciones",
                                    "Cantidad de articulos", "linea", "static/images/autores_frecuentes.png")

    #Bases de datos con mas publicaciones
    datos = sqlite_util.obtener_bds_frecuentes()
    graphics_util.realizar_graficos(datos, "Bases de datos con mas publicaciones", "Bases de datos",
                                    "Cantidad de articulos", "linea", "static/images/bds_frecuentes.png")

    #Anios en los que se realizaron mas publicaciones
    datos = sqlite_util.obtener_publicaciones_anio()
    graphics_util.realizar_graficos(datos, "Años en los que se realizaron publicaciones", "Año",
                                    "Cantidad de articulos", "linea", "static/images/publicaciones_anio.png")

    #Journals con mas articulos
    datos = sqlite_util.obtener_jorunals_frecuentes()
    graphics_util.realizar_graficos(datos, "Journals con mas cantidad de articulos", "Journals",
                                    "Cantidad de articulos", "linea", "static/images/journals_frecuentes.png")

    #Publisher con mas articulos
    datos = sqlite_util.obtener_publishers_frecuentes()
    graphics_util.realizar_graficos(datos, "Publishers con mas cantidad de articulos", "Publishers",
                                    "Cantidad de articulos", "linea", "static/images/publishers_frecuentes.png")

    #Tipos de publicaciones con mas articulos
    datos = sqlite_util.obtener_tipo_publicaciones_frecuentes()
    graphics_util.realizar_graficos(datos, "Tipos de publicaciones con mas cantidad de articulos", "Tipo publicación",
                                    "Cantidad de articulos", "linea", "static/images/tipo_publicaciones_frecuentes.png")

    #Aparición de conceptos
    datos = data_analysis.obtener_frecuencia_categoria()
    graphics_util.realizar_graficos(datos, "Frecuencia de aparición de conceptos", "Categoria",
                                    "Apariciones", "barra", "static/images/frecuencia_categoria.png")

    #Nube de palabras
    graphics_util.generar_nube_palabras(sqlite_util.obtener_abstracts(), data_analysis.keywords, "static/images/nube_palabras.png")

    #Grafo
    graphics_util.dibujar_grafo(sqlite_util.obtener_journals_top_10(), "static/images/relacion_journal_articulos_paises.png" )


    return render_template('datos_bibliometricos.html')

@app.route('/metodos_ordenamiento')
def metodos_ordenamiento():
    cantidad_registros = sqlite_util.obtener_cantidad_publicaciones()
    print(cantidad_registros)

    order_methods_time_graphics.graficar_tiempo_ejecucion_anio()
    order_methods_time_graphics.graficar_tiempo_ejecucion_publisher()
    order_methods_time_graphics.graficar_tiempo_ejecucion_primer_autor()
    order_methods_time_graphics.graficar_tiempo_ejecucion_journal()
    order_methods_time_graphics.graficar_tiempo_ejecucion_titulo()

    return render_template('metodos_ordenamiento.html', cantidad_registros=cantidad_registros)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)


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
    # Define la ruta de las imágenes
    image_paths = {
        "autores_frecuentes": "static/images/autores_frecuentes.png",
        "bds_frecuentes": "static/images/bds_frecuentes.png",
        "publicaciones_anio": "static/images/publicaciones_anio.png",
        "journals_frecuentes": "static/images/journals_frecuentes.png",
        "publishers_frecuentes": "static/images/publishers_frecuentes.png",
        "tipo_publicaciones_frecuentes": "static/images/tipo_publicaciones_frecuentes.png",
        "frecuencia_categoria": "static/images/frecuencia_categoria.png",
        "nube_palabras": "static/images/nube_palabras.png",
        "relacion_journal_articulos_paises": "static/images/relacion_journal_articulos_paises.png"
    }

    # Verifica si cada imagen existe
    images_exist = {key: os.path.exists(path) for key, path in image_paths.items()}

    return render_template('datos_bibliometricos.html', images_exist=images_exist)

@app.route('/generar_imagen/<imagen_tipo>', methods=['POST'])
def generar_imagen(imagen_tipo):
    try:
        if imagen_tipo == 'autores_frecuentes':
            data = sqlite_util.obtener_autores_frecuentes()
            graphics_util.realizar_graficos(data, "Autores con mas cantidad de publicaciones", "Autores de publicaciones",
                                            "Cantidad de articulos", "linea", "static/images/autores_frecuentes.png")
        elif imagen_tipo == 'bds_frecuentes':
            datos = sqlite_util.obtener_bds_frecuentes()
            graphics_util.realizar_graficos(datos, "Bases de datos con mas publicaciones", "Bases de datos",
                                            "Cantidad de articulos", "linea", "static/images/bds_frecuentes.png")
        elif imagen_tipo == 'publicaciones_anio':
            datos = sqlite_util.obtener_publicaciones_anio()
            graphics_util.realizar_graficos(datos, "Años en los que se realizaron publicaciones", "Año",
                                            "Cantidad de articulos", "linea", "static/images/publicaciones_anio.png")
        elif imagen_tipo == 'journals_frecuentes':
            datos = sqlite_util.obtener_jorunals_frecuentes()
            graphics_util.realizar_graficos(datos, "Journals con mas cantidad de articulos", "Journals",
                                    "Cantidad de articulos", "linea", "static/images/journals_frecuentes.png")
        elif imagen_tipo == 'publishers_frecuentes':
            datos = sqlite_util.obtener_publishers_frecuentes()
            graphics_util.realizar_graficos(datos, "Publishers con mas cantidad de articulos", "Publishers",
                                    "Cantidad de articulos", "linea", "static/images/publishers_frecuentes.png")
        elif imagen_tipo == 'tipo_publicaciones_frecuentes':
            datos = sqlite_util.obtener_tipo_publicaciones_frecuentes()
            graphics_util.realizar_graficos(datos, "Tipos de publicaciones con mas cantidad de articulos","Tipo publicación", "Cantidad de articulos", "linea","static/images/tipo_publicaciones_frecuentes.png")
        elif imagen_tipo == 'frecuencia_categoria':
            datos = data_analysis.obtener_frecuencia_categoria()
            graphics_util.realizar_graficos(datos, "Frecuencia de aparición de conceptos", "Categoria",
                                            "Apariciones", "barra", "static/images/frecuencia_categoria.png")
        elif imagen_tipo == 'nube_palabras':
            graphics_util.generar_nube_palabras(data_analysis.obtener_frecuencia_palabras(),
                                                "static/images/nube_palabras.png")
        elif imagen_tipo == 'relacion_journal_articulos_paises':
            graphics_util.dibujar_grafo(sqlite_util.obtener_journals_top_10(),
                                        "static/images/relacion_journal_articulos_paises.png")
        elif imagen_tipo == 'tiempo_ejecucion_journal':
            order_methods_time_graphics.graficar_tiempo_ejecucion_journal()
        elif imagen_tipo == 'tiempo_ejecucion_ordenamiento_anio':
            order_methods_time_graphics.graficar_tiempo_ejecucion_anio()
        elif imagen_tipo == 'tiempo_ejecucion_ordenamiento_titulo':
            order_methods_time_graphics.graficar_tiempo_ejecucion_titulo()
        elif imagen_tipo == 'tiempo_ejecucion_primer_autor':
            order_methods_time_graphics.graficar_tiempo_ejecucion_primer_autor()
        elif imagen_tipo == 'tiempo_ejecucion_publisher':
            order_methods_time_graphics.graficar_tiempo_ejecucion_publisher()

        return {"success": True}

    except Exception as e:
        print(f"Error al generar la imagen {imagen_tipo}: {e}")
        return {"success": False}
@app.route('/metodos_ordenamiento')
def metodos_ordenamiento():
    image_paths = {
        "tiempo_ejecucion_journal": "static/images/tiempo_ejecucion_journal.png",
        "tiempo_ejecucion_ordenamiento_anio": "static/images/tiempo_ejecucion_ordenamiento_anio.png",
        "tiempo_ejecucion_ordenamiento_titulo": "static/images/tiempo_ejecucion_ordenamiento_titulo.png",
        "tiempo_ejecucion_primer_autor": "static/images/tiempo_ejecucion_primer_autor.png",
        "tiempo_ejecucion_publisher": "static/images/tiempo_ejecucion_publisher.png"
    }
    # Verifica si cada imagen existe
    images_exist = {key: os.path.exists(path) for key, path in image_paths.items()}

    cantidad_registros = sqlite_util.obtener_cantidad_publicaciones()


    return render_template('metodos_ordenamiento.html', cantidad_registros=cantidad_registros, images_exist=images_exist)

if __name__ == '__main__':
    app.run(debug=True)


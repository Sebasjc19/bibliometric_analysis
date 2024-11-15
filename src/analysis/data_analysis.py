import re
from collections import defaultdict, Counter

from src.utils import sqlite_util

keywords = {
    "Habilidades": [
        "Abstraction", "Algorithm", "Algorithmic thinking", "Coding", "Collaboration", "Cooperation",
        "Creativity", "Critical thinking", "Debug", "Decomposition", "Evaluation", "Generalization",
        "Logic", "Logical thinking", "Modularity", "Patterns recognition", "Problem solving",
        "Programming", "Representation", "Reuse", "Simulation"
    ],
    "Conceptos_Computacionales": [
        "Conditionals", "Control structures", "Directions", "Events", "Functions", "Loops",
        "Modular structure", "Parallelism", "Sequences", "Software/hardware", "Variables"
    ],
    "Actitudes": [
        "Emotional", "Engagement" ,"Motivation", "Perceptions", "Persistence", "Self-efficacy", "Self-perceived"
    ],
    "Propiedades psicométricas": [
        "Classical Test Theory - CTT", "Confirmatory Factor Analysis - CFA", "Exploratory Factor Analysis - EFA",
        "Item Response Theory (IRT) - IRT", "Reliability", "Structural Equation Model - SEM", "Validity"
    ],
    "Herramienta de evaluación": [
        "Beginners Computational Thinking test - BCTt", "Coding Attitudes Survey - ESCAS", "Collaborative Computing Observation Instrument",
        "Competent Computational Thinking test - cCTt", "Computational thinking skills test - CTST", "Computational concepts",
        "Computational Thinking Assessment for Chinese Elementary", "Students - CTA-CES", "Computational Thinking Challenge - CTC",
        "Computational Thinking Levels Scale - CTLS", "Computational Thinking Scale - CTS", "Computational Thinking Skill Levels Scale - CTS",
        "Computational Thinking Test - CTt", "Computational Thinking Test", "Computational Thinking Test for Elementary School Students - CTT-ES",
        "Computational Thinking Test for Lower Primary - CTtLP", "Computational thinking-skill tasks on numbers and arithmetic", "Computerized Adaptive Programming Concepts Test - CAPCT",
        "CT Scale - CTS","Elementary Student Coding Attitudes Survey - ESCAS", "General self-efficacy scale", "ICT competency test",
        "Instrument of computational identity", "KBIT fluid intelligence subtest", "Mastery of computational concepts Test and an Algorithmic Test",
        "Multidimensional 21st Century Skills Scale", "Self-efficacy scale", "STEM learning attitude scale - STEM-LAS", "The computational thinking scale"
    ],
    "Diseño de investigación": [
        "No experimental", "Experimental", "Longitudinal research", "Mixed methods", "Post-test", "Pre-test", "Quasi-experiments"
    ],
    "Nivel de escolaridad": [
        "Upper elementary education - Upper elementary school", "Primary school - Primary education - Elementary school", "Early childhood education – Kindergarten -Preschool",
        "Secondary school - Secondary education", "high school - higher education", "University – College"
    ],
    "Medio": [
        "Block programming", "Mobile application", "Pair programming", "Plugged activities", "Programming", "Robotics", "Spreadsheet",
        "STEM", "Unplugged activities"
    ],
    "Estrategia": [
        "Construct-by-self mind mapping - CBS-MM", "Construct-on-scaffold mind mapping - COS-MM", "Design-based learning - CTDBL",
        "Design-based learning - DBL", "Evidence-centred design approach", "Gamification", "Reverse engineering pedagogy - REP",
        "Technology-enhanced learning", "Collaborative learning", "Cooperative learning", "Flipped classroom", "Game-based learning",
        "Inquiry-based learning", "Personalized learning", "Problem-based learning", "Project-based learning", "Universal design for learning"
    ],
    "Herramienta": [
        "Alice", "Arduino", "Scratch", "ScratchJr", "Blockly Games", "Code.org", "Codecombat", "CSUnplugged", "Robot Turtles", "Hello Ruby",
        "Kodable", "LightbotJr", "KIBO robots", "BEE BOT", "CUBETTO", "Minecraft", "Agent Sheets", "Mimo", "Py– Learn", "SpaceChem"
    ]
}

def obtener_frecuencia_categoria_variable():
    # Crear un diccionario para almacenar la frecuencia de cada palabra en cada categoría
    frecuencia = {categoria: defaultdict(int) for categoria in keywords.keys()}

    abstracts = [pub[0].lower() for pub in sqlite_util.obtener_abstracts()]

    # Contar las palabras clave en los abstracts
    for abstract in abstracts:
        for categoria, palabras in keywords.items():
            for palabra in palabras:
                # Crear patrón regex para palabra o sus sinónimos
                patron = r'\b(' + '|'.join(palabra.lower().split(' - ')) + r')\b'
                # Contar ocurrencias en el abstract
                ocurrencias = len(re.findall(patron, abstract))
                frecuencia[categoria][palabra.split(' - ')[0]] += ocurrencias
    return frecuencia

def obtener_frecuencia_categoria():
    # Obtener la frecuencia de palabras clave en abstracts
    frecuencia = obtener_frecuencia_categoria_variable()
    # Crear un diccionario para almacenar el total de apariciones por categoría
    total_apariciones = {categoria: 0 for categoria in frecuencia.keys()}

    # Sumar las frecuencias por categoría
    for categoria, palabras in frecuencia.items():
        total_apariciones[categoria] = sum(palabras.values())

    return total_apariciones

def obtener_frecuencia_palabras():
    #Obtener los abstracts de la base de datos
    abstracts = [pub[0] for pub in sqlite_util.obtener_abstracts()]

    #Contar la frecuencia de palabras clave
    palabras_clave = [clave for categoria in keywords.values() for clave in categoria]
    frecuencias = Counter()

    for abstract in abstracts:
        # Convertir a minúsculas y eliminar caracteres no deseados
        texto = abstract.lower()
        texto = re.sub(r'[^a-záéíóúñü\s]', '', texto)

        # Contar la frecuencia de palabras clave
        for palabra in palabras_clave:
            if palabra.lower() in texto:
                frecuencias[palabra] += 1
    return frecuencias

import streamlit as st
import os

# Configuración de la página (debe ser el primer comando)
st.set_page_config(page_title="Análisis Depresión", layout="wide")

# Usamos HTML y CSS para centrar el título y darle color verde claro
st.markdown("""
    <h1 style="text-align: center; color: lightgreen;">Proyecto Final</h1>
""", unsafe_allow_html=True)

st.markdown("## Integrantes:")
st.write("")
st.write("Saúl Eduardo Andino Quijada")
st.write("Natalia Sofía Coto Mendoza")
st.write("Helen Esmeralda Gil Alvarez")
st.write("Julia Beatriz Henriquez Mendoza")

st.markdown("""
    <h2 style="text-align: center; color: #4CAF50;">🔆 Bienvenidos 🔆</h2>
""", unsafe_allow_html=True)

Este proyecto incluye las siguientes páginas:""")
st.header("EDA: Análisis Exploratorio de Datos")
st.write("Este proyecto utilizó el conjunto de datos *Student Depression Dataset*, donde el objetivo es poder analizar y relacionar patrones que existen en los hábitos de los estudiantes.")

# Columnas para mostrar las imágenes
col1, col2 = st.columns([2, 2])
with col1:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/tabla.png", width=350)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""Este dataset cuenta con 27,901 filas y 18 columnas.
Algunas columnas son cuantitativas (por ejemplo, CGPA, Work/Study Hours), y otras son cualitativas (por ejemplo, Gender, City).
Notamos que hay una columna con valores faltantes (Financial Stress) que tiene 27,898 valores no nulos, lo que indica 3 valores faltantes.""")

# Otra sección de imágenes y texto
col3, col4 = st.columns([2, 2])
with col3:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/Dep.jpg", width=350)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.subheader("Hipótesis Propuestas")
    st.markdown("""En esta página se presentarán las hipótesis realizadas al principio mediante gráficos.
    Utilizamos las siguientes hipótesis para crear las gráficas:""")

st.write("""1. Los estudiantes de género masculino tienen mayores probabilidades de estar deprimidos.
2. Los estudiantes con buenos hábitos alimenticios tienen menos probabilidades de estar deprimidos.
3. Los estudiantes con mejor desempeño académico (CGPA) tienen menos probabilidades de estar deprimidos.
4. Los estudiantes que estudian más horas a la semana tienen menos probabilidades de estar deprimidos.
5. Los estudiantes con patrones de sueño irregulares tienen mayores probabilidades de estar deprimidos.""")

st.title("Modelos")
st.write("Se seleccionó el algoritmo **Random Forest**, que ofrece robustez frente a datos complejos y permite capturar relaciones no lineales entre las variables.")

# Columnas para mostrar imágenes
col5, col6 = st.columns([2, 2])
with col5:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/random.jpg", width=350)
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.subheader("Random Forest")
    st.markdown("Random Forest es un algoritmo de aprendizaje supervisado basado en la combinación de múltiples árboles de decisión para mejorar la precisión y reducir el riesgo de sobreajuste.")

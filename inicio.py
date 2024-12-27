import streamlit as st
import os

st.set_page_config(page_title="análisis_depresión")
layout="wide"
st.title("Proyecto Final")
st.write("integrantes:")
st.write("Saúl Eduardo Andino Quijada")
st.write("Natalia Sofía Coto Mendoza")
st.write("Helen Esmeralda Gil Alvarez")
st.write("Julia Beatriz Henriquez Mendoza")

st.markdown("""
#Bienvenido,
Este proyecto incluye las siguientes páginas:""")
st.header("EDA: Análisis Exploratorio de Datos")
st.write("Este proyecto utilizó el conjunto de datos *Student Depression Dataset* en donde el objetivo es poder analizar y relacionar patrones que existen en los hábitos de los estudiantes")
col1, col2= st.columns([2,2])
with col1:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/tabla.png", width=250)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""Este dataset cuenta con 27,901 filas y 18 columnas.
Algunas columnas son cuantitativas (por ejemplo, CGPA, Work/Study Hours), y otras son cualitativas (por ejemplo, Gender, City).
Notamos que hay una columna con valores faltantes (Financial Stress) que tiene 27,898 valores no nulos, lo que indica 3 valores faltantes.""")

col3, col4= st.columns([2,2])
with col3:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/Dep.jpg", width=250)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.subheader("Hipótesis Propuestas")
    st.markdown("""En esta página se presentará las hipótesis hechas en un principio mediante gráficos
    utilizamos las siguientes hipotesis para crear las gráficas:""")
    
    
st.write("""1.Los estudiantes de genero masculino tienen mayores probabilidades de estar deprimidos.

2.Los estudiantes con buenos hábitos alimenticios tienen menos probabilidades de estar deprimidos.

3.Los estudiantes con mejor desempeño académico (CGPA) tienen menos probabilidades de estar deprimidos.

4.Los estudiantes que estudian más horas a la semana tienen menos probabilidades de estar deprimidos.

5.Los estudiantes con patrones de sueño irregulares tienen mayores probabilidades de estar deprimidos.""")



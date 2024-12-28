import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset solo una vez
df = pd.read_csv('data/Student Depression Dataset.csv')

# Título principal de la aplicación
st.title("Análisis de Depresión Estudiantil")

# Estilo personalizado para mejorar la apariencia
st.markdown("""
<style>
    .header {
        color: #4CAF50;
        text-align: center;
        font-size: 30px;
        margin-top: 30px;
    }
    .subheader {
        color: #333;
        font-size: 24px;
        margin-top: 20px;
    }
    .conclusion-title {
        color: #4CAF50;
        font-size: 20px;
        margin-top: 20px;
    }
    .conclusion {
        font-size: 16px;
        margin-top: 20px;
        color: #555;
    }
    .graph {
        margin-top: 20px;
        margin-bottom: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Hipótesis 1 - Gráfica de Género
st.subheader("Hipótesis 1: Género y Depresión")
st.markdown("**Hipótesis:** Los estudiantes de género masculino tienen mayores probabilidades de estar deprimidos.")

# Filtrar los estudiantes deprimidos
depressed_students = df[df['Depression'] == 1]

# Contar los géneros de los estudiantes deprimidos
gender_counts = depressed_students['Gender'].value_counts()

# Contar los géneros en el total de estudiantes
total_gender_counts = df['Gender'].value_counts()

# Calcular el porcentaje de estudiantes deprimidos por género
gender_percentages = (gender_counts / total_gender_counts) * 100

# Crear el gráfico
fig, ax = plt.subplots(figsize=(6, 5))
gender_percentages.plot(kind='bar', color=['blue', 'pink'], alpha=0.7, ax=ax)
ax.set_title('Porcentaje de Estudiantes Deprimidos por Género', fontsize=14)
ax.set_ylabel('Porcentaje (%)', fontsize=12)
ax.set_xlabel('Género', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
for i, percentage in enumerate(gender_percentages):
    ax.text(i, percentage + 0.5, f'{percentage:.2f}%', ha='center', fontsize=10)

st.pyplot(fig, use_container_width=True)

# **Conclusión** para Hipótesis 1
st.markdown("<div class='conclusion-title'>Conclusión:</div><div class='conclusion'>Los datos muestran que hay una mayor cantidad de hombres deprimidos en comparación con las mujeres. Sin embargo, al calcular la proporción, las diferencias de género no parecen ser tan significativas, lo que sugiere que ambos géneros enfrentan riesgos similares de depresión.</div>", unsafe_allow_html=True)

# Hipótesis 2 - Hábitos Alimenticios y Depresión
st.subheader("Hipótesis 2: Hábitos Alimenticios y Depresión")
st.markdown("**Hipótesis:** Los estudiantes con buenos hábitos alimenticios tienen menos probabilidades de estar deprimidos.")

# Filtrar estudiantes con diferentes hábitos alimenticios
studentH_notdepressed = df[(df['Dietary Habits'] == 'Healthy') & (df['Depression'] == 0)]
contador_SH_notdepressed = len(studentH_notdepressed)

studentH_depressed = df[(df['Dietary Habits'] == 'Healthy') & (df['Depression'] == 1)]
contador_SH_depressed = len(studentH_depressed)

student_notdepressed = df[(df['Dietary Habits'] == 'Moderate') & (df['Depression'] == 0)]
contador_SM_notdepressed = len(student_notdepressed)

student_depressed = df[(df['Dietary Habits'] == 'Moderate') & (df['Depression'] == 1)]
contador_SM_depressed = len(student_depressed)

student_unhealthy_notdepressed = df[(df['Dietary Habits'] == 'Unhealthy') & (df['Depression'] == 0)]
contador_SU_notdepressed = len(student_unhealthy_notdepressed)

student_unhealthy_depressed = df[(df['Dietary Habits'] == 'Unhealthy') & (df['Depression'] == 1)]
contador_SU_depressed = len(student_unhealthy_depressed)

# Calcular los porcentajes
total_studentH = len(df[df['Dietary Habits'] == 'Healthy'])
total_student = len(df[df['Dietary Habits'] == 'Moderate'])
total_studentU = len(df[df['Dietary Habits'] == 'Unhealthy'])

Porcentaje_Hnotdepressed = contador_SH_notdepressed / total_studentH * 100
Porcentaje_Hdepressed = contador_SH_depressed / total_studentH * 100
porcentaje_mnotdepressed = contador_SM_notdepressed / total_student * 100
porcentaje_mdepressed = contador_SM_depressed / total_student * 100
porcentaje_Unotdepressed = contador_SU_notdepressed / total_studentU * 100
porcentaje_Udepressed = contador_SU_depressed / total_studentU * 100

# Graficar Estudiantes sin Depresión
dh = ['Healthy', 'Moderate', 'Unhealthy']
percentages_notdepressed = [Porcentaje_Hnotdepressed, porcentaje_mnotdepressed, porcentaje_Unotdepressed]

fig, ax = plt.subplots(figsize=(6, 5))
ax.bar(dh, percentages_notdepressed, color=['green', 'orange', 'red'])
ax.set_title('Estudiantes sin depresión', fontsize=14)
ax.set_xlabel('Hábitos Alimenticios', fontsize=12)
ax.set_ylabel('Porcentaje sin depresión (%)', fontsize=12)
for i, v in enumerate(percentages_notdepressed):
    ax.text(i, v + 1, f'{v:.2f}%', ha='center', fontsize=10)

st.pyplot(fig, use_container_width=True)

# Graficar Estudiantes con Depresión
percentages_depressed = [Porcentaje_Hdepressed, porcentaje_mdepressed, porcentaje_Udepressed]

fig, ax = plt.subplots(figsize=(6, 5))
ax.bar(dh, percentages_depressed, color=['green', 'orange', 'red'])
ax.set_title('Estudiantes con depresión', fontsize=14)
ax.set_xlabel('Hábitos Alimenticios', fontsize=12)
ax.set_ylabel('Porcentaje de estudiantes deprimidos (%)', fontsize=12)
for i, v in enumerate(percentages_depressed):
    ax.text(i, v + 1, f'{v:.2f}%', ha='center', fontsize=10)

st.pyplot(fig, use_container_width=True)

# **Conclusión** para Hipótesis 2
st.markdown("<div class='conclusion-title'>Conclusión:</div><div class='conclusion'>Los estudiantes con hábitos alimenticios saludables tienen el mayor porcentaje de no depresión (54.61%), mientras que aquellos con hábitos moderados y no saludables muestran porcentajes significativamente más bajos. Esto respalda la hipótesis de que una dieta equilibrada podría contribuir a un menor riesgo de depresión.</div>", unsafe_allow_html=True)

# Hipótesis 3 - CGPA y Depresión
st.subheader("Hipótesis 3: CGPA y Depresión")
st.markdown("**Hipótesis:** Los estudiantes con mejor desempeño académico (CGPA) tienen menos probabilidades de estar deprimidos.")

# Graficar Promedio de CGPA por Estado de Depresión
promedio_cgpa_por_depresion = df.groupby('Depression')['CGPA'].mean()
porcentajes_cgpa = (promedio_cgpa_por_depresion / promedio_cgpa_por_depresion.sum()) * 100

fig, ax = plt.subplots(figsize=(6, 5))
porcentajes_cgpa.plot(kind='bar', color=['green', 'red'], alpha=0.7, ax=ax)
ax.set_title('Porcentaje de CGPA por Estado de Depresión', fontsize=14)
ax.set_xlabel('Estado de Depresión', fontsize=12)
ax.set_ylabel('Porcentaje del Promedio de CGPA (%)', fontsize=12)
ax.set_xticklabels(['No Deprimidos', 'Deprimidos'], rotation=0)
ax.set_ylim(0, porcentajes_cgpa.max() + 10)
for index, value in enumerate(porcentajes_cgpa):
    ax.text(index, value + 1, f'{value:.2f}%', ha='center', fontsize=12)

st.pyplot(fig, use_container_width=True)

# **Conclusión** para Hipótesis 3
st.markdown("<div class='conclusion-title'>Conclusión:</div><div class='conclusion'>El análisis revela que los estudiantes deprimidos tienen un porcentaje de promedio académico (CGPA) ligeramente superior (50.22%) al de los no deprimidos (49.78%). Esto sugiere que el desempeño académico por sí solo no es un predictor claro de depresión, y puede haber otros factores en juego, como el estrés asociado al rendimiento académico.</div>", unsafe_allow_html=True)

# Hipótesis 4 - Horas de Estudio y Depresión
st.subheader("Hipótesis 4: Horas de Estudio y Depresión")
st.markdown("**Hipótesis:** Los estudiantes que estudian más horas a la semana tienen menos probabilidades de estar deprimidos.")

# Graficar Promedio de Work/Study Hours por Estado de Depresión
promedio_Work_Study_Hours_por_depresion = df.groupby('Depression')['Work/Study Hours'].mean()
porcentajes_Work_Study_Hours = (promedio_Work_Study_Hours_por_depresion / promedio_Work_Study_Hours_por_depresion.sum()) * 100

fig, ax = plt.subplots(figsize=(6, 5))
porcentajes_Work_Study_Hours.plot(kind='bar', color=['blue', 'purple'], alpha=0.7, ax=ax)
ax.set_title('Porcentaje de Work/Study Hours por Estado de Depresión', fontsize=14)
ax.set_xlabel('Estado de Depresión', fontsize=12)
ax.set_ylabel('Porcentaje del Total de Work/Study Hours (%)', fontsize=12)
ax.set_xticklabels(['No Deprimidos', 'Deprimidos'], rotation=0)
for index, value in enumerate(porcentajes_Work_Study_Hours):
    ax.text(index, value + 1, f'{value:.2f}%', ha='center', fontsize=12)
ax.set_ylim(0, porcentajes_Work_Study_Hours.max() + 10)

st.pyplot(fig, use_container_width=True)

# **Conclusión** para Hipótesis 4
st.markdown("<div class='conclusion-title'>Conclusión:</div><div class='conclusion'>Los estudiantes deprimidos dedican un mayor porcentaje de tiempo (55.59%) a trabajar y estudiar en comparación con los no deprimidos (44.41%). Este resultado contradice la hipótesis inicial, indicando que estudiar más horas podría estar relacionado con un mayor nivel de estrés y un riesgo más alto de depresión.</div>", unsafe_allow_html=True)

# Hipótesis 5 - Patrones de Sueño y Depresión
st.subheader("Hipótesis 5: Patrones de Sueño y Depresión")
st.markdown("**Hipótesis:** Los estudiantes con patrones de sueño irregulares tienen mayores probabilidades de estar deprimidos.")

# Filtrar estudiantes con menos de 5 horas de sueño
irregular_sleep = df[df['Sleep Duration'] == 'Less than 5 hours']

# Calcular el número de deprimidos y no deprimidos
depression_counts = irregular_sleep['Depression'].value_counts()

# Crear el gráfico de pastel
fig, ax = plt.subplots(figsize=(6, 5))
ax.pie(depression_counts, labels=['Deprimidos', 'No Deprimidos'], autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
ax.set_title('Porcentaje de Depresión en Estudiantes con Patrones de Sueño Irregulares')

st.pyplot(fig, use_container_width=True)

# **Conclusión** para Hipótesis 5
st.markdown("<div class='conclusion-title'>Conclusión:</div><div class='conclusion'>Los datos muestran que los estudiantes deprimidos tienden a tener patrones de sueño menos regulares en comparación con los no deprimidos. Esto apoya la hipótesis de que los patrones de sueño irregulares pueden ser un factor de riesgo para la depresión.</div>", unsafe_allow_html=True)
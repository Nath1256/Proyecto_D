import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset solo una vez
df = pd.read_csv('data/Student Depression Dataset.csv')

# Título principal de la aplicación
st.title("Análisis de Depresión Estudiantil")

# Hipótesis 1 - Gráfica de Género
st.subheader("Hipótesis 1: Género y Depresión")
# Mostrar la hipótesis antes del gráfico
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
ax = gender_percentages.plot(kind='bar', color=['blue', 'pink'], alpha=0.7)
plt.title('Porcentaje de Estudiantes Deprimidos por Género')
plt.ylabel('Porcentaje (%)')
plt.xlabel('Género')
plt.xticks(rotation=0)

# Agregar los valores de porcentaje encima de las barras
for i, percentage in enumerate(gender_percentages):
    plt.text(i, percentage + 0.5, f'{percentage:.2f}%', ha='center', fontsize=10)

# Mostrar la gráfica en Streamlit
st.pyplot(plt)

# **Conclusión** para Hipótesis 1
st.markdown("**Conclusión:** Los datos muestran que hay una mayor cantidad de hombres deprimidos en comparación con las mujeres. Sin embargo, al calcular la proporción, las diferencias de género no parecen ser tan significativas, lo que sugiere que ambos géneros enfrentan riesgos similares de depresión.")

# Hipótesis 2 - Hábitos Alimenticios y Depresión
st.subheader("Hipótesis 2: Hábitos Alimenticios y Depresión")
# Mostrar la hipótesis antes del gráfico
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

plt.figure(figsize=(7, 6))
plt.bar(dh, percentages_notdepressed, color=['green', 'orange', 'red'])

plt.title('Estudiantes sin depresión', fontsize=10)
plt.xlabel('Hábitos Alimenticios', fontsize=10)
plt.ylabel('Porcentaje sin depresión (%)', fontsize=10)

for i, v in enumerate(percentages_notdepressed):
    plt.text(i, v + 1, f'{v:.2f}%', ha='center', fontsize=10)

st.pyplot(plt)

# Graficar Estudiantes con Depresión
percentages_depressed = [Porcentaje_Hdepressed, porcentaje_mdepressed, porcentaje_Udepressed]

plt.figure(figsize=(7, 6))
plt.bar(dh, percentages_depressed, color=['green', 'orange', 'red'])

plt.title('Estudiantes con depresión', fontsize=10)
plt.xlabel('Hábitos Alimenticios', fontsize=10)
plt.ylabel('Porcentaje de estudiantes deprimidos (%)', fontsize=10)

for i, v in enumerate(percentages_depressed):
    plt.text(i, v + 1, f'{v:.2f}%', ha='center', fontsize=10)

st.pyplot(plt)

# **Conclusión** para Hipótesis 2
st.markdown("**Conclusión:** Los estudiantes con hábitos alimenticios saludables tienen el mayor porcentaje de no depresión (54.61%), mientras que aquellos con hábitos moderados y no saludables muestran porcentajes significativamente más bajos. Esto respalda la hipótesis de que una dieta equilibrada podría contribuir a un menor riesgo de depresión.")

# Hipótesis 3 - CGPA y Depresión
st.subheader("Hipótesis 3: CGPA y Depresión")
# Mostrar la hipótesis antes del gráfico
st.markdown("**Hipótesis:** Los estudiantes con mejor desempeño académico (CGPA) tienen menos probabilidades de estar deprimidos.")

# Graficar Promedio de CGPA por Estado de Depresión
promedio_cgpa_por_depresion = df.groupby('Depression')['CGPA'].mean()
porcentajes_cgpa = (promedio_cgpa_por_depresion / promedio_cgpa_por_depresion.sum()) * 100

plt.figure(figsize=(8, 6))
porcentajes_cgpa.plot(kind='bar', color=['green', 'red'], alpha=0.7)
plt.title('Porcentaje de CGPA por Estado de Depresión', fontsize=14)
plt.xlabel('Estado de Depresión (0 = No, 1 = Sí)', fontsize=12)
plt.ylabel('Porcentaje del Promedio de CGPA (%)', fontsize=12)
plt.xticks(ticks=[0, 1], labels=['No Deprimidos', 'Deprimidos'], rotation=0)
plt.ylim(0, porcentajes_cgpa.max() + 10)

for index, value in enumerate(porcentajes_cgpa):
    plt.text(index, value + 1, f'{value:.2f}%', ha='center', fontsize=12)

st.pyplot(plt)

# **Conclusión** para Hipótesis 3
st.markdown("**Conclusión:** El análisis revela que los estudiantes deprimidos tienen un porcentaje de promedio académico (CGPA) ligeramente superior (50.22%) al de los no deprimidos (49.78%). Esto sugiere que el desempeño académico por sí solo no es un predictor claro de depresión, y puede haber otros factores en juego, como el estrés asociado al rendimiento académico.")

# Hipótesis 4 - Horas de Estudio y Depresión
st.subheader("Hipótesis 4: Horas de Estudio y Depresión")
# Mostrar la hipótesis antes del gráfico
st.markdown("**Hipótesis:** Los estudiantes que estudian más horas a la semana tienen menos probabilidades de estar deprimidos.")

# Graficar Promedio de Work/Study Hours por Estado de Depresión
promedio_Work_Study_Hours_por_depresion = df.groupby('Depression')['Work/Study Hours'].mean()
porcentajes_Work_Study_Hours = (promedio_Work_Study_Hours_por_depresion / promedio_Work_Study_Hours_por_depresion.sum()) * 100

plt.figure(figsize=(8, 6))
porcentajes_Work_Study_Hours.plot(kind='bar', color=['blue', 'purple'], alpha=0.7)
plt.title('Porcentaje de Work/Study Hours por Estado de Depresión', fontsize=14)
plt.xlabel('Estado de Depresión', fontsize=12)
plt.ylabel('Porcentaje del Total de Work/Study Hours (%)', fontsize=12)
plt.xticks(ticks=[0, 1], labels=['No Deprimidos', 'Deprimidos'], rotation=0)

for index, value in enumerate(porcentajes_Work_Study_Hours):
    plt.text(index, value + 1, f'{value:.2f}%', ha='center', fontsize=12)

plt.ylim(0, porcentajes_Work_Study_Hours.max() + 10)

st.pyplot(plt)

# **Conclusión** para Hipótesis 4
st.markdown("**Conclusión:** Los estudiantes deprimidos dedican un mayor porcentaje de tiempo (55.59%) a trabajar y estudiar en comparación con los no deprimidos (44.41%). Este resultado contradice la hipótesis inicial, indicando que estudiar más horas podría estar relacionado con un mayor nivel de estrés y un riesgo más alto de depresión.")

# Hipótesis 5 - Patrones de Sueño y Depresión
st.subheader("Hipótesis 5: Patrones de Sueño y Depresión")
# Mostrar la hipótesis antes del gráfico
st.markdown("**Hipótesis:** Los estudiantes con patrones de sueño irregulares tienen mayores probabilidades de estar deprimidos.")

# Filtrar estudiantes con menos de 5 horas de sueño
irregular_sleep = df[df['Sleep Duration'] == 'Less than 5 hours']

# Calcular el número de deprimidos y no deprimidos
depression_counts = irregular_sleep['Depression'].value_counts()

# Crear el gráfico de pastel
labels = ['Deprimidos', 'No Deprimidos']
colors = ['red', 'green']

plt.figure(figsize=(8, 6))
plt.pie(depression_counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Porcentaje de Depresión en Estudiantes con Patrones de Sueño Irregulares')
plt.axis('equal')  # Para asegurar que el gráfico sea circular

st.pyplot(plt)

# **Conclusión** para Hipótesis 5
st.markdown("**Conclusión:** Los datos muestran que los estudiantes deprimidos tienden a tener patrones de sueño menos regulares en comparación con los no deprimidos. Esto apoya la hipótesis de que los patrones de sueño irregulares pueden ser un factor de riesgo para la depresión.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('data/Student Depression Dataset.csv')

# Título de la aplicación
st.title("Análisis Exploratorio de Datos (EDA) - Depresión Estudiantil")

# 1. Vista inicial del dataset
st.subheader("Vista Inicial del Dataset")
st.write("Esta sección muestra las primeras filas del dataset para dar un vistazo general a las columnas y los datos disponibles.")
st.write(df.head())  # Muestra las primeras filas

st.write("Información general sobre el dataset, incluyendo tipos de datos y valores nulos:")
st.write(df.info())  # Información general sobre el dataset

st.write("Estadísticas descriptivas de las variables numéricas para entender sus rangos y distribuciones:")
st.write(df.describe())  # Estadísticas descriptivas de las variables numéricas

# 2. Análisis de valores nulos
st.subheader("Análisis de Valores Nulos")
st.write("Se analiza la cantidad de valores faltantes por columna para garantizar la calidad del dataset:")
st.write(df.isnull().sum())  # Número de valores nulos por columna

# 3. Información estadística
st.subheader("Información Estadística")

# Gender distribution
st.write("Distribución de Género")
st.write("Distribución de género en el dataset:")
gender_stats = {
    'Male': 15547,
    'Female': 12354
}
st.write(gender_stats)

# City distribution
st.write("Distribución de Ciudades")
st.write("Distribución de estudiantes por ciudad:")
city_stats = {
    'Kalyan': 1570,
    'Srinagar': 1372,
    'Hyderabad': 1340,
    'Vasai-Virar': 1290,
    'Lucknow': 1155,
    'Thane': 1139,
    'Ludhiana': 1111,
    'Agra': 1094,
    'Surat': 1078,
    'Kolkata': 1066,
    'Jaipur': 1036,
    'Patna': 1007,
    'Visakhapatnam': 969,
    'Pune': 968,
    'Ahmedabad': 951,
    'Bhopal': 934,
    'Chennai': 885,
    'Meerut': 825,
    'Rajkot': 816,
    'Delhi': 768,
    'Bangalore': 767,
    'Ghaziabad': 745,
    'Mumbai': 699,
    'Vadodara': 694,
    'Varanasi': 685,
    'Nagpur': 651,
    'Indore': 643,
    'Kanpur': 609,
    'Nashik': 547,
    'Faridabad': 461,
    'Saanvi': 2,
    'Bhavna': 2,
    'City': 2,
    'Harsha': 2,
    'Kibara': 1,
    'Nandini': 1,
    'Nalini': 1,
    'Mihir': 1,
    'Nalyan': 1,
    'M.Com': 1,
    'ME': 1,
    'Rashi': 1,
    'Gaurav': 1,
    'Reyansh': 1,
    'Harsh': 1,
    'Vaanya': 1,
    'Mira': 1,
    'Less than 5 Kalyan': 1,
    '3.0': 1,
    'Less Delhi': 1,
    'M.Tech': 1,
    'Khaziabad': 1
}
st.write(city_stats)

# Profession distribution
st.write("Distribución de Profesiones")
st.write("Distribución de estudiantes por profesión:")
profession_stats = {
    'Student': 27870,
    'Architect': 8,
    'Teacher': 6,
    'Digital Marketer': 3,
    'Content Writer': 2,
    'Chef': 2,
    'Doctor': 2,
    'Pharmacist': 2,
    'Civil Engineer': 1,
    'UX/UI Designer': 1,
    'Educational Consultant': 1,
    'Manager': 1,
    'Lawyer': 1,
    'Entrepreneur': 1
}
st.write(profession_stats)

# Sleep Duration distribution
st.write("Distribución de Duración de Sueño")
st.write("Distribución de la duración del sueño entre los estudiantes:")
sleep_stats = {
    'Less than 5 hours': 8310,
    '7-8 hours': 7346,
    '5-6 hours': 6183,
    'More than 8 hours': 6044,
    'Others': 18
}
st.write(sleep_stats)

# Dietary Habits distribution
st.write("Distribución de Hábitos Alimenticios")
st.write("Distribución de hábitos alimenticios de los estudiantes:")
diet_stats = {
    'Unhealthy': 10317,
    'Moderate': 9921,
    'Healthy': 7651,
    'Others': 12
}
st.write(diet_stats)

# Degree distribution
st.write("Distribución de Grado Académico")
st.write("Distribución de grados académicos de los estudiantes:")
degree_stats = {
    'Class 12': 6080,
    'B.Ed': 1867,
    'B.Com': 1506,
    'B.Arch': 1478,
    'BCA': 1433,
    'MSc': 1190,
    'B.Tech': 1152,
    'MCA': 1044,
    'M.Tech': 1022,
    'BHM': 925,
    'BSc': 888,
    'M.Ed': 821,
    'B.Pharm': 810,
    'M.Com': 734,
    'MBBS': 696,
    'BBA': 696,
    'LLB': 671,
    'BE': 613,
    'BA': 600,
    'M.Pharm': 582,
    'MD': 572,
    'MBA': 562,
    'MA': 544,
    'PhD': 522,
    'LLM': 482,
    'MHM': 191,
    'ME': 185,
    'Others': 35
}
st.write(degree_stats)

# Family History of Mental Illness distribution
st.write("Distribución de Antecedentes Familiares de Enfermedades Mentales")
st.write("Distribución de antecedentes familiares de enfermedades mentales:")
family_history_stats = {
    'No': 14398,
    'Yes': 13503
}
st.write(family_history_stats)

# Depression distribution
st.write("Distribución de Estado de Depresión")
st.write("Distribución de estudiantes deprimidos y no deprimidos:")
depression_stats = {
    '1': 16336,
    '0': 11565
}
st.write(depression_stats)

# 4. Distribución de las variables
st.subheader("Distribución de Variables Numéricas")

# Histograma de CGPA
st.write("Gráfica: Distribución de CGPA")
st.write("El histograma muestra cómo se distribuyen los valores de CGPA entre los estudiantes. Ayuda a identificar concentraciones y posibles outliers.")
fig, ax = plt.subplots()
df['CGPA'].hist(ax=ax)
ax.set_title("Distribución de CGPA")
ax.set_xlabel("CGPA")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)

# Histograma de Horas de Estudio
st.write("Gráfica: Distribución de Horas de Estudio")
st.write("Esta gráfica muestra la distribución del tiempo semanal dedicado al estudio/trabajo entre los estudiantes.")
fig, ax = plt.subplots()
df['Work/Study Hours'].hist(ax=ax)
ax.set_title("Distribución de Horas de Estudio")
ax.set_xlabel("Horas de Estudio")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)

# 5. Correlación entre variables numéricas
st.subheader("Matriz de Correlación entre Variables Numéricas")
st.write("La matriz de correlación visualiza las relaciones entre variables numéricas del dataset. Los valores cercanos a 1 o -1 indican relaciones fuertes.")

# Seleccionar solo las columnas numéricas
df_numeric = df.select_dtypes(include=['float64', 'int64'])

# Eliminar filas con valores nulos
df_cleaned = df_numeric.dropna()

# Calcular la correlación solo para las columnas numéricas y limpias
corr = df_cleaned.corr()

# Mostrar la matriz de correlación
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
ax.set_title('Matriz de Correlación')
st.pyplot(fig)

# 6. Comparación entre Depresión y otras variables
st.subheader("Comparación entre Depresión y Otras Variables")

# Boxplot de CGPA por Estado de Depresión
st.write("Gráfica: CGPA por Estado de Depresión")
st.write("El boxplot permite comparar la distribución del CGPA entre estudiantes deprimidos y no deprimidos.")
fig, ax = plt.subplots()
sns.boxplot(x='Depression', y='CGPA', data=df, ax=ax)
ax.set_title("CGPA por Estado de Depresión")
st.pyplot(fig)

# Boxplot de Horas de Estudio por Estado de Depresión
st.write("Gráfica: Horas de Estudio por Estado de Depresión")
st.write("Esta gráfica compara la distribución del tiempo semanal dedicado al estudio/trabajo entre ambos grupos.")
fig, ax = plt.subplots()
sns.boxplot(x='Depression', y='Work/Study Hours', data=df, ax=ax)
ax.set_title("Horas de Estudio por Estado de Depresión")
st.pyplot(fig)

# 7. Análisis de Tendencias en Variables Categóricas y Depresión
st.subheader("Análisis de Tendencias en Variables Categóricas y Depresión")

# Gráfico de barras: Depresión vs. Hábitos Alimenticios
st.write("Gráfica: Relación entre Depresión y Hábitos Alimenticios")
st.write("El gráfico muestra cómo las diferentes categorías de hábitos alimenticios se relacionan con el estado de depresión.")
fig, ax = plt.subplots()
df.groupby('Dietary Habits')['Depression'].value_counts().unstack().plot(kind='bar', stacked=True, ax=ax)
ax.set_title("Relación entre Depresión y Hábitos Alimenticios")
st.pyplot(fig)

# Gráfico de barras: Depresión vs. Género
st.write("Gráfica: Relación entre Depresión y Género")
st.write("Aquí se observa cómo se distribuyen los estados de depresión entre estudiantes masculinos y femeninos.")
fig, ax = plt.subplots()
df.groupby('Gender')['Depression'].value_counts().unstack().plot(kind='bar', stacked=True, ax=ax)
ax.set_title("Relación entre Depresión y Género")
st.pyplot(fig)

# 8. Patrones de Sueño y Depresión
st.subheader("Patrones de Sueño y Depresión")

# Filtrar estudiantes con menos de 5 horas de sueño
irregular_sleep = df[df['Sleep Duration'] == 'Less than 5 hours']

# Contar la depresión en estudiantes con sueño irregular
depression_counts = irregular_sleep['Depression'].value_counts()

# Gráfico circular para Patrones de Sueño
st.write("Gráfica: Porcentaje de Depresión en Estudiantes con Patrones de Sueño Irregulares")
st.write("El gráfico circular muestra qué porcentaje de estudiantes con sueño irregular está deprimido.")
fig, ax = plt.subplots()
ax.pie(depression_counts, labels=["Deprimidos", "No Deprimidos"], autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
ax.axis('equal')  # Asegurar que el gráfico sea circular
ax.set_title("Distribución de Depresión en Estudiantes con Sueño Irregular")
st.pyplot(fig)
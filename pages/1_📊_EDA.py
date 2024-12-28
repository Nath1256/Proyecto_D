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

# 3. Distribución de las variables
st.subheader("Distribución de Variables Numéricas")

# Histograma de CGPA
st.write("Gráfica: Distribución de CGPA")
st.write("El histograma muestra cómo se distribuyen los valores de CGPA entre los estudiantes. Ayuda a identificar concentraciones y posibles outliers.")
st.write(df['CGPA'].hist())
st.pyplot()

# Histograma de Work/Study Hours
st.write("Gráfica: Distribución de Horas de Estudio")
st.write("Esta gráfica muestra la distribución del tiempo semanal dedicado al estudio/trabajo entre los estudiantes.")
st.write(df['Work/Study Hours'].hist())
st.pyplot()

# 4. Distribución de variables categóricas
st.subheader("Distribución de Variables Categóricas")

# Gráfico de barras de Género
st.write("Gráfica: Distribución de Género")
st.write("Este gráfico de barras ilustra la proporción de estudiantes masculinos y femeninos en el dataset.")
st.write(df['Gender'].value_counts().plot(kind='bar'))
st.pyplot()

# Gráfico de barras de Hábitos Alimenticios
st.write("Gráfica: Distribución de Hábitos Alimenticios")
st.write("Este gráfico muestra la frecuencia de cada categoría de hábitos alimenticios (Saludables, Moderados, y No Saludables).")
st.write(df['Dietary Habits'].value_counts().plot(kind='bar'))
st.pyplot()

# Gráfico de barras de Estado de Depresión
st.write("Gráfica: Distribución de Estado de Depresión")
st.write("Aquí se observa la proporción de estudiantes deprimidos y no deprimidos en el dataset.")
st.write(df['Depression'].value_counts().plot(kind='bar'))
st.pyplot()

# 5. Correlación entre variables numéricas
st.subheader("Matriz de Correlación entre Variables Numéricas")
st.write("La matriz de correlación visualiza las relaciones entre variables numéricas del dataset. Los valores cercanos a 1 o -1 indican relaciones fuertes.")
corr = df.corr()
st.write(sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1))
st.pyplot()

# 6. Comparación entre Depresión y otras variables
st.subheader("Comparación entre Depresión y Otras Variables")

# Boxplot de CGPA por Estado de Depresión
st.write("Gráfica: CGPA por Estado de Depresión")
st.write("El boxplot permite comparar la distribución del CGPA entre estudiantes deprimidos y no deprimidos.")
st.write(sns.boxplot(x='Depression', y='CGPA', data=df))
st.pyplot()

# Boxplot de Horas de Estudio por Estado de Depresión
st.write("Gráfica: Horas de Estudio por Estado de Depresión")
st.write("Esta gráfica compara la distribución del tiempo semanal dedicado al estudio/trabajo entre ambos grupos.")
st.write(sns.boxplot(x='Depression', y='Work/Study Hours', data=df))
st.pyplot()

# 7. Análisis de Tendencias en Variables Categóricas y Depresión
st.subheader("Análisis de Tendencias en Variables Categóricas y Depresión")

# Gráfico de barras: Depresión vs. Hábitos Alimenticios
st.write("Gráfica: Relación entre Depresión y Hábitos Alimenticios")
st.write("El gráfico muestra cómo las diferentes categorías de hábitos alimenticios se relacionan con el estado de depresión.")
st.write(df.groupby('Dietary Habits')['Depression'].value_counts().unstack().plot(kind='bar', stacked=True))
st.pyplot()

# Gráfico de barras: Depresión vs. Género
st.write("Gráfica: Relación entre Depresión y Género")
st.write("Aquí se observa cómo se distribuyen los estados de depresión entre estudiantes masculinos y femeninos.")
st.write(df.groupby('Gender')['Depression'].value_counts().unstack().plot(kind='bar', stacked=True))
st.pyplot()

# 8. Patrones de Sueño y Depresión
st.subheader("Patrones de Sueño y Depresión")

# Filtrar estudiantes con menos de 5 horas de sueño
irregular_sleep = df[df['Sleep Duration'] == 'Less than 5 hours']

# Contar la depresión en estudiantes con sueño irregular
depression_counts = irregular_sleep['Depression'].value_counts()

# Gráfico circular para Patrones de Sueño
st.write("Gráfica: Porcentaje de Depresión en Estudiantes con Patrones de Sueño Irregulares")
st.write("El gráfico circular muestra qué porcentaje de estudiantes con sueño irregular está deprimido.")
st.write(plt.pie(depression_counts, labels=["Deprimidos", "No Deprimidos"], autopct='%1.1f%%', startangle=90, colors=['red', 'green']))
plt.axis('equal')  # Asegurar que el gráfico sea circular
st.pyplot()
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
st.write(df.head())  # Muestra las primeras filas
st.write(df.info())  # Información general sobre el dataset
st.write(df.describe())  # Estadísticas descriptivas de las variables numéricas

# 2. Análisis de valores nulos
st.subheader("Análisis de Valores Nulos")
st.write(df.isnull().sum())  # Número de valores nulos por columna

# 3. Distribución de las variables
st.subheader("Distribución de Variables Numéricas")

# Histograma de CGPA
st.write("Distribución de CGPA")
fig, ax = plt.subplots()
df['CGPA'].hist(ax=ax, bins=20, color='blue', edgecolor='black')
ax.set_title("Distribución de CGPA")
ax.set_xlabel("CGPA")
ax.set_ylabel("Frecuencia")
st.pyplot(fig)

# Histograma de Work/Study Hours
st.write("Distribución de Horas de Estudio")
st.write(df['Work/Study Hours'].hist())
st.pyplot()

# 4. Distribución de variables categóricas
st.subheader("Distribución de Variables Categóricas")

# Gráfico de barras de Género
st.write("Distribución de Género")
fig, ax = plt.subplots()
df['Gender'].value_counts().plot(kind='bar', ax=ax)
ax.set_title("Distribución de Género")
ax.set_xlabel("Género")
ax.set_ylabel("Cantidad")
st.pyplot(fig)

# Gráfico de barras de Hábitos Alimenticios
st.write("Distribución de Hábitos Alimenticios")
st.write(df['Dietary Habits'].value_counts().plot(kind='bar'))
st.pyplot()

# Gráfico de barras de Estado de Depresión
st.write("Distribución de Estado de Depresión")
st.write(df['Depression'].value_counts().plot(kind='bar'))
st.pyplot()

# 5. Correlación entre variables numéricas
st.subheader("Matriz de Correlación entre Variables Numéricas")
corr = df.corr()
st.write(sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1))
st.pyplot()

# 6. Comparación entre Depresión y otras variables
st.subheader("Comparación entre Depresión y Otras Variables")

# Boxplot de CGPA por Estado de Depresión
st.write("CGPA por Estado de Depresión")
st.write(sns.boxplot(x='Depression', y='CGPA', data=df))
st.pyplot()

# Boxplot de Horas de Estudio por Estado de Depresión
st.write("Horas de Estudio por Estado de Depresión")
st.write(sns.boxplot(x='Depression', y='Work/Study Hours', data=df))
st.pyplot()

# 7. Análisis de Tendencias en Variables Categóricas y Depresión
st.subheader("Análisis de Tendencias en Variables Categóricas y Depresión")

# Gráfico de barras: Depresión vs. Hábitos Alimenticios
st.write("Relación entre Depresión y Hábitos Alimenticios")
st.write(df.groupby('Dietary Habits')['Depression'].value_counts().unstack().plot(kind='bar', stacked=True))
st.pyplot()

# Gráfico de barras: Depresión vs. Género
st.write("Relación entre Depresión y Género")
st.write(df.groupby('Gender')['Depression'].value_counts().unstack().plot(kind='bar', stacked=True))
st.pyplot()

# 8. Patrones de Sueño y Depresión
st.subheader("Patrones de Sueño y Depresión")

# Filtrar estudiantes con menos de 5 horas de sueño
irregular_sleep = df[df['Sleep Duration'] == 'Less than 5 hours']

# Contar la depresión en estudiantes con sueño irregular
depression_counts = irregular_sleep['Depression'].value_counts()

# Gráfico circular para Patrones de Sueño
st.write("Porcentaje de Depresión en Estudiantes con Patrones de Sueño Irregulares")
st.write(plt.pie(depression_counts, labels=["Deprimidos", "No Deprimidos"], autopct='%1.1f%%', startangle=90, colors=['red', 'green']))
plt.axis('equal')  # Asegurar que el gráfico sea circular
st.pyplot()


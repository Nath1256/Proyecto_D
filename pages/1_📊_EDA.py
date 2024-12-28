import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
ax.hist(df['CGPA'])
st.pyplot(fig)

# Histograma de Work/Study Hours
st.write("Distribución de Horas de Estudio")
fig, ax = plt.subplots()
ax.hist(df['Work/Study Hours'])
st.pyplot(fig)

# 4. Distribución de variables categóricas
st.subheader("Distribución de Variables Categóricas")

# Gráfico de barras de Género
st.write("Distribución de Género")
fig, ax = plt.subplots()
df['Gender'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

# Gráfico de barras de Hábitos Alimenticios
st.write("Distribución de Hábitos Alimenticios")
fig, ax = plt.subplots()
df['Dietary Habits'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

# Gráfico de barras de Estado de Depresión
st.write("Distribución de Estado de Depresión")
fig, ax = plt.subplots()
df['Depression'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

# 5. Correlación entre variables numéricas
st.subheader("Matriz de Correlación entre Variables Numéricas")

# Asegurarse de que solo se seleccionen columnas numéricas
df_numeric = df.select_dtypes(include=['float64', 'int64'])

# Rellenar los valores nulos con la media de cada columna
df_numeric = df_numeric.fillna(df_numeric.mean())

# Calcular la matriz de correlación
corr = df_numeric.corr()

# Graficar la matriz de correlación
fig, ax = plt.subplots(figsize=(10, 8))  # Ajustar tamaño de la figura si es necesario
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
st.pyplot(fig)

# 6. Comparación entre Depresión y otras variables
st.subheader("Comparación entre Depresión y Otras Variables")

# Boxplot de CGPA por Estado de Depresión
st.write("CGPA por Estado de Depresión")
fig, ax = plt.subplots()
sns.boxplot(x='Depression', y='CGPA', data=df, ax=ax)
st.pyplot(fig)

# Boxplot de Horas de Estudio por Estado de Depresión
st.write("Horas de Estudio por Estado de Depresión")
fig, ax = plt.subplots()
sns.boxplot(x='Depression', y='Work/Study Hours', data=df, ax=ax)
st.pyplot(fig)

# 7. Análisis de Tendencias en Variables Categóricas y Depresión
st.subheader("Análisis de Tendencias en Variables Categóricas y Depresión")

# Gráfico de barras: Depresión vs. Hábitos Alimenticios
st.write("Relación entre Depresión y Hábitos Alimenticios")
fig, ax = plt.subplots()
df.groupby('Dietary Habits')['Depression'].value_counts().unstack().plot(kind='bar', stacked=True, ax=ax)
st.pyplot(fig)

# Gráfico de barras: Depresión vs. Género
st.write("Relación entre Depresión y Género")
fig, ax = plt.subplots()
df.groupby('Gender')['Depression'].value_counts().unstack().plot(kind='bar', stacked=True, ax=ax)
st.pyplot(fig)

# 8. Patrones de Sueño y Depresión
st.subheader("Patrones de Sueño y Depresión")

# Filtrar estudiantes con menos de 5 horas de sueño
irregular_sleep = df[df['Sleep Duration'] == 'Less than 5 hours']

# Contar la depresión en estudiantes con sueño irregular
depression_counts = irregular_sleep['Depression'].value_counts()

# Gráfico circular para Patrones de Sueño
st.write("Porcentaje de Depresión en Estudiantes con Patrones de Sueño Irregulares")
fig, ax = plt.subplots()
ax.pie(depression_counts, labels=["Deprimidos", "No Deprimidos"], autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
ax.axis('equal')  # Asegurar que el gráfico sea circular
st.pyplot(fig)

# Conclusión General
st.subheader("Conclusión General")
st.write("""
El análisis de los datos revela varias relaciones interesantes entre las variables y la depresión estudiantil:

1. **Género**: Aunque hay más hombres deprimidos que mujeres, las proporciones no son significativamente diferentes, lo que sugiere que ambos géneros enfrentan riesgos similares de depresión.
2. **Hábitos Alimenticios**: Los estudiantes con hábitos alimenticios saludables tienden a tener menos probabilidades de estar deprimidos.
3. **Desempeño Académico (CGPA)**: No se observa una relación clara entre el CGPA y la depresión, lo que indica que el rendimiento académico por sí solo no es un predictor claro de la depresión.
4. **Horas de Estudio**: Los estudiantes deprimidos parecen estar dedicando más tiempo al estudio, lo que podría estar relacionado con el estrés.
5. **Sueño Irregular**: Los estudiantes con menos de 5 horas de sueño tienen una mayor probabilidad de estar deprimidos, lo que sugiere que el sueño irregular es un factor de riesgo significativo para la depresión.
""")
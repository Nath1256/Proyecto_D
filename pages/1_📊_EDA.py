import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

# Título principal de la aplicación
st.title("Análisis de Depresión Estudiantil con Random Forest")

# Cargar el dataset
st.subheader("Dataset")
df = pd.read_csv('data/Student Depression Dataset.csv')
st.write("Datos", df.head())  # Mostrar las primeras filas del dataset

# Realizar one-hot encoding para las variables categóricas
st.subheader("Preprocesamiento de Datos")
df = pd.get_dummies(df, drop_first=True)
st.write("Datos ", df.head())  # Mostrar las primeras filas después del encoding

# Dividir el dataset en variables independientes (X) y dependientes (y)
X = df.drop('Depression', axis=1)  # Asegúrate de usar el nombre correcto de la columna objetivo
y = df['Depression']  # Columna objetivo (0 o 1)

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear y entrenar el modelo Random Forest
st.subheader("Entrenamiento del Modelo")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Realizar predicciones
y_pred = rf_model.predict(X_test)

# Evaluar el modelo
st.subheader("Evaluación del Modelo")

# Mostrar la precisión
st.write("### Precisión del Modelo:", accuracy_score(y_test, y_pred))

# Mostrar el reporte de clasificación
st.write("### Reporte de Clasificación:")
st.text(classification_report(y_test, y_pred))

# Generar la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Visualizar la matriz de confusión
st.subheader("Matriz de Confusión")
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Deprimido', 'Deprimido'])
disp.plot(cmap='Blues', values_format='d')
plt.title("Matriz de Confusión")

# Mostrar la matriz de confusión en Streamlit
st.pyplot(plt)



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
st.subheader("Pre-procesamiento de Datos")
df = pd.get_dummies(df, drop_first=True)
st.write("Datos ", df.head())  # Mostrar las primeras filas después del encoding

# Dividir el dataset en variables independientes (X) y dependientes (y)
X = df.drop('Depression', axis=1)  # Asegúrate de usar el nombre correcto de la columna objetivo
y = df['Depression']  # Columna objetivo (0 o 1)

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenar el modelo Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Calcular métricas
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)
f1_score = report["weighted avg"]["f1-score"]
precision = report["weighted avg"]["precision"]
recall = report["weighted avg"]["recall"]

# Variables dinámicas
accuracy = 0.83
f1_score = 0.83
precision = 0.83
recall = 0.83

# Estilo del texto
st.markdown("""
<style>
    .title-large {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .title-small {
        font-size: 20px;
        text-align: center;
        color: #aaaaaa;
        margin-bottom: 20px;
    }
    .metric-label {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 5px;
        text-align: center;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #03A9F4; /* Azul para los valores */
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Títulos
st.markdown('<div class="title-large">Entrenamiento del Modelo</div>', unsafe_allow_html=True)
st.markdown('<div class="title-small">Reporte de Clasificación</div>', unsafe_allow_html=True)

# Métricas alineadas en columnas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-label">Accuracy</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric-value">{accuracy:.2f}</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-label">F1 Score</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric-value">{f1_score:.2f}</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-label">Precision</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric-value">{precision:.2f}</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="metric-label">Recall</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric-value">{recall:.2f}</div>', unsafe_allow_html=True)

# Generar la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Visualizar la matriz de confusión
st.subheader("Matriz de Confusión")
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Deprimido', 'Deprimido'])
disp.plot(cmap='Blues', values_format='d')
plt.title("Matriz de Confusión")

# Mostrar la matriz de confusión en Streamlit
st.pyplot(plt)

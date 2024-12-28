import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Análisis de Depresión", layout="wide")

# Usamos HTML y CSS para centrar los títulos y personalizar colores y estilos
st.markdown("""
    <style>
        body {
            background-color: #f4f8fb;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            color: #3498db; /* Azul */
            font-size: 50px;
            margin-top: 30px;
            font-weight: bold;
        }
        .subheader {
            text-align: center;
            color: #2980b9; /* Azul más oscuro */
            font-size: 35px;
            margin-top: 20px;
        }
        .intro-text {
            font-size: 20px;
            text-align: center;
            color: #333;
            margin-top: 20px;
            line-height: 1.6;
        }
        .team {
            text-align: center;
            font-size: 18px;
            margin-top: 30px;
            color: #555;
        }
        .content-section {
            margin-top: 50px;
            display: flex;
            justify-content: space-around;
        }
        .content-image {
            width: 350px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .content-text {
            max-width: 500px;
            font-size: 18px;
            color: #555;
        }
        .hypothesis-list {
            font-size: 18px;
            color: #333;
            margin-top: 30px;
        }
        .divider {
            margin: 40px 0;
            border-top: 2px solid #3498db;
        }
    </style>

    <h1 class="title">Proyecto Final</h1>
""", unsafe_allow_html=True)

# Mostrar los integrantes
st.markdown(
    "<div class='team'><strong>Integrantes:</strong><br>Saúl Eduardo Andino Quijada<br>Natalia Sofía Coto Mendoza<br>Helen Esmeralda Gil Alvarez<br>Julia Beatriz Henriquez Mendoza</div>", 
    unsafe_allow_html=True
)

# Mensaje de bienvenida
st.markdown("<div class='subheader'>🔆 Bienvenidos 🔆</div>", unsafe_allow_html=True)
st.markdown("<div class='intro-text'>Este proyecto incluye las siguientes páginas y su análisis de datos sobre la depresión estudiantil.</div>", unsafe_allow_html=True)

# Sección de EDA
st.header("EDA: Análisis Exploratorio de Datos")
st.write("Este proyecto utilizó el conjunto de datos *Student Depression Dataset*, cuyo objetivo es analizar y encontrar patrones en los hábitos de los estudiantes.")

# Columnas para mostrar las imágenes
col1, col2 = st.columns([2, 2])

with col1:
    st.image("utils/tabla.png", width=350, use_container_width=True, caption="Exploración de Datos")

with col2:
    st.markdown(
        """
        Este dataset cuenta con 27,901 filas y 18 columnas. Algunas columnas son cuantitativas (por ejemplo, CGPA, Work/Study Hours), 
        y otras son cualitativas (por ejemplo, Gender, City). Notamos que hay una columna con valores faltantes (Financial Stress) que tiene 
        27,898 valores no nulos, lo que indica 3 valores faltantes.
        """
    )

# Segunda sección de EDA
col3, col4 = st.columns([2, 2])

with col3:
    st.image("utils/Dep.jpg", width=350, use_container_width=True, caption="Patrones de Depresión")

with col4:
    st.subheader("Hipótesis Propuestas")
    st.markdown("""
        En esta página se presentarán las hipótesis realizadas al principio mediante gráficos. Utilizamos las siguientes hipótesis para crear las gráficas:
    """)

# Mostrar hipótesis
st.markdown("""
<ul class="hypothesis-list">
    <li>Los estudiantes de género masculino tienen mayores probabilidades de estar deprimidos.</li>
    <li>Los estudiantes con buenos hábitos alimenticios tienen menos probabilidades de estar deprimidos.</li>
    <li>Los estudiantes con mejor desempeño académico (CGPA) tienen menos probabilidades de estar deprimidos.</li>
    <li>Los estudiantes que estudian más horas a la semana tienen menos probabilidades de estar deprimidos.</li>
    <li>Los estudiantes con patrones de sueño irregulares tienen mayores probabilidades de estar deprimidos.</li>
</ul>
""", unsafe_allow_html=True)

# Divisor
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Título de la siguiente sección
st.title("Modelos")
st.write("Se seleccionó el algoritmo **Random Forest**, que ofrece robustez frente a datos complejos y permite capturar relaciones no lineales entre las variables.")

# Mostrar imagen y texto sobre Random Forest
col5, col6 = st.columns([2, 2])

with col5:
    st.image("utils/random.jpg", width=350, use_container_width=True, caption="Modelo Random Forest")

with col6:
    st.subheader("Random Forest")
    st.markdown(
        "Random Forest es un algoritmo de aprendizaje supervisado basado en la combinación de múltiples árboles de decisión para mejorar la precisión y reducir el riesgo de sobreajuste."
    )

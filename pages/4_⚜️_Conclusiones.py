import streamlit as st

# Título de la sección
st.title("Conclusiones del Análisis")

st.write("""
El modelo tiene un desempeño sólido con una precisión general del **83.3%** y un F1-Score más alto para la clase "deprimido" (86%). Esto indica que el modelo es más eficiente en predecir correctamente a los estudiantes deprimidos, lo cual es positivo dado el contexto del análisis. Sin embargo, hay 773 falsos positivos, es decir, estudiantes clasificados como "Deprimidos" que en realidad no lo estaban y también hay 636 falsos negativos, que son estudiantes "Deprimidos" que el modelo no detectó.

Debido a los puntos débiles que presenta el modelo lo mejor sería mejorar su rendimiento para que devuelva mejores resultados que sean beneficiosos para los usuarios. Se debe considerar que, aunque la predicción de la depresión a través de modelos puede ser una herramienta valiosa, la intervención humana sigue siendo fundamental.
""")


st.subheader("Utilidad del modelo:")

# Añadir texto o conclusiones
st.write("""
Este modelo sería útil como herramienta de apoyo para instituciones educativas para monitorear la salud mental de los estudiantes, identificando a aquellos en riesgo y ofreciendo ayuda personalizada. Pero no debería ser la única base para tomar decisiones importantes. Podría emplearse como un primer filtro para identificar a estudiantes en riesgo y luego realizar una evaluación más detallada con otros métodos. Esto garantizaría una respuesta más precisa y adecuada a las necesidades de cada estudiante.
""")

st.subheader("Pasos para mejorar el rendimiento del modelo:")
st.write("""
**Aumentar la calidad y cantidad de datos:**

Si se recopilaran más datos y asegurar que las clases estén balanceadas (número similar de instancias para estudiantes deprimidos y no deprimidos). Incorporar más variables relevantes, como eventos recientes, situaciones familiares, entre otros factores que puedan influir en la salud mental.

**Usar menos variables redudantes:**

Se podría eliminar las que no parezcan relevantes (por ejemplo, variables redundantes o irrelevantes como nombres). A veces, usar menos variables ayuda al modelo a concentrarse en las más importantes.

**Evaluación en datos reales:**

Es importante probar el modelo en un entorno real con datos actualizados para validar su efectividad y utilidad práctica. Esto permitirá ajustar el modelo de acuerdo con su desempeño en situaciones reales y hacer ajustes a sus parámetros según sea necesario, lo que mejorará la fiabilidad y aplicabilidad del modelo en contextos reales.
""")

import streamlit as st
import pandas as pd
import base64
from PyPDF2 import PdfReader, PdfWriter

# Datos de ejemplo para la tabla
data = {
    'ID': [0, 1, 2],
    'Nombre': [
        'Poder General', 
        'pagare', 
        'escrito'
        ],
    'Ruta PDF': [
        'https://unionnegocios.com.py/sistema/content/csj/pdf/610892.pdf', 
        'https://unionnegocios.com.py/sistema/content/documentos/pdf/grupo1/931745.pdf', 
        'https://unionnegocios.com.py/sistema/escritos/preparacion_pdf/500'
        ]
}
df = pd.DataFrame(data)

# Función para cargar y mostrar el PDF
def mostrar_pdf(ruta_pdf):
    try:
        pdf_display = f'<iframe src="{ruta_pdf}#toolbar=1&navpanes=0&scrollbar=1" width="100%" height="600px"></iframe>'
        return pdf_display
    except FileNotFoundError:
        return "<p style='color: red;'>Archivo PDF no encontrado.</p>"

# Configuración de la interfaz en Streamlit
st.title("Vista con Tabla, Visualizador de PDF y Generador de Texto")

# Crear tres columnas
col1, col2, col3 = st.columns([3, 3, 1])

# Columna 1: Tabla
with col1:
    st.subheader("Tabla de Documentos")
    # Mostrar la tabla como interactiva
    selected_row = st.data_editor(
        df,
        use_container_width=True,
        column_config={
            "ID": "ID del Documento",
            "Nombre": "Nombre del Documento",
        },
        height=200,
        key="documentos_table"
    )
    # Obtener el ID seleccionado
    if selected_row is not None:
        selected_id = selected_row["ID"]

# Columna 2: Visualizador de PDF
with col2:
    st.subheader("Visualizador de PDF")
    pdf_ruta = df.loc[selected_id, 'Ruta PDF']
    st.markdown(mostrar_pdf(pdf_ruta), unsafe_allow_html=True)

# Columna 3: Botón para generar texto
with col3:
    st.subheader("Generador de Texto")
    if st.button("GENERAR"):
        st.write("Texto generado basado en los documentos seleccionados.")

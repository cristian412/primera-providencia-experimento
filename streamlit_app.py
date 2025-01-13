import streamlit as st
import pandas as pd
import base64
from PyPDF2 import PdfReader, PdfWriter

# Datos de ejemplo para la tabla
data = {
    'ID': [1, 2, 3, 4],
    'Nombre': [
        'Poder General', 
        'pagare', 
        'pagare solo',
        'escrito'
        ],
    'Ruta PDF': [
        'static/pdfs/poder_general_union.pdf', 
        'static/pdfs/pagare.pdf', 
        'static/pdfs/pagare-4.pdf',
        'static/pdfs/preparacion.pdf'
        ]
}
df = pd.DataFrame(data)



def convertir_pdf_a_estandar(ruta_origen, ruta_destino):
    try:
        reader = PdfReader(ruta_origen)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        with open(ruta_destino, "wb") as f:
            writer.write(f)
        return True
    except Exception as e:
        print(f"Error al convertir el PDF: {e}")
        return False




# Función para cargar y mostrar el PDF
def mostrar_pdf(ruta_pdf):
    # Convertir los PDFs problemáticos
    convertir_pdf_a_estandar(ruta_pdf, ruta_pdf+"-clean.pdf")
    try:
        with open(ruta_pdf+"-clean.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        url_extarnal = "https://unionnegocios.com.py/sistema/content/documentos/pdf/grupo1/931745.pdf#toolbar=0&navpanes=0&scrollbar=0"
        pdf_display = f'<iframe src="{url_extarnal}" width="100%" height="600px"></iframe>'
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
    selected_index = st.radio(
        "Selecciona un documento:",
        options=df.index,
        format_func=lambda x: f"{df.loc[x, 'Nombre']} (ID: {df.loc[x, 'ID']})",
        key="radio_selector"
    )

# Columna 2: Visualizador de PDF
with col2:
    st.subheader("Visualizador de PDF")
    pdf_ruta = df.loc[selected_index, 'Ruta PDF']
    st.markdown(mostrar_pdf(pdf_ruta), unsafe_allow_html=True)

# Columna 3: Botón para generar texto
with col3:
    st.subheader("Generador de Texto")
    if st.button("GENERAR"):
        st.write("Texto generado basado en los documentos seleccionados.")

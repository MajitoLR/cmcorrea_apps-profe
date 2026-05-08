import streamlit as st
from PIL import Image

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    layout="wide",
    page_icon="💗"
)

# ===== ESTILOS PERSONALIZADOS =====
st.markdown("""
<style>

.main {
    background: linear-gradient(to bottom, #fff7fb, #ffeef7);
}

h1 {
    color: #d63384;
    text-align: center;
    font-size: 50px !important;
    margin-bottom: 10px;
    font-weight: 800;
}

h2, h3 {
    color: #c2185b;
}

section[data-testid="stSidebar"] {
    background-color: #ffd9ec;
}

.stButton>button {
    background-color: #ff69b4;
    color: white;
    border-radius: 15px;
    border: none;
    padding: 0.5rem 1rem;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 25px;
    box-shadow: 0px 4px 15px rgba(255, 105, 180, 0.15);
    margin-bottom: 25px;
    transition: 0.3s;
    border: 2px solid #ffe0ef;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 8px 25px rgba(255, 105, 180, 0.25);
}

.card-text {
    color: #5e5e5e;
    font-size: 15px;
}

.link-style a {
    color: #d63384 !important;
    font-weight: bold;
    text-decoration: none;
}

.link-style a:hover {
    color: #ff1493 !important;
    text-decoration: underline;
}

img {
    border-radius: 18px;
}

</style>
""", unsafe_allow_html=True)

# ===== TITULO =====
st.title("Aplicaciones de Inteligencia Artificial.")

# ===== SIDEBAR =====
with st.sidebar:
    st.subheader("💗 Aplicaciones con Inteligencia Artificial")

    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )

    st.write(parrafo)

# ===== ENLACE PRINCIPAL =====
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown("""
<div class="card">
<h3>🌸 Recursos y ejercicios prácticos</h3>
<p class="card-text">
Explora materiales interactivos, ejemplos y aplicaciones de inteligencia artificial.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<div class="link-style">💗 <a href="{url_ia}" target="_blank">Ir al sitio principal</a></div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ===== COLUMNAS =====
col1, col2, col3 = st.columns(3)

# =========================================
# COLUMNA 1
# =========================================
with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Detector de Gestos")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=220)
    st.write("Explora una aplicación interactiva capaz de detectar y reconocer gestos en tiempo real.")
    url = "https://detecciondegestosprofe-w3acjxoexzrkszjfdbrpxx.streamlit.app/"
    st.markdown(f'<div class="link-style"><a href="{url}">Abrir aplicación</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Audio Libro Para Niños")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=220)
    st.write("Descubre una experiencia interactiva que combina imágenes, voz y reconocimiento de objetos.")
    url = "https://interfazmultimodalprofemj.streamlit.app/"
    st.markdown(f'<div class="link-style"><a href="{url}">Abrir aplicación</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Mi Primera App")
    image = Image.open('OIG5.jpg')
    st.image(image, width=220)
    st.write("Aprende cómo utilizar modelos entrenados dentro de una aplicación sencilla e intuitiva.")
    url = "https://introduccionmajo.streamlit.app/"
    st.markdown(f'<div class="link-style"><a href="{url}">Abrir aplicación</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# COLUMNA 2
# =========================================
with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Mi Primera App Introducción 2")
    image = Image.open('OIG8.jpg')
    st.image(image, width=220)
    st.write("Conoce una aplicación enfocada en la conversión de voz a texto mediante IA.")
    url = "https://introcopiaprofemj.streamlit.app/"
    st.markdown(f'<div class="link-style"><a href="{url}">Abrir aplicación</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Reconocimiento Optico De Carácteres Imagen")
    image = Image.open('data_analisis.png')
    st.image(image, width=220)
    st.write("Experimenta herramientas de análisis de datos y reconocimiento inteligente.")
    url = "https://audioimagenprofe.streamlit.app/"
    st.markdown(f'<div class="link-style"><a href="{url}">Abrir aplicación</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Reconocimiento Optico de Carácteres Tomar Foto")
    image = Image.open('OIG3.jpg')
    st.image(image, width=220)
    st.write("Convierte imágenes capturadas en texto mediante reconocimiento óptico avanzado.")
    url = "https://imagentextoprofe.streamlit.app/"
    st.markdown(f'<div class="link-style"><a href="{url}">Abrir aplicación</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# COLUMNA 3
# =========================================
with col3:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Análisis de Sentimiento")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=220)
    st.write("Analiza emociones y opiniones en textos utilizando inteligencia artificial.")
    url = "https://sentimientoprofemjl.streamlit.app/"
    st.markdown(f'<div class="link-style"><a href="{url}">Abrir aplicación</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Demo TF-IDF en Español")
    image = Image.open('OIG4.jpg')
    st.image(image, width=220)
    st.write("Visualiza cómo funciona el análisis de palabras y relevancia en español.")
    url = "https://tdf-idef-esp-profemjl.streamlit.app/"
    st.markdown(f'<div class="link-style"><a href="{url}">Abrir aplicación</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Demo de TF-IDF con Preguntas y Respuestas")
    image = Image.open('OIG6.jpg')
    st.image(image, width=220)
    st.write("Interactúa con preguntas inteligentes usando técnicas de procesamiento de lenguaje.")
    url = "https://tf-idfprofemjl.streamlit.app/"
    st.markdown(f'<div class="link-style"><a href="{url}">Abrir aplicación</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

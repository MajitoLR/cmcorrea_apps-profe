import streamlit as st
from PIL import Image

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================

st.set_page_config(
    page_title="Portafolio de María José",
    page_icon="🎀",
    layout="wide"
)

# =========================================================
# ESTILOS GIRLY / ROSA PASTEL
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(to bottom, #fff0f6, #ffe8f3, #fff7fb);
}

/* HEADER */

.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: 700;
    color: #ff4fa3;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #8d5c74;
    font-size: 18px;
    margin-bottom: 35px;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #ffd8ea, #ffeaf4);
    border-right: 2px solid #ffc2de;
}

.sidebar-text {
    color: #6f4b5f;
    font-size: 15px;
}

/* CARDS */

.card {
    background: rgba(255,255,255,0.72);
    backdrop-filter: blur(10px);
    border-radius: 28px;
    padding: 22px;
    margin-bottom: 28px;
    box-shadow: 0 8px 20px rgba(255, 105, 180, 0.18);
    border: 2px solid rgba(255,255,255,0.7);
    transition: 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 25px rgba(255, 105, 180, 0.25);
}

/* TITULOS */

h3 {
    color: #ff4fa3 !important;
    font-weight: 600 !important;
}

/* TEXTO */

.card-text {
    color: #6f5d66;
    font-size: 15px;
}

/* LINKS */

.link-style a {
    display: inline-block;
    background: linear-gradient(to right, #ff8fc7, #ff5ca8);
    color: white !important;
    text-decoration: none;
    padding: 10px 18px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 500;
    margin-top: 8px;
    transition: 0.3s ease;
}

.link-style a:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 15px rgba(255, 105, 180, 0.3);
}

/* IMÁGENES */

img {
    border-radius: 20px;
}

/* SEPARADOR */

.divider {
    height: 2px;
    background: linear-gradient(to right, transparent, #ff99c8, transparent);
    margin-top: 10px;
    margin-bottom: 40px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER PRINCIPAL
# =========================================================

st.markdown("""
<div class="main-title">
🎀 Portafolio de María José
</div>

<div class="subtitle">
Explora mis proyectos y aplicaciones desarrolladas en clase.
</div>

<div class="divider"></div>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.subheader("💗 Portafolio Maria José Larrea")

    parrafo = (
        "Aquí encontrarás los trabajos realizados en clase "
        "y todos los ejercios enseñados por el profesor a través de cada link."
    )

    st.markdown(f'<div class="sidebar-text">{parrafo}</div>', unsafe_allow_html=True)

# =========================================================
# ENLACE PRINCIPAL
# =========================================================

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown("""
<div class="card">
<h3>🌸 Recursos y ejercicios prácticos</h3>

<p class="card-text">
Aquí puedes encontrar páginas, actividades y ejercicios.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<div class="link-style"><a href="{url_ia}" target="_blank">✨ Ir al sitio principal</a></div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# COLUMNAS
# =========================================================

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7, _, _ = st.columns(3)

# =========================================================
# FUNCIÓN PARA LAS CARDS
# =========================================================

def crear_card(titulo, imagen, descripcion, url, emoji="💗"):

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader(titulo)

    image = Image.open(imagen)
    st.image(image, use_container_width=True)

    st.write(descripcion)

    st.markdown(
        f'<div class="link-style"><a href="{url}" target="_blank">{emoji} Ver proyecto</a></div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# COLUMNA 1
# =========================================================

with col1:

    crear_card(
        "Detector de Gestos",
        "detector_gestos.png",
        "Aplicación interactiva enfocada en la detección y reconocimiento de gestos mediante inteligencia artificial.",
        "https://detecciondegestosprofe-w3acjxoexzrkszjfdbrpxx.streamlit.app/"
    )

    crear_card(
        "Audio Libro Para Niños",
        "Audio_libro.png",
        "Experiencia multimedia diseñada para niños con interacción de audio e imágenes inteligentes.",
        "https://interfazmultimodalprofemj.streamlit.app/",
        "🌸"
    )

    crear_card(
        "Mi Primera App",
        "mi_primera_app.png",
        "Introducción práctica al uso de modelos entrenados y aplicaciones inteligentes.",
        "https://introduccionmajo.streamlit.app/",
        "🎀"
    )

# =========================================================
# COLUMNA 2
# =========================================================

with col2:

    crear_card(
        "Mi Primera App Introducción 2",
        "mi_primera_app_intro2.png",
        "Aplicación enfocada en la conversión de voz a texto utilizando inteligencia artificial.",
        "https://introcopiaprofemj.streamlit.app/"
    )

    crear_card(
        "Reconocimiento Optico De Carácteres Imagen",
        "reconocimiento_optico_imag.png",
        "Herramienta orientada al reconocimiento inteligente de texto y análisis automatizado.",
        "https://audioimagenprofe.streamlit.app/",
        "✨"
    )

    crear_card(
        "Reconocimiento Optico de Carácteres Tomar Foto",
        "reconocimiento_optico_foto.png",
        "Convierte imágenes capturadas en texto mediante reconocimiento óptico avanzado.",
        "https://imagentextoprofe.streamlit.app/",
        "🌷"
    )

# =========================================================
# COLUMNA 3
# =========================================================

with col3:

    crear_card(
        "Análisis de Sentimiento",
        "analisis_sentimiento.png",
        "Analiza emociones y opiniones en textos utilizando técnicas de inteligencia artificial.",
        "https://sentimientoprofemjl.streamlit.app/"
    )

    crear_card(
        "Demo TF-IDF en Español",
        "OIG4.jpg",
        "Explora el análisis de palabras y relevancia utilizando TF-IDF en español.",
        "https://tdf-idef-esp-profemjl.streamlit.app/",
        "🌸"
    )

    crear_card(
        "Demo de TF-IDF con Preguntas y Respuestas",
        "preguntas_respuestas.png",
        "Sistema interactivo de preguntas y respuestas basado en procesamiento de lenguaje natural.",
        "https://tf-idfprofemjl.streamlit.app/",
        "🎀"
    )

# =========================================================
# COLUMNA 4
# =========================================================

with col4:

    crear_card(
        "Traductor",
        "Chat_pdf.png",
        "Aplicación inteligente orientada a la traducción automática de texto.",
        "https://traductormjl.streamlit.app/"
    )

    crear_card(
        "WordCloud Studio",
        "OIG4.jpg",
        "Genera visualizaciones dinámicas de palabras mediante inteligencia artificial.",
        "https://wordcloudprofemjl.streamlit.app/",
        "🌸"
    )

    crear_card(
        "Detección de Objetos en Imágenes Yolov",
        "OIG6.jpg",
        "Detección de objetos en imágenes utilizando modelos YOLO y visión computacional.",
        "https://yolov5profemjl.streamlit.app/",
        "🎀"
    )

# =========================================================
# COLUMNA 5
# =========================================================

with col5:

    crear_card(
        "Análisis PDF",
        "Chat_pdf.png",
        "Interactúa con documentos PDF utilizando técnicas RAG e inteligencia artificial.",
        "https://chatpdf-profe-8kwrnfv9jyh96k6eszqybq.streamlit.app/"
    )

    crear_card(
        "Control Inteligente por voz",
        "OIG4.jpg",
        "Sistema interactivo de control mediante comandos de voz inteligentes.",
        "https://ctrlvoice-profe-mjl.streamlit.app/",
        "🌸"
    )

    crear_card(
        "Lienzo Inteligente",
        "OIG6.jpg",
        "Herramienta creativa e interactiva con reconocimiento inteligente de dibujos.",
        "https://drawrecog-profe-mjl.streamlit.app/",
        "🎀"
    )

# =========================================================
# COLUMNA 6
# =========================================================

with col6:

    crear_card(
        "Reconocimiento Digitos Escritos A Mano",
        "Chat_pdf.png",
        "Reconocimiento inteligente de dígitos escritos a mano utilizando IA.",
        "https://handw-profe-mjl.streamlit.app/"
    )

    crear_card(
        "Trazos Con Emoción",
        "OIG4.jpg",
        "Aplicación interactiva que interpreta emociones mediante trazos y dibujo.",
        "https://histinf-mjl-emotion.streamlit.app/",
        "🌸"
    )

    crear_card(
        "Lector de Sensor MQTT",
        "OIG6.jpg",
        "Visualización y lectura de sensores conectados mediante MQTT.",
        "https://recepmqtt-profe-mjl.streamlit.app/",
        "🎀"
    )

# =========================================================
# COLUMNA 7
# =========================================================

with col7:

    crear_card(
        "Control MQTT Inteligente",
        "Chat_pdf.png",
        "Control inteligente de dispositivos y sensores utilizando MQTT.",
        "https://sendcmqtt-profe-mjl.streamlit.app/"
    )

    crear_card(
        "Lienzo de Inspiración",
        "Chat_pdf.png",
        "Espacio creativo e interactivo para organizar ideas e inspiración visual.",
        "https://tableroprop2mjl-class.streamlit.app/",
        "🌸"
    )

    crear_card(
        "Análisis de imagen",
        "Chat_pdf.png",
        "Herramienta de análisis inteligente de imágenes mediante visión computacional.",
        "https://visionapp-profe-mjl.streamlit.app/",
        "🎀"
    )

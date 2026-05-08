import streamlit as st
from PIL import Image

# =========================================
# CONFIGURACIÓN DE PÁGINA
# =========================================
st.set_page_config(
    page_title="Portafolio de María José",
    page_icon="🎀",
    layout="wide"
)

# =========================================
# ESTILOS GIRLY
# =========================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(to bottom, #fff0f6, #ffe4ef, #fff7fb);
}

/* TITULO PRINCIPAL */
.main-title {
    text-align: center;
    font-size: 60px;
    color: #ff4fa3;
    font-weight: 700;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    color: #8b5d74;
    font-size: 18px;
    margin-bottom: 40px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #ffd6ea, #ffeaf4);
    border-right: 2px solid #ffc2de;
}

.sidebar-text {
    color: #7a4762;
    font-size: 15px;
}

/* TARJETAS */
.card {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(10px);
    border-radius: 30px;
    padding: 25px;
    margin-bottom: 28px;
    box-shadow: 0 8px 20px rgba(255, 105, 180, 0.15);
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
    color: #6d5c66;
    font-size: 15px;
}

/* LINKS */
.link-style a {
    display: inline-block;
    margin-top: 8px;
    background: linear-gradient(to right, #ff8fc7, #ff5ca8);
    color: white !important;
    text-decoration: none;
    padding: 10px 18px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 500;
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
    background: linear-gradient(to right, transparent, #ff8fc7, transparent);
    margin-top: 10px;
    margin-bottom: 35px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================
st.markdown("""
<div class="main-title">
🎀 Portafolio de María José
</div>

<div class="subtitle">
Explora mis proyectos y aplicaciones desarrolladas con Inteligencia Artificial, 
visión computacional, procesamiento de lenguaje natural y experiencias interactivas.
</div>

<div class="divider"></div>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================
with st.sidebar:

    st.markdown("## 💗 Sobre este portafolio")

    st.markdown("""
    <div class="sidebar-text">
    Este espacio reúne diferentes proyectos y aplicaciones creadas con herramientas de Inteligencia Artificial.  
    Aquí podrás encontrar experiencias interactivas relacionadas con:
    
    ✨ Visión computacional  
    ✨ Reconocimiento de voz  
    ✨ Procesamiento de texto  
    ✨ Análisis de datos  
    ✨ Modelos inteligentes  
    ✨ Aplicaciones multimodales  
    </div>
    """, unsafe_allow_html=True)

# =========================================
# ENLACE PRINCIPAL
# =========================================
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown("""
<div class="card">
<h3>🌸 Recursos y ejercicios prácticos</h3>

<p class="card-text">
Aquí encontrarás materiales complementarios, actividades y ejercicios relacionados con Inteligencia Artificial.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<div class="link-style"><a href="{url_ia}" target="_blank">✨ Ir al sitio principal</a></div>',
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# COLUMNAS
# =========================================
col1, col2, col3 = st.columns(3)

# =========================================
# COLUMNA 1
# =========================================
with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Detector de Gestos")
    image = Image.open('txt_to_audio2.png')
    st.image(image, use_container_width=True)

    st.write("Aplicación interactiva enfocada en la detección y reconocimiento de gestos mediante inteligencia artificial.")

    url = "https://detecciondegestosprofe-w3acjxoexzrkszjfdbrpxx.streamlit.app/"

    st.markdown(
        f'<div class="link-style"><a href="{url}">💗 Ver proyecto</a></div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Audio Libro Para Niños")
    image = Image.open('txt_to_audio.png')
    st.image(image, use_container_width=True)

    st.write("Experiencia interactiva orientada a la narración y exploración multimedia para niños.")

    url = "https://interfazmultimodalprofemj.streamlit.app/"

    st.markdown(
        f'<div class="link-style"><a href="{url}">🌸 Ver proyecto</a></div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Mi Primera App")
    image = Image.open('OIG5.jpg')
    st.image(image, use_container_width=True)

    st.write("Introducción práctica al uso de modelos inteligentes dentro de aplicaciones web.")

    url = "https://introduccionmajo.streamlit.app/"

    st.markdown(
        f'<div class="link-style"><a href="{url}">🎀 Ver proyecto</a></div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================
# COLUMNA 2
# =========================================
with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Mi Primera App Introducción 2")
    image = Image.open('OIG8.jpg')
    st.image(image, use_container_width=True)

    st.write("Aplicación enfocada en conversión de voz a texto utilizando inteligencia artificial.")

    url = "https://introcopiaprofemj.streamlit.app/"

    st.markdown(
        f'<div class="link-style"><a href="{url}">💖 Ver proyecto</a></div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Reconocimiento Optico De Carácteres Imagen")
    image = Image.open('data_analisis.png')
    st.image(image, use_container_width=True)

    st.write("Proyecto orientado al reconocimiento inteligente y análisis automatizado de información.")

    url = "https://audioimagenprofe.streamlit.app/"

    st.markdown(
        f'<div class="link-style"><a href="{url}">✨ Ver proyecto</a></div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # --------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Reconocimiento Optico de Carácteres Tomar Foto")
    image = Image.open('OIG3.jpg')
    st.image(image, use_container_width=True)

    st.write("Convierte imágenes capturadas en texto mediante reconocimiento óptico avanzado.")

    url = "https://imagentextoprofe.streamlit.app/"

    st.markdown(
        f'<div class="link-style"><a href="{url}">🌷 Ver proyecto</a></div>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

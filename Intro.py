import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Detector de Gestos")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones para detectar gestos") 
 url = "•	https://detecciondegestosprofe-w3acjxoexzrkszjfdbrpxx.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Audio Libro Para Niños")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://interfazmultimodalprofemj.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Mi Primera App")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://introduccionmajo.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Mi Primera App Introducción 2")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "•	https://introcopiaprofemj.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Reconocimiento Optico De Carácteres Imagen")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://audioimagenprofe.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Reconocimiento Optico de Carácteres Tomar Foto")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://imagentextoprofe.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Análisis de Sentimiento")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://sentimientoprofemjl.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Demo TF-IDF en Español")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://tdf-idef-esp-profemjl.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Demo de TF-IDF con Preguntas y Respuestas")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://tf-idfprofemjl.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

with col4:
 st.subheader("Traductor")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://traductormjl.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("WordCloud Studio")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://wordcloudprofemjl.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Detección de Objetos en Imágenes Yolov")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://yolov5profemjl.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

with col5:
 st.subheader("Análisis PDF")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-profe-8kwrnfv9jyh96k6eszqybq.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Control Inteligente por voz")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://ctrlvoice-profe-mjl.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Lienzo Inteligente")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://drawrecog-profe-mjl.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

with col6:
 st.subheader("Reconocimiento Digitos Escritos A Mano")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://handw-profe-mjl.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Trazos Con Emoción")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://histinf-mjl-emotion.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Lector de Sensor MQTT")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://recepmqtt-profe-mjl.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

with col7:
 st.subheader("Control MQTT Inteligente")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://sendcmqtt-profe-mjl.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")
  
 st.subheader("Lienzo de Inspiración")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://tableroprop2mjl-class.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de imagen")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://visionapp-profe-mjl.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

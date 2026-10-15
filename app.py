import streamlit as st
import requests

# Configuración de la página para móvil
st.set_page_config(page_title="Mi Estudio Seedance", page_icon="🎬", layout="centered")

st.title("🎬 Mi Estudio Privado de Video IA")
st.write("Genera videos personalizados utilizando el motor de video conectado.")

# 1. Caja de texto para el prompt
prompt = st.text_area(
    "Describe tu escena, personaje o acción:",
    placeholder="Ej: Animación 3D estilo cinemático, plano medio de un personaje...",
)

# 2. Opciones de configuración del video
col1, col2 = st.columns(2)
with col1:
    aspect_ratio = st.selectbox("Formato", ["9:16 (Vertical)", "16:9 (Horizontal)", "1:1 (Cuadrado)"])
with col2:
    duration = st.slider("Duración (segundos)", 2, 10, 5)

# 3. Subir imagen de referencia (Opcional para consistencia)
uploaded_file = st.file_uploader("Sube una imagen de referencia (Opcional)", type=["jpg", "png", "jpeg"])

# 4. Botón de Generación
if st.button("🚀 Generar Video"):
    if prompt:
        with st.spinner("Conectando con el motor de video en PiAPI... Esto puede tomar unos momentos."):
            try:
                # Obtener la llave secreta configurada en Streamlit
                api_key = st.secrets["PIAPI_API_KEY"]
                
                # Configuración de la petición a la API de PiAPI con autenticación corregida
                url = "https://api.piapi.ai/api/v1/task"
                headers = {
                    "x-api-key": api_key,
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "seedance-2.0",
                    "task_type": "text-to-video",
                    "input": {
                        "prompt": prompt,
                        "aspect_ratio": aspect_ratio,
                        "duration": duration
                    }
                }
                
                response = requests.post(url, json=payload, headers=headers)
                
                if response.status_code == 200 or response.status_code == 201:
                    st.success("¡Petición enviada con éxito al motor de video! Tu tarea está siendo procesada en la nube.")
                    st.json(response.json())
                else:
                    st.error(f"Hubo un error al conectar con la API (Código {response.status_code}): {response.text}")
                    
            except Exception as e:
                st.error(f"Error de configuración: Asegúrate de haber agregado 'PIAPI_API_KEY' en los Secrets de Streamlit. Detalles: {e}")
    else:
        st.warning("Por favor escribe una descripción para el video.")

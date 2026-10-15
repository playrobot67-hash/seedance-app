import streamlit as st

# Configuración de la página para móvil
st.set_page_config(page_title="Mi Estudio Seedance", page_icon="🎬", layout="centered")

st.title("🎬 Mi Estudio Privado de Video IA")
st.write("Genera videos personalizados sin límites de uso.")

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
        with st.spinner("Conectando con el motor de video... Esto puede tomar unos momentos."):
            
            # --- AQUÍ IRÁ LA CONEXIÓN CON TU API DE SEEDANCE ---
            # headers = {"Authorization": "Bearer TU_API_KEY"}
            # payload = {"prompt": prompt, "aspect_ratio": aspect_ratio, "duration": duration}
            # response = requests.post("URL_DE_LA_API", json=payload, headers=headers)
            
            # Simulación de éxito
            st.success("¡Petición enviada con éxito a tu motor de video!")
            st.info("Nota: Recuerda configurar tus llaves de API (API Keys) en el código o en los secretos de Streamlit para procesar videos reales.")
            
    else:
        st.warning("Por favor escribe una descripción para el video.")


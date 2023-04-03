import streamlit as st
from PIL import Image

st.title("Color to Grayscale Converter")


upload_image = st.file_uploader("Upload image")
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_image = img.convert("L")
    st.image(gray_image)

if upload_image:
    img = Image.open(upload_image)
    gray_image = img.convert("L")
    st.image(gray_image)
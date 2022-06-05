import streamlit as st
import time
from PIL import Image

style_name = {
    'default': 'Default',
    'dark': 'Dark',
}

# title and instruction
st.title("Apply style transfer to your images")
st.markdown("""
    Upload your image and select the style you want to apply.
    """)

# interactive components
image_box = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
style_box = st.selectbox("Choose the style you want to apply", list(style_name.keys()))
apply_button = st.button("Apply style transfer")

# processing
if apply_button:
    if image_box is not None and style_box is not None:
        st.text("Applying style transfer...")
        st.text("Please wait...")

        # load and process image

        # send request to backend

        # show result



        st.success("Done!")

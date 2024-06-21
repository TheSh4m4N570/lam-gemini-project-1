# importing
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# create a function to load gemini pro vision model
model = genai.GenerativeModel(model_name='gemini-pro-vision')


def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini Image Demo")
input = st.text_input("Input prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image", use_column_width=True)


submit = st.button("Tell me about the image")

# If submit is clicked
if submit is True:
    response = get_gemini_response(input, image)
    st.write(response)
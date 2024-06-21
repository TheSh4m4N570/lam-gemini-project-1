# importing
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# create a function to load gemini pro model
model = genai.GenerativeModel(model_name='gemini-pro')


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# Set up the streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# When submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is: ")
    st.write(response)
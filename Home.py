import streamlit as st
import openai
import os


openai.api_key =  os.getenv("APIKEY")
# openai.api_key = "YOUR_API_KEY"

st.title("QuickBOM.ai")

prompt = st.text_input("Enter a prompt:")
if prompt:
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    text = response.choices[0].text
    st.write(text)

import streamlit as st
import openai
import os

openai.api_key = "YOUR_API_KEY"

st.title("GPT-3 Text Generation")

prompt = st.text_input("Enter a prompt:")
if prompt:
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    text = response.choices[0].text
    st.write(text)

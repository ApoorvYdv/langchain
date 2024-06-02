import requests
import streamlit as st


def get_essay(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}}
    )

    return response.json()["output"]


text_input = st.text_input("Write an essay on")

if text_input:
    st.write(get_essay(text_input))

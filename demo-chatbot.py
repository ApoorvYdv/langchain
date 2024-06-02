import google.generativeai as genai
from langchain_community.llms import Ollama

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")
# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework

st.title("Langchain Demo with OPEN AI")
input_text = st.text_input("Search the topic u want")

## Google Gemini LLM
# llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.3)

## Ollama llama3
llm = Ollama(model="llama3")

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text: 
    st.write(chain.invoke({"question": input_text}))
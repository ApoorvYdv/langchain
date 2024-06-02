import os

import google.generativeai as genai
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI(
    title="Langchain Server", version="1.0", description="A simple API server"
)

# add_routes(
#     app,
#     Gemini(),
#     path="/gemini"
# )

llm = Ollama(model="llama3")

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)

add_routes(app, prompt1 | llm, path="/essay")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

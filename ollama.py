# Importing necessary libraries

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

api_key = st.secrets["LANGCHAIN_API_KEY"]

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = api_key

#Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

#Streamlit Framework

st.set_page_config(page_title="Ollama Demo")
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Search about the topic")

#Ollama LLAma2 LLM
 
llm = Ollama(model = "llama2-uncensored")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
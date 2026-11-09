from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

st.header("Reasearch Tool")

user_input = st.text_input("Enter your research query here:")


if st.button("Generate Research Summary"):
    result = ChatGoogleGenerativeAI(model="gemini-2.5-flash").invoke(user_input)
    st.write(result)
import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("⚠️ Please set your GROQ_API_KEY in a .env file")
    st.stop()

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are a helpful assistant. "
         "Answer questions clearly and concisely."),
        ("user", "Question: {question}")
    ]
)

# Output parser
output_parser = StrOutputParser()

def generate_response(question, engine="llama-3.1-8b-instant"):
    llm = ChatGroq(
        model=engine,
        groq_api_key=groq_api_key,
    )
    chain = prompt | llm | output_parser
    return chain.invoke({'question': question})

# ---------------------------
# Streamlit Interface
# ---------------------------
st.title("🤖 AI Q&A Bot (Groq API)")
st.write("Ask me anything and I’ll try to answer clearly and concisely.")

# Sidebar
st.sidebar.title("Settings")
engine = st.sidebar.selectbox(
    "Select Model",
    ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"]
)

# Main input
user_input = st.text_input("Your Question:")

if user_input:
    try:
        response = generate_response(user_input, engine)
        st.success("**Bot:** " + response)
    except Exception as e:
        st.error(f"Error: {e}")

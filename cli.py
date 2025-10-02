
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    print("⚠️ Please set your GROQ_API_KEY environment variable first.")
    exit()

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer clearly."),
    ("user", "Question: {question}")
])

output_parser = StrOutputParser()

def generate_response(question, engine="llama-3.1-8b-instant"):
    llm = ChatGroq(model=engine, groq_api_key=groq_api_key)
    chain = prompt | llm | output_parser
    return chain.invoke({'question': question})

print("=== AI Q&A Bot (Groq API) ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye 👋")
        break
    try:
        print("Bot:", generate_response(user_input), "\n")
    except Exception as e:
        print("Error:", e)

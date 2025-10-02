# AI Q&A Bot (Groq API)

A simple AI-powered command-line chatbot built using the Groq API. Users can type a question, and the bot provides clear, concise answers.

This project was completed as part of an internship assignment to showcase effort, creativity, and ability to use AI APIs.

🔹 Features

Ask any question and get answers using Groq LLM.

Minimal command-line interface.

Optional Streamlit UI for web-based interaction.

Model selection support (e.g., llama-3.1-8b-instant, llama-3.3-70b-versatile).

Handles multiple queries in a single session.

🔹 Setup Instructions
1. Clone the repository
 ```
git clone https://github.com/your-username/ai-qna-bot.git
cd ai-qna-bot
```
3. Install Python dependencies
```
pip install langchain langchain-groq python-dotenv
```
5. Add your Groq API Key

Create a .env file in the project root:
```
GROQ_API_KEY=your_api_key_here
```
4. Run the Command-Line Bot
```
python qna_bot.py
```
6. (Optional) Run Streamlit UI
```
streamlit run qna_streamlit.py
```
🔹 Usage

Command-Line Interface Example:
```
=== AI Q&A Bot (Groq API) ===
Type 'exit' to quit.

You: What is phishing?
Bot: Phishing is a type of cyber attack where attackers trick users into revealing sensitive information...
```

Streamlit UI Example:
```
Enter your question in the text box and click Ask.

Bot response appears below.
```
🔹 Challenges / Errors Faced

Error: ImportError: No module named 'langchain_groq'
Fix: Installed missing dependency: pip install langchain-groq.

Error: API key not found
Fix: Added .env file with GROQ_API_KEY and loaded it using dotenv.

Error: Model invocation timeout
Fix: Switched to smaller model (llama-3.1-8b-instant) for faster responses.

🔹 Stretch Goals Implemented

Streamlit UI for a simple web interface.

Model selection via sidebar.

Clean display of bot responses.

Potential deployment to Hugging Face Spaces / Render.

🔹 Notes

This project is intended to demonstrate AI API integration, problem-solving, and creative implementation.

No prior coding experience is required; effort and documentation are key.

🔹 Future Improvements

Add conversation memory to see past Q&A pairs.

Integrate custom knowledge base for domain-specific Q&A.

Deploy as a fully interactive web app with persistent chat history.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ac79f7d2-edba-466d-a921-f3dc5a37d56b" />

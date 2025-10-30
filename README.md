# LangChain-Chatbot-using-Groq-LLM
🧬 LangChain Chatbot using Groq LLM

This project is a simple AI chatbot built using LangChain and Groq’s Llama 3.3 70B model.
It demonstrates how to integrate an LLM into a conversational app using prompt templates, parsing, and environment management.

🚀 Project Overview

The chatbot:

Accepts user input in a conversational loop.

Uses ChatPromptTemplate from LangChain to dynamically construct prompts.

Connects to Groq’s Llama 3.3-70B model for generating intelligent, context-aware responses.

Uses StrOutputParser to parse the output into readable text.

Supports chat history — maintaining context between turns.

Runs fully in your terminal.

🧰 Tech Stack   
Component           	       Purpose
Python                      Core programming language
LangChain	                  Framework for building LLM workflows
Groq LLM (Llama 3.3 70B)	   Language model for intelligent responses
dotenv	                     Load environment variables securely
Git & GitHub	               Version control and project hosting

🧩 Project Structure
Langchain_chatbot/
- chatbot.py              Main chatbot logic
- requirements.txt        Dependencies
- .env                    API key (not uploaded to GitHub)
- .gitignore              Files to be ignored by Git
-  README.md              Project documentation
-  venv/                  Virtual environment (ignored)

⚙️ Setup Instructions

1️⃣ Clone the repository
git clone https://github.com/<yourusername>/Langchain_chatbot.git
cd Langchain_chatbot

2️⃣ Create a virtual environment
python -m venv .venv
source .venv/Scripts/activate   # for Windows PowerShell

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add your API key
Create a .env file and paste:
GROQ_API_KEY=your_api_key_here

5️⃣ Run the chatbot
python chatbot.py

🧠 What I Learned from This Project

Through this project, I gained hands-on understanding of AI pipeline fundamentals and how modern LLM frameworks operate.
Key takeaways:

🧩 1. LangChain Framework

How prompt templates dynamically control LLM behavior.

The idea of a prompt → model → parser chain.

Using ChatPromptTemplate to maintain structured multi-turn conversations.

⚙️ 2. Large Language Models (LLMs)

Understanding how LLMs (like Llama 3.3 70B) generate context-aware responses.

How temperature affects creativity vs. accuracy in responses.

🔐 3. Environment & API Management

How to use .env and dotenv to securely manage API keys.

How to use .gitignore to protect sensitive information.

🧠 4. Data Engineering & AI Integration Concepts

Basics of connecting Python pipelines to LLMs using APIs.

How prompt chaining resembles data pipelines in AI/ML workflows.

Insight into building modular and reusable components for GenAI systems.

🌐 5. Git & Version Control

Initializing repositories, staging, committing, pushing.

Understanding how local and remote repos sync.

Maintaining a professional project structure on GitHub.

💡 Future Enhancements

Add a Streamlit UI for an interactive chat interface.

Integrate RAG (Retrieval-Augmented Generation) for domain-specific knowledge.

Store chat history using ChromaDB or FAISS for memory.

Deploy on Streamlit Cloud or AWS Lambda.


🧬 Author
👩‍💻 Sanjana Ghosh
Bioinformatics & AI Enthusiast | Exploring GenAI in Healthcare
🌐 LinkedIn
 • GitHub

📜 License
This project is open-source and available under the MIT License.

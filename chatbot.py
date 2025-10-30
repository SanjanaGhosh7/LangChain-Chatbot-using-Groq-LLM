# Building a Chatbot with LangChain

# Install dependencies:
# pip install -r requirements.txt

import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Load the environment variables (Groq API key should be in .env)
load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
)

# Initialize the parser
parser = StrOutputParser()

def chat():
    chat_history = [
        ("system", "You are a helpful chatbot. Be concise and accurate.")
    ]
    print("Welcome to LangChain Chatbot. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break

        # Add user message
        chat_history.append(("user", user_input))

        # Build prompt dynamically
        prompt = ChatPromptTemplate.from_messages(chat_history)

        # Build the chain
        chain = prompt | llm | parser

        # Get response
        response = chain.invoke({})

        # Display response
        print(f"Bot: {response}\n")

        # Save assistant response
        chat_history.append(("assistant", response))

        print("-" * 50)

# Run chatbot
chat()

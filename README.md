# 🤖 AI Chatbot

## 📌 Project Overview

This project is an AI chatbot developed as a practical Generative AI internship project.

The chatbot uses the Hugging Face Inference API to generate AI-based responses and maintains conversation context during the current session.

## ✨ Features

- AI-powered chatbot
- Real AI API integration
- User-friendly Streamlit interface
- Conversation history
- Context-aware responses
- Prompt design
- Clear Chat option
- Natural language interaction

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Inference API
- Hugging Face InferenceClient
- Generative AI
- Prompt Engineering

## 🧠 Prompt Design

The chatbot uses a system prompt to guide the AI assistant.

The prompt instructs the chatbot to:

- Provide clear and simple answers
- Give accurate information
- Understand user questions
- Use previous conversation messages for follow-up questions

## 💬 Conversation Context

The chatbot stores messages from the current session and sends the conversation history to the AI model.

Example:

User: What is Python?

Bot: Python is a programming language used for many applications.

User: What is it used for?

Bot: Python is used for web development, data analysis, automation, machine learning and artificial intelligence.

The second question can be understood using the previous conversation context.

## 🔗 AI API Integration

The project uses the Hugging Face Inference API through the Python `InferenceClient`.

The chatbot sends the user's message and conversation history to the AI model and receives an AI-generated response.

## 🧪 Testing

The chatbot was tested using different questions such as:

- Hello
- What is Python?
- What is artificial intelligence?
- What is Python used for?
- Explain machine learning
- Follow-up questions

The chatbot successfully generated responses for the test cases.

## ▶️ How to Run

1. Install Python.
2. Install the required packages.
3. Set the Hugging Face API token as an environment variable.
4. Open the project folder in Command Prompt or Terminal.
5. Run:

```text
python -m streamlit run app.py
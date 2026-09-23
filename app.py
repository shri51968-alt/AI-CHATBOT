import os
from huggingface_hub import InferenceClient
import streamlit as st

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

client = InferenceClient(token=os.getenv("HF_TOKEN"))


st.title("🤖 AI Chatbot")
st.write("An AI chatbot with conversation context")


# Sidebar
with st.sidebar:
    st.header("⚙️ Chat Settings")
    st.write("AI Chatbot Project")
    st.write("Mode: Demo")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []


# Generate chatbot response
def generate_response(user_input):

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI assistant. "
                "Give clear, simple and accurate answers. "
                "Use the conversation history to understand follow-up questions."
            )
        }
    ]

    # Add conversation history
    messages.extend(st.session_state.messages)

    response = client.chat_completion(
        model="openai/gpt-oss-120b",
        messages=messages,
        max_tokens=300,
        temperature=0.7
    )

    return response.choices[0].message.content
# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# User input
user_input = st.chat_input("Ask me anything...")

if user_input:

    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    answer = generate_response(user_input)

    with st.chat_message("assistant"):
        st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
import streamlit as st

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

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

    text = user_input.lower()

    if "what is python" in text:
        return (
            "Python is a high-level programming language. "
            "It is easy to learn and is widely used in software "
            "development, data analysis, AI and machine learning."
        )

    elif "python" in text or "used for" in text:
        return (
            "Python is used for web development, data analysis, "
            "automation, machine learning and artificial intelligence."
        )

    elif "hello" in text or "hi" in text:
        return "Hello! How can I help you today?"

    elif "ai" in text or "artificial intelligence" in text:
        return (
            "Artificial Intelligence (AI) is a technology that "
            "allows computers to perform tasks that normally "
            "require human intelligence."
        )

    elif "how are you" in text:
        return "I'm doing great! What would you like to learn?"

    elif "thank" in text:
        return "You're welcome!"

    else:
        return "That's an interesting question! I'm currently running in demo mode."
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
import streamlit as st
from chatbot import generate_response

# Page Config
st.set_page_config(page_title="NLP Chatbot", page_icon="")

st.title("NLP Chatbot with Streamlit")

#  Sidebar
st.sidebar.title("Chatbot Settings")

st.sidebar.markdown("### About")
st.sidebar.info(
    "This chatbot uses:\n\n"
    "- NLP preprocessing\n"
    "- NLTK\n"
    "- Rule-based logic"
)

# Clear Chat Button
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.success("Chat cleared!")

# Chat Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# User Input
user_input = st.text_input("Ask something to chat bot , try saying hi:", key="input")

if user_input:
    response = generate_response(user_input)

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Display Chat
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
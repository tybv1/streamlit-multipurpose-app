"""Streamlit page for the GPT4All Chatbot."""

import streamlit as st

from app import config  # Absolute import
from app.utils import chatbot_utils  # Absolute import


def render_page():
    """Renders the Chatbot page."""
    st.title("🤖 Chatbot")

    # Model parameters
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=config.GPT4ALL_DEFAULT_TEMP,
        step=0.05,
        help="Controls randomness. Lower values are more deterministic.",
    )
    top_p = st.slider(
        "Top P",
        min_value=0.0,
        max_value=1.0,
        value=config.GPT4ALL_DEFAULT_TOP_P,
        step=0.05,
        help="Nucleus sampling. Higher values consider more word choices.",
    )

    # Chat mode selection
    chat_mode = st.radio(
        "Chat Mode", ["Single Chat", "Iterative Conversation"]
    )

    # Initialize or get chat history from session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if user_input := st.chat_input("Your message"):
        # Add user message to chat history
        st.session_state.chat_history.append(
            {"role": "user", "content": user_input}
        )
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get chatbot response
        with st.spinner("Thinking..."):
            if chat_mode == "Single Chat":
                response = chatbot_utils.get_response(
                    user_input, temperature, top_p
                )
            else:  # Iterative Conversation
                response = chatbot_utils.get_iterative_response(
                    st.session_state.chat_history, temperature, top_p
                )
            st.session_state.chat_history.append(
                {"role": "assistant", "content": response}
            )

        # Display chatbot response
        with st.chat_message("assistant"):
            st.markdown(response)

    # Reset button for iterative conversation
    if chat_mode == "Iterative Conversation" and st.button("Reset Conversation"):
        st.session_state.chat_history = []
        st.rerun()
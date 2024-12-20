"""Main module for the Streamlit application."""

import streamlit as st

from app import config
from app.pages import news_sentiment, chatbot, covid_dashboard

# Basic page config
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    """Main function to run the Streamlit app."""
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to", ["News Sentiment", "Chatbot", "COVID Dashboard"]
    )

    if page == "News Sentiment":
        news_sentiment.render_page()
    elif page == "Chatbot":
        chatbot.render_page()
    elif page == "COVID Dashboard":
        covid_dashboard.render_page()


if __name__ == "__main__":
    main()
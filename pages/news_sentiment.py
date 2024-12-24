"""Streamlit page for News Sentiment Analysis."""

import streamlit as st

import config  # Absolute import
from utils import news_utils, nlp_utils  # Absolute import


def render_page():
    """Renders the News Sentiment Analysis page."""
    st.title("📰 News Sentiment Analysis")

    # User selects a news category
    selected_category = st.selectbox("Select News Category", config.NEWS_CATEGORIES)

    # User inputs a free search query
    search_query = st.text_input("Or enter a search query (optional)")

    # User sets the maximum number of articles
    max_articles = st.slider(
        "Maximum Number of News Articles",
        min_value=1,
        max_value=20,
        value=config.MAX_NEWS_ARTICLES,
    )

    if st.button("Fetch News"):
        # Construct the correct URL based on user input
        if search_query:
            news_url = f"{config.GOOGLE_NEWS_BASE_URL}/search?q={search_query}"
        elif selected_category != "Choose Topic":
            news_url = f"{config.GOOGLE_NEWS_BASE_URL}/headlines/section/topic/{selected_category}"
        else:
            news_url = config.GOOGLE_NEWS_BASE_URL  # Default: trending news

        # Fetch news articles
        news_data = news_utils.fetch_news(news_url, max_articles)

        if news_data:
            for article in news_data:
                st.markdown(f"### [{article['title']}]({article['link']})")
                st.write(f"**Published:** {article['published']}")

                # Summarize the article
                summary = news_utils.summarize_article(article["link"])
                st.write("**Summary:**")
                st.write(summary)

                # Perform sentiment analysis
                sentiment_scores = nlp_utils.get_sentiment(summary)
                st.write("**Sentiment Analysis:**")
                st.write(f"   - Polarity: {sentiment_scores['polarity']:.2f}")
                st.write(f"   - Subjectivity: {sentiment_scores['subjectivity']:.2f}")

                st.write("---")
        else:
            st.error("Failed to fetch news articles.")

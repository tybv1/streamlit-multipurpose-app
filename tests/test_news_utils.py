"""Unit tests for the news_utils module."""

import pytest

from app.utils import news_utils

@pytest.mark.parametrize("invalid_url", [
    "",
    " ",
    "invalid-url",
    "https://",
    "ftp://example.com",
    "https://nonexistent-domain.com",
])
def test_fetch_news_invalid_url(invalid_url):
    """Test that fetch_news returns an empty list for invalid URLs."""
    articles = news_utils.fetch_news(invalid_url)
    assert articles == []


def test_fetch_news_valid_url():
    """Test that fetch_news returns a list of articles for a valid URL."""
    valid_url = "https://news.google.com/news/rss"  # Example valid URL
    articles = news_utils.fetch_news(valid_url, max_articles=5)
    assert isinstance(articles, list)
    assert len(articles) <= 5
    for article in articles:
        assert isinstance(article, dict)
        assert "title" in article
        assert "link" in article
        assert "published" in article

def test_summarize_article_invalid_url():
    """Test that summarize_article returns an empty string for invalid URLs."""
    invalid_url = "https://invalid-url"
    summary = news_utils.summarize_article(invalid_url)
    assert summary == ""


def test_summarize_article_valid_url():
    """Test that summarize_article returns a summary for a valid URL."""
    valid_url = "https://www.bbc.com/news/world-us-canada-68089454"  # Example valid URL (replace as needed)
    summary = news_utils.summarize_article(valid_url)
    assert isinstance(summary, str)
    assert len(summary) > 0
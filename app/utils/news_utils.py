"""Utility functions for fetching and processing news articles."""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from newspaper import Article

from app.utils import nlp_utils


def fetch_news(url, max_articles=10):
    """
    Fetches news articles from a given URL.

    Args:
        url (str): The URL of the news source (Google News RSS).
        max_articles (int): The maximum number of articles to fetch.

    Returns:
        list: A list of dictionaries, where each dictionary represents a news
              article with 'title', 'link', and 'published' keys.
              Returns an empty list if fetching fails.
    """
    try:
        client = urlopen(url)
        xml_page = client.read()
        client.close()

        soup_page = soup(xml_page, "xml")
        news_list = soup_page.find_all("item")

        articles = []
        for news in news_list[:max_articles]:
            articles.append(
                {
                    "title": news.title.text,
                    "link": news.link.text,
                    "published": news.pubDate.text,
                }
            )
        return articles
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []


def summarize_article(article_url):
    """
    Summarizes a news article from a given URL using the newspaper3k library.

    Args:
        article_url (str): The URL of the news article.

    Returns:
        str: The summary of the article.
             Returns an empty string if summarization fails.
    """
    try:
        article = Article(article_url)
        article.download()
        article.parse()
        article.nlp()
        return article.summary
    except Exception as e:
        print(f"Error summarizing article: {e}")
        return ""
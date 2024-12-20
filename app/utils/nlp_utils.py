"""Utility functions for natural language processing tasks."""

from textblob import TextBlob
import spacy

# Load the spaCy English language model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading en_core_web_sm...")
    from spacy.cli import download

    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


def get_sentiment(text):
    """
    Performs sentiment analysis on a given text using TextBlob.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing the polarity and subjectivity scores.
    """
    blob = TextBlob(text)
    return {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity,
    }


def detect_bias(text):
    """
    Detects potential bias in a text using spaCy.

    This is a placeholder function. Bias detection is a complex task and
    requires more sophisticated techniques.

    Args:
        text (str): The text to analyze.

    Returns:
        bool: True if potential bias is detected, False otherwise.
    """
    doc = nlp(text)
    # Placeholder: Check for the presence of certain keywords or patterns
    # that might indicate bias.
    biased_words = ["always", "never", "all", "none"]  # Example
    for token in doc:
        if token.text.lower() in biased_words:
            return True
    return False
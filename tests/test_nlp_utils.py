"""Unit tests for the nlp_utils module."""

import pytest

from utils import nlp_utils  # Absolute import


@pytest.mark.parametrize(
    "text, expected_polarity, expected_subjectivity",
    [
        ("This is a great product!", 0.8, 0.75),  # Positive sentiment
        ("This is a terrible product!", -1.0, 1.0),  # Negative sentiment
        ("This is an okay product.", 0.5, 0.5),  # Neutral sentiment
        ("", 0.0, 0.0),  # Empty string
    ],
)
def test_get_sentiment(text, expected_polarity, expected_subjectivity):
    """Test the get_sentiment function with various inputs."""
    sentiment = nlp_utils.get_sentiment(text)
    assert sentiment["polarity"] == expected_polarity
    assert sentiment["subjectivity"] == expected_subjectivity


@pytest.mark.parametrize(
    "text, expected_bias",
    [
        ("Everyone knows that this is true.", True),  # Biased language
        ("This is a factual statement.", False),  # Neutral language
        ("All politicians are corrupt.", True),  # Biased generalization
        ("The data suggests a trend.", False),  # Neutral observation
        ("", False),  # Empty string
    ],
)
def test_detect_bias(text, expected_bias):
    """Test the detect_bias function with various inputs."""
    bias_detected = nlp_utils.detect_bias(text)
    assert bias_detected == expected_bias

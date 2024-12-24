"""Unit tests for the chatbot_utils module."""

import pytest

from utils import chatbot_utils  # Absolute import
import config


@pytest.mark.skipif(
    not config.GPT4ALL_MODEL_PATH, reason="GPT4ALL_MODEL_PATH not configured"
)
def test_get_response():
    """Test the get_response function."""
    prompt = "Hello, how are you?"
    temperature = 0.7
    top_p = 0.9
    response = chatbot_utils.get_response(prompt, temperature, top_p)
    assert isinstance(response, str)
    assert len(response) > 0


@pytest.mark.skipif(
    not config.GPT4ALL_MODEL_PATH, reason="GPT4ALL_MODEL_PATH not configured"
)
def test_get_iterative_response():
    """Test the get_iterative_response function."""
    chat_history = [
        {"role": "user", "content": "What's the weather like today?"},
        {
            "role": "assistant",
            "content": "I'm sorry, I don't have access to real-time weather information.",
        },
        {"role": "user", "content": "Okay, what's the capital of France?"},
    ]
    temperature = 0.7
    top_p = 0.9
    response = chatbot_utils.get_iterative_response(chat_history, temperature, top_p)
    assert isinstance(response, str)
    assert len(response) > 0
    assert "Paris" in response  # Check for a relevant keyword in response

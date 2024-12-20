"""Utility functions for the GPT4All chatbot."""

from gpt4all import GPT4All

from app import config

# Load the GPT4All model (do this only once when the app starts)
gpt4all_model = GPT4All(config.GPT4ALL_MODEL_PATH)

def get_response(prompt, temperature, top_p):
    """
    Generates a response to a single prompt using the GPT4All model.

    Args:
        prompt (str): The user's prompt.
        temperature (float): The temperature for sampling.
        top_p (float): The top-p value for nucleus sampling.

    Returns:
        str: The chatbot's response.
    """
    try:
        with gpt4all_model.chat_session():
            response = gpt4all_model.generate(
                prompt, temp=temperature, top_p=top_p
            )
            return response
    except Exception as e:
        print(f"Error getting chatbot response: {e}")
        return "Sorry, I encountered an error."


def get_iterative_response(chat_history, temperature, top_p):
    """
    Generates a response in an iterative conversation using the GPT4All model.

    Args:
        chat_history (list): A list of dictionaries representing the chat
                             history, where each dictionary has "role" (user or
                             assistant) and "content" keys.
        temperature (float): The temperature for sampling.
        top_p (float): The top-p value for nucleus sampling.

    Returns:
        str: The chatbot's response.
    """
    try:
        with gpt4all_model.chat_session():
            for message in chat_history:
                if message["role"] == "user":
                    gpt4all_model.generate(message["content"], temp=temperature, top_p=top_p)
                else:
                    gpt4all_model.generate(message["content"], temp=temperature, top_p=top_p, response=False)
        
            response = gpt4all_model.generate("", temp=temperature, top_p=top_p)
            return response
    except Exception as e:
        print(f"Error getting iterative chatbot response: {e}")
        return "Sorry, I encountered an error."
# Multipurpose Streamlit Application

This project is a multi-page Streamlit application that demonstrates various Python skills, including frontend development, natural language processing, data analysis, and AI chatbot integration.

## Features

-   **Page 1: News Sentiment Analysis:** Fetches news articles from Google News, summarizes them, and performs sentiment analysis using NLP techniques.
-   **Page 2: GPT4All Chatbot:** An interactive chatbot powered by a local GPT4All language model.
-   **Page 3: COVID-19 Dashboard:** An interactive dashboard to visualize COVID-19 data using Pandas and Plotly.

## Prerequisites

-   Python 3.8+
-   Git

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd streamlit-multipurpose-app
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Download NLTK data (if needed):**

    ```python
    import nltk
    nltk.download('punkt')
    ```
5. **Download a GPT4All Model**
Download a GPT4All compatible model like `Llama-3.2-3B-Instruct-Q4_0.gguf` and place it in a known directory. Update the `config.py` with the model path.

## Setting up the Chatbot

This project uses a local GPT4All language model for the chatbot. You need to download it separately:

1.  **Download a model:** Go to [https://gpt4all.io/](https://gpt4all.io/) and download the `Llama-3.2-3B-Instruct-Q4_0.gguf` model from the "Ecosystem" section.
2.  **Place the model:** Create a `models` folder in the project's root directory and place the downloaded `.gguf` file inside.
3.  **Update `config.py`:** Make sure the `GPT4ALL_MODEL_PATH` variable in `config.py` points to the correct location of your model file.

6.  **(Optional) Install pre-commit hooks:**

    ```bash
    pre-commit install
    ```

## Running the Application

```bash
streamlit run app/main.py
"""Configuration settings for the Streamlit application."""

import os

# --- General Configs ---
APP_TITLE = "Multipurpose Streamlit App"

# --- News API Configs (if using newsapi.org) ---
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")  # Get API key from environment variable
GOOGLE_NEWS_BASE_URL = "https://news.google.com/rss"
NEWS_CATEGORIES = [
    "Choose Topic",
    "WORLD",
    "NATION",
    "BUSINESS",
    "TECHNOLOGY",
    "ENTERTAINMENT",
    "SPORTS",
    "SCIENCE",
    "HEALTH",
]
MAX_NEWS_ARTICLES = 10

# --- GPT4All Configs ---
GPT4ALL_MODEL_PATH = (
    # Update with your actual model path
    "models/Llama-3.2-3B-Instruct-Q4_0.gguf"
)
GPT4ALL_DEFAULT_TEMP = 0.7
GPT4ALL_DEFAULT_TOP_P = 0.9

# --- COVID Dashboard Configs ---
# These are example links. You'll need to replace them with the actual links to the data.
COVID_DATA_LINKS = [
    "https://example.com/covid_data_1.xlsx",
    "https://example.com/covid_data_2.xlsx",
    # ... more links
]
# Optional: Include a default data file in your project
DEFAULT_COVID_DATA_FILE = "app/data/default_covid_data.xlsx"
REGIONS = [
    "East of England",
    "London",
    "Midlands",
    "North East and Yorkshire",
    "North West",
    "South East",
    "South West",
]
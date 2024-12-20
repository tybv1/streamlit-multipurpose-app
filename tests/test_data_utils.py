"""Unit tests for the data_utils module."""

import pytest
import pandas as pd
from app.utils import data_utils
from app import config

def create_test_excel_file(file_path, data):
    """Helper function to create a test Excel file."""
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False, engine='openpyxl')

def test_load_data_valid_file():
    """Test loading data from a valid Excel file."""
    # Create a dummy Excel file for testing
    test_file = "test_data.xlsx"
    test_data = {
        "Date": ["2023-01-01", "2023-01-02"],
        "Total Beds Occupied Covid": [10, 20],
        "Admissions Total": [5, 8],
        "Diagnosis Total": [12, 15],
        "Region": ["London", "South East"],
    }
    create_test_excel_file(test_file, test_data)

    df = data_utils.load_data(test_file)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == list(test_data.keys())

    # Clean up the test file
    import os
    os.remove(test_file)

def test_load_data_invalid_file():
    """Test loading data from an invalid file path."""
    df = data_utils.load_data("invalid_file.xlsx")
    assert df is None

def test_clean_data():
    """Test the data cleaning function."""
    # Create a sample DataFrame for testing
    data = {
        "Date": ["2023-01-01", "2023-01-02", "2023/01/03"],
        "Total Beds Occupied Covid": [10, "20", None],
        "Admissions Total": ["5", 8, ""],
        "Diagnosis Total": [12.5, 15, "abc"],
        "Region": ["London", "South East", "Midlands"],
    }
    df = pd.DataFrame(data)

    df_cleaned = data_utils.clean_data(df)

    # Assertions to check if cleaning was done correctly
    assert isinstance(df_cleaned, pd.DataFrame)
    assert pd.api.types.is_datetime64_any_dtype(df_cleaned["Date"])
    assert pd.api.types.is_numeric_dtype(df_cleaned["Total Beds Occupied Covid"])
    assert pd.api.types.is_numeric_dtype(df_cleaned["Admissions Total"])
    assert pd.api.types.is_numeric_dtype(df_cleaned["Diagnosis Total"])
    assert df_cleaned["Total Beds Occupied Covid"].isnull().sum() == 0
    assert df_cleaned["Admissions Total"].isnull().sum() == 0
    assert df_cleaned["Diagnosis Total"].isnull().sum() == 0
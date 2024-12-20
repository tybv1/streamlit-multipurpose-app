"""Utility functions for data loading and processing for the dashboard."""

import pandas as pd

from app import config

def load_data(filepath_or_buffer):
    """
    Loads data from an Excel file into a Pandas DataFrame.

    Args:
        filepath_or_buffer: The path to the Excel file or a file-like object.

    Returns:
        pandas.DataFrame: The loaded DataFrame, or None if an error occurred.
    """
    try:
        df = pd.read_excel(filepath_or_buffer, engine='openpyxl')
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath_or_buffer}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def clean_data(df):
    """
    Performs basic data cleaning operations on the COVID-19 DataFrame.

    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pandas.DataFrame: The cleaned DataFrame.
    """
    df_cleaned = df.copy()

    # 1. Convert 'Date' column to datetime objects
    if 'Date' in df_cleaned.columns:
        df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])
    else:
        print("Warning: 'Date' column not found.")

    # 2. Convert relevant columns to numeric type (handle errors)
    numeric_cols = ["Total Beds Occupied Covid", "Admissions Total", "Diagnosis Total"]
    for col in numeric_cols:
        if col in df_cleaned.columns:
            df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')
        else:
            print(f"Warning: '{col}' column not found.")

    # 3. Fill missing values (if necessary)
    df_cleaned.fillna(0, inplace=True)  # Example: Fill NaN with 0

    # 4. Add a 'Region' column if it doesn't exist (based on the data format)
    if "Region" not in df_cleaned.columns:
        # Assuming you can infer the region from some other column or data logic
        # Example: If you have a 'Hospital' column, you might map hospitals to regions
        # df_cleaned['Region'] = df_cleaned['Hospital'].map(hospital_to_region_mapping)
        print("Warning: 'Region' column not found. You might need to add logic to infer it.")

    return df_cleaned
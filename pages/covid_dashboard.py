"""Streamlit page for the COVID-19 Dashboard."""

import streamlit as st

# import pandas as pd
import plotly.express as px

import config  # Absolute import
from utils import data_utils  # Absolute import


def render_page():
    """Renders the COVID-19 Dashboard page."""
    st.title("📊 COVID-19 Dashboard")

    # File uploader
    uploaded_file = st.file_uploader("Upload COVID-19 Data (Excel)", type=["xlsx"])

    if uploaded_file:
        df = data_utils.load_data(uploaded_file)
        st.session_state.data = df  # Store data in session state
    elif "data" in st.session_state:
        # Use data from session state if available
        df = st.session_state.data
    else:
        st.write("Please upload a file or use the default data.")
        # Optionally load default data if provided in config
        if config.DEFAULT_COVID_DATA_FILE:
            try:
                df = data_utils.load_data(config.DEFAULT_COVID_DATA_FILE)
                st.session_state.data = df
            except FileNotFoundError:
                st.error("Default data file not found.")
                df = None
        else:
            df = None

    if df is not None:
        # Display basic info about the DataFrame
        st.write("Data Preview:")
        st.dataframe(df.head())

        # --- Data Cleaning and Preprocessing ---
        df_cleaned = data_utils.clean_data(df)

        # --- Sidebar Filters ---
        st.sidebar.header("Filters")

        # Region filter
        selected_regions = st.sidebar.multiselect(
            "Select Regions", config.REGIONS, default=config.REGIONS
        )

        # --- Filter data based on selections ---
        df_filtered = df_cleaned[df_cleaned["Region"].isin(selected_regions)]

        # --- Create Visualizations ---
        st.header("Visualizations")

        # --- Total Beds Occupied by COVID Patients ---
        st.subheader("Total Beds Occupied by COVID Patients")
        fig_beds = px.bar(
            df_filtered,
            x="Date",
            y="Total Beds Occupied Covid",
            color="Region",
            barmode="group",
        )
        st.plotly_chart(fig_beds)

        # --- Total Admissions ---
        st.subheader("Total Admissions")
        fig_admissions = px.bar(
            df_filtered,
            x="Date",
            y="Admissions Total",
            color="Region",
            barmode="group",
        )
        st.plotly_chart(fig_admissions)

        # --- Total Diagnosis ---
        st.subheader("Total Diagnosis")
        fig_diagnosis = px.pie(df_filtered, names="Region", values="Diagnosis Total")
        st.plotly_chart(fig_diagnosis)
    else:
        st.info("Please upload COVID-19 data to get started.")

import streamlit as st
import pandas as pd
import random

st.title("💰 Personal Finance Tracker")

# --- Upload CSV ---
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Check required columns
    required_columns = {"Date", "Description", "Amount"}
    if not required_columns.issubset(df.columns):
        st.error("CSV must contain 'Date', 'Description', 'Amount' columns")
    else:
        # Initialize categories
        if 'Category' not in df.columns:
            df['Category'] = ""
        
        # Example: simple auto-categorization rules
        auto_rules = {
            "grocery": "Food",
            "salary": "Income",
            "rent": "Housing",
            "uber": "Transport",
            "coffee": "Food",
            "restaurant": "Food",
            "electricity": "Utilities",
            "water": "Utilities",
            "internet": "Utilities",
            "gym": "Health",
            "bookstore": "Entertainment",
            "movie": "Entertainment"
        }
        
        def categorize(description):
            description = str(description).lower()
            for key, cat in auto_rules.items():
                if key in description:
                    return cat
            return "Uncategorized"
        
        df['Category'] = df.apply(lambda row: row['Category'] if row['Category'] else categorize(row['Description']), axis=1)
        
        # --- Editable table (Streamlit 1.25+) ---
        st.subheader("Edit categories")
        edited_df = st.data_editor(df, num_rows="dynamic")
        
        # --- Summary chart ---
        st.subheader("Spending Summary")
        summary = edited_df.groupby('Category')['Amount'].sum().sort_values()
        st.bar_chart(summary)

import pandas as pd
import os

def load_data(relative_path):
    """
    Load CSV data using a path relative to the project root.
    Works in both local and Streamlit Cloud environments.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, relative_path)

    df = pd.read_csv(full_path)

    # Standardize column names
    df.columns = df.columns.str.lower()

    # Parse date
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    else:
        raise ValueError("No date column found")

    # Standardize sales column
    if "weekly_sales" in df.columns:
        df.rename(columns={"weekly_sales": "sales"}, inplace=True)
    elif "sales" not in df.columns:
        raise ValueError("No sales column found")

    return df

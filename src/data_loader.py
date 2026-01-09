import pandas as pd

print("Script started")

def load_data(path):
    print("Loading CSV...")
    df = pd.read_csv(path)

    print("Original columns:", df.columns)

    # standardize column names
    df.columns = df.columns.str.lower()

    # fix date parsing (DD-MM-YYYY)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    else:
        raise ValueError("No date column found")

    # standardize sales column
    if 'weekly_sales' in df.columns:
        df.rename(columns={'weekly_sales': 'sales'}, inplace=True)
    elif 'sales' not in df.columns:
        raise ValueError("No sales column found")

    return df

if __name__ == "__main__":
    print("Main block running")
    df = load_data("data/raw/sales.csv")
    print(df.head())

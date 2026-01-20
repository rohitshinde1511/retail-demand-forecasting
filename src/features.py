import pandas as pd

def create_features(df):
    """
    Create time-series and business features for demand forecasting.
    Assumes weekly aggregated sales data.
    """

    df = df.sort_values(["store", "date"]).copy()

    # --- Lag features (temporal dependency) ---
    df["lag_1"] = df.groupby("store")["sales"].shift(1)
    df["lag_2"] = df.groupby("store")["sales"].shift(2)
    df["lag_4"] = df.groupby("store")["sales"].shift(4)

    # --- Rolling statistics ---
    df["rolling_mean_4"] = (
        df.groupby("store")["sales"]
        .shift(1)
        .rolling(window=4)
        .mean()
    )

    df["rolling_std_4"] = (
        df.groupby("store")["sales"]
        .shift(1)
        .rolling(window=4)
        .std()
    )

    # --- Holiday flag ---
    df["holiday_flag"] = df["holiday_flag"].astype(int)

    # Drop rows with missing feature values
    df = df.dropna().reset_index(drop=True)

    return df


###Features :
	
#lag_1, lag_2, lag_4  ->  Captures short-term and monthly demand memory
#rolling_mean_4       ->  Smooths recent demand trend
#rolling_std_4	      ->  Captures demand volatility
#holiday_flag	      ->  Models holiday demand uplift
#store	              ->  Captures store-level heterogeneity


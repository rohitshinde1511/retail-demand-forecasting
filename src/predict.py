import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from src.data_loader import load_data
from src.features import create_features
from src.business_metrics import calculate_reorder_quantity


def forecast_next_week(store_id, current_inventory):
    df = load_data("data/raw/sales.csv")
    df = create_features(df)
    df = df.sort_values(["store", "date"])

    features = [
        "lag_1",
        "lag_2",
        "lag_4",
        "rolling_mean_4",
        "rolling_std_4",
        "holiday_flag",
        "store",
    ]

    X = df[features]
    y = df["sales"]

    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X, y)

    latest = df[df["store"] == store_id].iloc[-1:]
    forecast = model.predict(latest[features])[0]

    reorder_qty = calculate_reorder_quantity(
        forecast_demand=forecast,
        current_inventory=current_inventory,
        safety_stock=0
    )

    return forecast, reorder_qty

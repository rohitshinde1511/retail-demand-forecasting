import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

from src.data_loader import load_data
from src.features import create_features



def train_model():
    # Load and prepare data
    df = load_data("data/raw/sales.csv")
    df = create_features(df)

    # Sort by time to avoid leakage
    df = df.sort_values(["store", "date"])

    # Features and target
    target = "sales"
    features = [
        "lag_1",
        "lag_2",
        "lag_4",
        "rolling_mean_4",
        "rolling_std_4",
        "holiday_flag",
        "store"
    ]

    X = df[features]
    y = df[target]

    # Time-based train-test split (80/20)
    split_date = df["date"].quantile(0.8)

    X_train = X[df["date"] <= split_date]
    X_test = X[df["date"] > split_date]

    y_train = y[df["date"] <= split_date]
    y_test = y[df["date"] > split_date]

    # ------------------
    # Baseline model
    # ------------------
    baseline_preds = X_test["lag_1"]
    baseline_mae = mean_absolute_error(y_test, baseline_preds)

    print(f"Baseline MAE (lag-1): {baseline_mae:.2f}")

    # ------------------
    # ML model
    # ------------------
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)
    ml_preds = model.predict(X_test)
    ml_mae = mean_absolute_error(y_test, ml_preds)

    print(f"ML Model MAE (RandomForest): {ml_mae:.2f}")

    return baseline_mae, ml_mae


if __name__ == "__main__":
    train_model()

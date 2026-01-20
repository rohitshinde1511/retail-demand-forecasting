import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.predict import forecast_next_week


st.set_page_config(
    page_title="Retail Demand Forecasting",
    layout="centered"
)

st.title("📦 Retail Demand Forecasting & Decision System")

st.info(
    "ℹ️ This demo forecasts **weekly demand** using historical retail sales data.\n\n"
    "- Valid Store IDs: **1–50**\n"
    "- Inventory represents **current weekly on-hand stock (units)**\n"
    "- Values outside realistic ranges are restricted for accuracy"
)


st.markdown(
    """
    Forecast next week's demand and receive inventory reorder recommendations
    based on historical retail sales data.
    """
)

st.divider()

# User inputs
store_id = st.number_input(
    "Store ID",
    min_value=1,
    max_value=50,
    step=1,
    value=1,
    help="Select a valid store ID (1–50)"
)

current_inventory = st.number_input(
    "Current Inventory (units)",
    min_value=0,
    max_value=500_000,
    step=1_000,
    value=50_000,
    help="Enter current weekly inventory (e.g., 20,000–100,000 units)"
)


# Logical validation
if current_inventory > 200_000:
    st.warning(
        "⚠️ Inventory value is unusually high for weekly stock. "
        "Please verify this is intentional."
    )


st.caption(
    "Click to generate a one-week demand forecast and inventory reorder recommendation "
    "for the selected store."
)


if st.button("Predict Demand"):
    with st.spinner("Generating forecast..."):
        forecast, reorder_qty = forecast_next_week(
            store_id=int(store_id),
            current_inventory=int(current_inventory)
        )

    st.success("Prediction completed")
    
    st.subheader("📊 Forecast & Inventory Decision")

    st.metric(
    label="📈 Forecasted Weekly Demand",
    value=f"{forecast:,.0f} units",
    help="Predicted total units expected to be sold next week"
    )
    
    st.metric(
    label="📦 Recommended Reorder Quantity",
    value=f"{reorder_qty:,.0f} units",
    help="Suggested inventory to order based on forecast and current stock"
    )

st.caption(
    "This dashboard is a demonstration of a retail forecasting workflow and is not intended "
    "for live production use."
)



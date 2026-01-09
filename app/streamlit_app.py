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
    step=1,
    value=1
)

current_inventory = st.number_input(
    "Current Inventory (units)",
    min_value=0,
    step=1000,
    value=50000
)

if st.button("Predict Demand"):
    with st.spinner("Generating forecast..."):
        forecast, reorder_qty = forecast_next_week(
            store_id=int(store_id),
            current_inventory=int(current_inventory)
        )

    st.success("Prediction completed")

    st.metric(
        label="📈 Forecasted Weekly Demand",
        value=f"{forecast:,.0f} units"
    )

    st.metric(
        label="📦 Recommended Reorder Quantity",
        value=f"{reorder_qty:,.0f} units"
    )

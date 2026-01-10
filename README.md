# 📦 Retail Demand Forecasting & Business Decision System

🔗 **Live App**: https://retail-demand-forecasting-dashboard.streamlit.app/

---

## 📌 Overview
This project is an end-to-end **retail demand forecasting system** that predicts weekly product demand and provides **inventory reorder recommendations** based on historical sales data.

Unlike notebook-only projects, this system is:
- fully modular
- production-style
- deployed as an interactive web application

The goal is not just prediction, but **business decision support**.

---

## 🎯 Business Problem
Retailers often face:
- overstocking → higher holding costs  
- understocking → lost sales and poor customer experience  

This project addresses the problem by:
1. Forecasting next-week demand
2. Recommending how much inventory to reorder

---

## 🗂️ Dataset
- Historical weekly sales data
- Store-level sales
- External factors:
  - Holidays
  - Temperature
  - Fuel price
  - CPI
  - Unemployment

Dataset is tracked in the repository for reproducibility.

---

## 🧠 Approach & Architecture

### 1️⃣ Data Loading
- Centralized CSV loader
- Cloud-safe absolute path handling
- Standardized column names and date parsing

### 2️⃣ Feature Engineering
- Lag features (1, 2, 4 weeks)
- Rolling statistics (mean & standard deviation)
- Holiday flag
- Store identifier

These features capture **temporal demand patterns**.

### 3️⃣ Modeling
- Baseline: lag-based forecasting
- ML model: **Random Forest Regressor**
- Evaluation metric: **Mean Absolute Error (MAE)**

The ML model outperformed the baseline, validating feature usefulness.

### 4️⃣ Business Logic
A reorder recommendation is computed using:

# 📦 Retail Demand Forecasting & Business Decision System

🔗 **Live App**: https://retail-demand-forecasting-dashboard.streamlit.app/

---

## 📌 Overview
This project is an end-to-end **retail demand forecasting system** that predicts weekly product demand and provides **inventory reorder recommendations** based on historical sales data.

Unlike notebook-only projects, this system is:
- fully modular
- production-style
- deployed as an interactive web application

The goal is not just prediction, but **business decision support**.

---

## 🎯 Business Problem
Retailers often face:
- overstocking → higher holding costs  
- understocking → lost sales and poor customer experience  

This project addresses the problem by:
1. Forecasting next-week demand
2. Recommending how much inventory to reorder

---

## 🗂️ Dataset
- Historical weekly sales data
- Store-level sales
- External factors:
  - Holidays
  - Temperature
  - Fuel price
  - CPI
  - Unemployment

Dataset is tracked in the repository for reproducibility.

---

## 🧠 Approach & Architecture

### 1️⃣ Data Loading
- Centralized CSV loader
- Cloud-safe absolute path handling
- Standardized column names and date parsing

### 2️⃣ Feature Engineering
- Lag features (1, 2, 4 weeks)
- Rolling statistics (mean & standard deviation)
- Holiday flag
- Store identifier

These features capture **temporal demand patterns**.

### 3️⃣ Modeling
- Baseline: lag-based forecasting
- ML model: **Random Forest Regressor**
- Evaluation metric: **Mean Absolute Error (MAE)**

The ML model outperformed the baseline, validating feature usefulness.

### 4️⃣ Business Logic
A reorder recommendation is computed using:

reorder_quantity = forecasted_demand - current_inventory


This separates **prediction** from **decision-making**, which is critical in real systems.

---

## 🖥️ Application Interface
The Streamlit dashboard allows users to:
- Select Store ID
- Enter current inventory
- Generate demand forecast
- Receive reorder recommendation

The app is deployed publicly and runs end-to-end without notebooks.

---

## 🚀 Deployment
- Platform: **Streamlit Community Cloud**
- Environment-safe imports and file paths
- Automatic rebuilds on GitHub commits

Live URL:
👉 https://retail-demand-forecasting-dashboard.streamlit.app/

---

## 📁 Project Structure


This separates **prediction** from **decision-making**, which is critical in real systems.

---

## 🖥️ Application Interface
The Streamlit dashboard allows users to:
- Select Store ID
- Enter current inventory
- Generate demand forecast
- Receive reorder recommendation

The app is deployed publicly and runs end-to-end without notebooks.

---

## 🚀 Deployment
- Platform: **Streamlit Community Cloud**
- Environment-safe imports and file paths
- Automatic rebuilds on GitHub commits

Live URL:
👉 https://retail-demand-forecasting-dashboard.streamlit.app/

---

## 📁 Project Structure

retail-demand-forecasting/
├── app/
│ └── streamlit_app.py
├── src/
│ ├── data_loader.py
│ ├── features.py
│ ├── predict.py
│ ├── business_metrics.py
│ └── train.py
├── data/
│ └── raw/
│ └── sales.csv
├── notebooks/
│ └── 01_eda.ipynb
├── requirements.txt
└── README.md 

---

## 🔑 Key Takeaways
- Built a **deployable ML system**, not just a notebook
- Separated modeling logic from business decisions
- Solved real deployment issues (imports, paths, data tracking)
- Delivered a production-style dashboard

---

## 🔮 Future Improvements
- Store-specific models
- Seasonality-aware forecasting
- Safety stock optimization
- Model monitoring & retraining pipeline

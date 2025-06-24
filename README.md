# ETLpython
# 📊 Fraud Risk Overview Dashboard

This project showcases a business-ready dashboard created in **Power BI** to visualize the results of a Python-based ETL pipeline for financial fraud detection. It helps identify trends, patterns, and high-risk transactions using an easy-to-understand and interactive interface.

---

## 🎯 Project Objective

To build a professional dashboard that:
- Highlights high-risk or fraudulent transactions
- Monitors transaction behavior across different times
- Supports decision-making through risk scoring and categorization

---

## 🧪 Data Source

**File:** `cleaned_transactions.csv`  
**Generated from:** Python ETL script that:
- Extracts raw transaction data
- Transforms it with new features like `risk_score`, `high_value`, `transaction_hour`
- Loads the cleaned data into a CSV for visualization

---

## 📁 Key Features in the Dashboard

### 🔹 KPI Cards
- **Total Transactions**
- **Total High-Risk Transactions (Risk Score ≥ 4)**
- **Total Amount Processed**
- **Detected Fraud Cases**

### 🔹 Visualizations
- **Risk Score Distribution** (Bar Chart)
- **Fraud Cases Over Time** (Line Chart)
- **Transaction Type Breakdown** (Pie Chart: High Value vs Normal)
- **Detailed Transaction Table** (With conditional formatting)

### 🔹 Filters / Slicers
- Filter by `risk_score`, `high_value`, `transaction_hour`

---

## 🧱 Tools Used

- **Power BI Desktop** for dashboard creation
- **Python (Pandas)** for ETL processing
- **Jupyter Notebook** for prototyping
- **CSV files** for data storage and transfer

---

## 📸 Dashboard Preview



---

## 📦 File Structure

fraud-risk-dashboard/
 etl_pipeline.py # Python script for ETL
   data/
      transactions.csv # Raw data
      cleaned_transactions.csv # Output from ETL
 Fraud_ETL_Dashboard.pbix # Power BI dashboard file
 fraud_dashboard.ipynb # Optional notebook for EDA
 README.md # Project documentation


---

## 🚀 How to Use

1. Run `etl_pipeline.py` to generate `cleaned_transactions.csv`.
2. Open `Fraud_ETL_Dashboard.pbix` using Power BI Desktop.
3. Explore the dashboard interactively using filters and visuals.

---

## 🙋‍♂️ Author

**Guravasala Ashok Kumar**  
📧 cherryashok17@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ashok-kumar-70309a24a)  
🧑‍💻 [GitHub](https://github.com/Kuramatheninetails)

---

## 📝 License

This project is for educational and portfolio demonstration purposes only.

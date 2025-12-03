# Superstore Sales Analysis & Dashboard

## 📊 Project Overview
This project analyzes sales data from a Superstore to provide insights into revenue, profit, and sales trends. It includes an **interactive dashboard** built with Streamlit for data visualization.  

The goal is to understand sales performance by year, category, region, and products, and identify areas for improvement, such as products generating negative profit.

---

## 🗂 Project Files

| File Name | Description |
|-----------|-------------|
| `analysis.py` | Python script for data cleaning, exploration, and analysis |
| `superstore_dashboard.py` | Streamlit dashboard for interactive visualization |
| `Sample_-_Superstore.csv` | Dataset containing sales, orders, and product info |

---

## 🧰 Tools & Libraries
- **Python**  
- **Pandas**  
- **Plotly Express**  
- **Streamlit**  

---

## 🚀 Features

### Key Analysis
- Total Sales, Profit, and Orders  
- Negative Profit Orders count  
- Sales trends over time (daily/monthly)  
- Sales by Category and Region  
- Top 10 Products by Sales  
- Worst 10 Products (most negative profit)

### Interactive Dashboard
- Upload your own Superstore CSV or use the sample dataset  
- Filter by Year, Category, and Region  
- View interactive charts and KPI metrics  

---

## 📝 How to Run
## 1.Install dependencies
pip install pandas plotly streamlit

## 2.Run the Streamlit dashboard
streamlit run superstore_dashboard.py

## 3.Upload dataset (optional)
You can upload your own CSV or use the provided Sample_-_Superstore.csv.

## 💡 Insights
Highest sales come from Technology and Furniture categories
Regions like West and East contribute most to sales
Some products generate negative profit, highlighting areas for review

## 📁 Folder Structure
Data analyst project 1/
│
├─ analysis.py
├─ superstore_dashboard.py
├─ Sample_-_Superstore.csv
└─ README.md

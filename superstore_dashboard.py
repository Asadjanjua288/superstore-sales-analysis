import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------
#  DASHBOARD TITLE
# --------------------------
st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide")
st.title("📊 Superstore Sales Analytics Dashboard")

# --------------------------
#  DATA UPLOAD SECTION
# --------------------------
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload Superstore CSV", type=["csv"])

# Load dataset with proper encoding to avoid Unicode errors
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding='latin1')
else:
    st.info("Using local dataset...")
    try:
        df = pd.read_csv(r"C:\Users\Pc\Downloads\Sample_-_Superstore.csv", encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(r"C:\Users\Pc\Downloads\Sample_-_Superstore.csv", encoding='latin1')

# --------------------------
#  DATA CLEANING
# --------------------------
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.strftime("%B")
df["Quarter"] = df["Order Date"].dt.quarter

# --------------------------
#  SIDEBAR FILTERS
# --------------------------
st.sidebar.header("Filters")

year_filter = st.sidebar.multiselect(
    "Select Year(s)", options=sorted(df["Year"].unique()), default=sorted(df["Year"].unique())
)

category_filter = st.sidebar.multiselect(
    "Select Category", options=df["Category"].unique(), default=df["Category"].unique()
)

region_filter = st.sidebar.multiselect(
    "Select Region", options=df["Region"].unique(), default=df["Region"].unique()
)

# Apply filters
df_filtered = df[
    (df["Year"].isin(year_filter)) &
    (df["Category"].isin(category_filter)) &
    (df["Region"].isin(region_filter))
]

# --------------------------
#  KPI METRICS
# --------------------------
total_sales = df_filtered["Sales"].sum()
total_profit = df_filtered["Profit"].sum()
total_orders = df_filtered["Order ID"].nunique()
negative_profit_count = len(df_filtered[df_filtered["Profit"] < 0])

# KPI layout
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", total_orders)
col4.metric("Negative Profit Orders", negative_profit_count)

st.markdown("---")

# --------------------------
#  SALES TREND
# --------------------------
st.subheader("📈 Sales Trend Over Time")

sales_trend = df_filtered.groupby("Order Date")["Sales"].sum().reset_index()
fig1 = px.line(sales_trend, x="Order Date", y="Sales", title="Daily Sales Trend")
fig1.update_traces(mode="lines+markers")
st.plotly_chart(fig1, use_container_width=True)

# --------------------------
#  SALES BY CATEGORY
# --------------------------
st.subheader("📦 Sales by Category")

sales_category = df_filtered.groupby("Category")["Sales"].sum().reset_index()
fig2 = px.bar(sales_category, x="Category", y="Sales", title="Sales by Category", text="Sales", color="Category")
fig2.update_traces(texttemplate='$%{text:,.2f}', textposition='outside')
st.plotly_chart(fig2, use_container_width=True)

# --------------------------
#  SALES BY REGION
# --------------------------
st.subheader("🌎 Sales by Region")

sales_region = df_filtered.groupby("Region")["Sales"].sum().reset_index()
fig3 = px.bar(sales_region, x="Region", y="Sales", title="Sales by Region", text="Sales", color="Region")
fig3.update_traces(texttemplate='$%{text:,.2f}', textposition='outside')
st.plotly_chart(fig3, use_container_width=True)

# --------------------------
#  TOP 10 PRODUCTS
# --------------------------
st.subheader("🏆 Top 10 Products by Sales")

top_products = (
    df_filtered.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(top_products, x="Product Name", y="Sales", title="Top 10 Products", text="Sales", color="Product Name")
fig4.update_traces(texttemplate='$%{text:,.2f}', textposition='outside')
fig4.update_layout(xaxis_tickangle=45)
st.plotly_chart(fig4, use_container_width=True)

# --------------------------
#  RAW DATA VIEW
# --------------------------
with st.expander("📄 View Dataset"):
    st.dataframe(df_filtered)


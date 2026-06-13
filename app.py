import streamlit as st
import pandas as pd
import plotly.express as px
from forecast import predicted_revenue
from gemini_analysis import generate_insights

st.set_page_config(
    page_title="AI Business Decision Intelligence System",
    layout="wide"
)

# Load Data
df = pd.read_csv("data/cleaned_superstore.csv")

# Title
st.title("📊 AI-Powered Business Decision Intelligence System")

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# KPI Metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Sales",
        f"${total_sales:,.2f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"${total_profit:,.2f}"
    )

# Sales by Category
st.subheader("Sales by Category")

sales_by_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    sales_by_category,
    x="Category",
    y="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig1, use_container_width=True)

# Regional Analysis
st.subheader("Regional Sales Distribution")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    region_sales,
    names="Region",
    values="Sales"
)

st.plotly_chart(fig2, use_container_width=True)

# Top Customers
st.subheader("Top 10 Customers")

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .nlargest(10)
    .reset_index()
)

fig3 = px.bar(
    top_customers,
    x="Customer Name",
    y="Sales",
    title="Top 10 Customers"
)

st.plotly_chart(fig3, use_container_width=True)

# Revenue Forecast
st.subheader("Revenue Forecast")

st.metric(
    "Next Month Revenue Prediction",
    f"${predicted_revenue:,.2f}"
)

# Business Health Score
st.subheader("Business Health Score")

profit_margin = (total_profit / total_sales) * 100

health_score = min(
    100,
    max(0, profit_margin * 5)
)

st.progress(int(health_score))

st.write(
    f"Business Health Score: {health_score:.1f}/100"
)

# AI Insights
st.subheader("AI Business Insights")

if st.button("Generate AI Insights"):

    insights = generate_insights(
        total_sales,
        total_profit
    )

    st.write(insights)

# Business Questions
st.subheader("Ask Business Questions")

question = st.text_input(
    "Ask a business question"
)

if question:

    insights = generate_insights(
        total_sales,
        total_profit
    )

    st.write(insights)

# Download Report
st.subheader("Download Report")

report = f"""
Business Report

Total Sales: {total_sales}

Total Profit: {total_profit}

Profit Margin: {profit_margin:.2f}%

Forecast Revenue: {predicted_revenue:.2f}
"""

st.download_button(
    label="Download Report",
    data=report,
    file_name="business_report.txt",
    mime="text/plain"
)
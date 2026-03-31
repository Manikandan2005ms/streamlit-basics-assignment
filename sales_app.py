import streamlit as st
import pandas as pd

# Title
st.title("Sales Dashboard")

# Sample Data (5 rows, 3 columns)
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Smartwatch"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Sales": [50000, 30000, 20000, 10000, 15000]
}

df = pd.DataFrame(data)

# Sidebar Filter
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter Data
filtered_df = df[df["Category"] == category]

# Display Table
st.subheader("Filtered Sales Data")
st.dataframe(filtered_df)

# Line Chart
st.subheader("Sales Trend")
st.line_chart(filtered_df["Sales"])
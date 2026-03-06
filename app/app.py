import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Apple Global Sales Overview",
    page_icon="🍎",
    layout="wide"
)

# -------------------
# Header
# -------------------
st.image("images/apple_logo_black.svg", width=150)
st.title("📊 Apple Global Sales Overview")
st.markdown('General analysis of global sales, with key performance indicators.')


# -------------------
# Notes / Explanation
# -------------------
with st.expander("📌 Notes"):
    st.write("""
        Apple Global Sales Analysis

        This project analyzes Apple’s global sales dataset to generate meaningful insights and visualizations using Python and Streamlit. It provides a dashboard overview of key metrics, trends, and product performance.

        The main overview page provides:

        Total Orders – Total number of orders recorded in the dataset.

        Total Products – Number of unique products sold.

        Average Customer Rating – Average rating given by customers.

        Total Revenue (USD) – Total revenue generated.

        All these metrics are presented in summary cards for quick insights.

        📊 Visualizations

        The dashboard includes interactive visualizations:

        Sales Distribution Across Years – Shows the yearly distribution of sales.

        Revenue Distribution Across Months – Highlights monthly revenue trends.

        Top 10 Products by Revenue – Bar chart of highest revenue-generating products.

        Top 10 Products by Units Sold – Bar chart of most sold products.

        Products Sunburst Chart – Displays product hierarchy and contribution to revenue.

        Location Sunburst Chart – Shows sales contribution by region/country.

        🛠 Tools & Libraries

        Python 3.11+

        Streamlit
        – Web dashboard framework

        Plotly Express
        – Interactive visualizations

        Pandas & NumPy – Data manipulation

        Matplotlib & WordCloud – Additional plotting

        🚀 How to Run

            https://apple-global-sales-analysis.streamlit.app/

        📈 Insights

        From the raw dataset analysis:

        Total Orders: ✅

        Total Products: ✅

        Average Customer Rating: ✅

        Total Revenue: ✅

        And visual trends:

        Seasonal patterns in sales & revenue

        Top-performing products by units and revenue

        Product and location contributions to global sales

        📌 Notes

        Any new pages added to the pages/ folder are automatically listed in the sidebar.

        Ensure images/apple_logo.png is present for branding.

        Dataset is stored in data/apple_sales.csv
    """)
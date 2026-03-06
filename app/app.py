import streamlit as st
from pathlib import Path

# -------------------
# Page Config
# -------------------
st.set_page_config(
    page_title="Apple Global Sales Dashboard",
    page_icon="🍎",
    layout="wide"
)

# -------------------
# Sidebar
# -------------------
st.sidebar.image("app/images/apple_logo.png", width=150)
st.sidebar.title("Navigation")
st.sidebar.markdown("---")
st.sidebar.write("اختر الصفحة اللي تحب تشوفها:")

# صفحات موجودة في pages/
pages = {
    "Dashboard": "app/pages/dashboard.py",
    "Sales by Region": "app/pages/sales_by_region.py",
    "Product Analysis": "app/pages/product_analysis.py"
}

selection = st.sidebar.radio("Go to", list(pages.keys()))

# -------------------
# Load Selected Page
# -------------------
page_path = pages[selection]
with open(page_path, "r", encoding="utf-8") as f:
    code = f.read()
exec(code)
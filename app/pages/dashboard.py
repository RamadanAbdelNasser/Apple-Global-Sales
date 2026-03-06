import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st          # streamlit run app/app.py
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config( 'Analysis Dashboard', ':bar_chart:', 'wide' )

col1, col2 = st.columns([1, 15])
col1.image("images/apple_logo_black.svg", width=250) 
col2.title("Apple Sales Dashboard")



df = pd.read_csv('data/clean_data/apple_global_sales_cleaned_data.csv')

# Filter SideBar

payment_method_filter = st.sidebar.multiselect( 'Payment Method',
                                  options= df['payment_method'].unique(),
                                  default= df['payment_method'].unique()
                                  )

return_status_filter = st.sidebar.multiselect( 'Return Status',
                                  options= df['return_status'].unique(),
                                  default= df['return_status'].unique(),
                                  )

sales_channel_filter = st.sidebar.multiselect( 'Sales Channel',
                                  options= df['sales_channel'].unique(),
                                  default= df['sales_channel'].unique(),
                                  )

color_filter = st.sidebar.multiselect( 'Colors',
                                  options= df['color'].unique(),
                                  default= df['color'].unique(),
                                  )

discount_pct_filter = st.sidebar.slider( 'discount_pct',
                                  min_value= df['discount_pct'].min(),
                                  max_value= df['discount_pct'].max()
                                  )



filtered_df =df.query(' (payment_method == @payment_method_filter) and (return_status == @return_status_filter) and (sales_channel == @sales_channel_filter) and (color == @color_filter) and (discount_pct >= @discount_pct_filter) ' )


Total_Sales = len(filtered_df['sale_id'])
Total_Products = filtered_df['product_name'].nunique()
Avg_Customer_Ratings = filtered_df[filtered_df['has_rating']==True]['customer_rating'].mean()
Total_Revenue = filtered_df['revenue_usd'].sum()

Total_Revenue_across_Years_df = filtered_df.groupby('year')['revenue_usd'].sum().to_frame().reset_index()
sales_distribution_cross_years_fig = px.line(Total_Revenue_across_Years_df,'year','revenue_usd',title='Revenue in USD in each year',color_discrete_sequence=[ "#0071E3"])
sales_distribution_cross_years_fig.update_xaxes(dtick=1)

Total_Revenue_across_Months_df = filtered_df.groupby('month')['revenue_usd'].sum().to_frame().reset_index()
revenue_distribution_cross_months_fig = px.bar(Total_Revenue_across_Months_df,'month','revenue_usd',color='revenue_usd',title='Revenue in USD in each month',color_continuous_scale=["#E5E5EA", "#A0A0A5", "#0071E3"])


Location_sunburst_fig = px.sunburst(filtered_df,path=['region','country'],values='revenue_usd',color='revenue_usd',title='Revenue in USD cross Lactions',color_continuous_scale=["#E5E5EA", "#A0A0A5", "#0071E3"])

top_10_prducts_in_revenue_df = filtered_df.groupby('product_name')['revenue_usd'].sum().sort_values(ascending=False).to_frame().reset_index()
top_10_products_fig = px.bar(top_10_prducts_in_revenue_df.head(10),'product_name','revenue_usd',color='revenue_usd',title='Top 10 Products Revenue in USD',color_continuous_scale=["#E5E5EA", "#A0A0A5", "#0071E3"])

top_10_prducts_sold_df = filtered_df.groupby('product_name')['units_sold'].sum().sort_values(ascending=False).to_frame().reset_index()
top_10_products_sold_fig = px.bar(top_10_prducts_sold_df.head(10),'product_name','units_sold',color='units_sold',title='Top 10 Products sold',color_continuous_scale=["#E5E5EA", "#A0A0A5", "#0071E3"])

Products_sunburst_fig = px.sunburst(filtered_df,path=['category','product_name'],values='revenue_usd',color='revenue_usd',title='Revenue by each category',color_continuous_scale=["#E5E5EA", "#A0A0A5", "#0071E3"])



col_kpis, col_graph = st.columns([2, 3],border=True)
row2col1, row2col2 = col_kpis.columns(2)
sp1,sp2 = col_kpis.columns(2)
row3col1, row3col2 = col_kpis.columns(2)

def kpi_box(title, value):
    return f"""
    <div style="
        background: white;
        width: 250px;
        height: 200px;
        border-radius: 16px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.08);
        border-left: 6px solid #A0A0A5;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
        box-sizing: border-box;
    ">
        <p style="
            margin:0;
            font-size:14px;
            color:#6c757d;
            font-weight:500;
            letter-spacing:0.5px;
            text-align:center;
        ">
            {title}
        </p>
        <hr style="
            margin:10px 0;
            border:none;
            height:1px;
            width:80%;
            background-color:#f0f0f0;
        ">
        <h1 style="
            margin:0;
            font-size:44px;
            font-weight:800;
            color:#0071E3;
            text-align:center;
        ">
            {value}
        </h1>
    </div>
    """

row2col1.markdown(kpi_box("TOTAL SALES", Total_Sales), unsafe_allow_html=True)
row2col2.markdown(kpi_box("TOTAL PRODUCTS", Total_Products), unsafe_allow_html=True)
row3col1.markdown(kpi_box("AVG CUSTOMER RATING", round(Avg_Customer_Ratings,3)), unsafe_allow_html=True)
row3col2.markdown(kpi_box("TOTAL REVENUE", round(Total_Revenue)), unsafe_allow_html=True)

col_graph.plotly_chart(sales_distribution_cross_years_fig)

row4col1,row4col2 =st.columns(2,border=True)
row4col1.plotly_chart(revenue_distribution_cross_months_fig)
row4col2.plotly_chart(Location_sunburst_fig)

row5col1, row5col2, row5col3 = st.columns(3,border=True)
row5col1.plotly_chart(top_10_products_fig)
row5col2.plotly_chart(top_10_products_sold_fig)
row5col3.plotly_chart(Products_sunburst_fig)


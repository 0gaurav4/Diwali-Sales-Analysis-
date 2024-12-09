import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv('DiwaliSalesCleaned.csv')
st.title(":orange[Diwali Sales] :green[Analysis] :blue[Conclusion] 🪔")

# Dataset Summary
st.sidebar.info(f"""
### Dataset Summary Top 3 Insights
- **Top 3 Insights**:
    1. Married Female 26-35: {df[(df['Gender'] == 'F') & (df['Age Group'] == '26-35')].shape[0]}
- 
- **Top 3 States**:
    1. Uttar Pradesh: {df[df['State'] == 'Uttar Pradesh'].shape[0]}
    2. Maharashtra: {df[df['State'] == 'Maharashtra'].shape[0]}
    3. Karnataka: {df[df['State'] == 'Karnataka'].shape[0]}
-
- **Top 3 Occupations**:
    1. IT: {df[df['Occupation'] == 'IT Sector'].shape[0]}
    2. Healthcare: {df[df['Occupation'] == 'Healthcare'].shape[0]}
    3. Aviation: {df[df['Occupation'] == 'Aviation'].shape[0]}
-
- **Top 3 Product Categories**:
    1. Food: {df[df['Product_Category'] == 'Food'].shape[0]}
    2. Clothing: {df[df['Product_Category'] == 'Clothing & Apparel'].shape[0]}
    3. Electronics: {df[df['Product_Category'] == 'Electronics & Gadgets'].shape[0]}
""")



# Calculating the counts for different categories
female_count = df[(df['Gender'] == 'F') & (df['Age Group'] == '26-35')].shape[0]
sales_up = df[df['State'] == 'Uttar Pradesh'].shape[0]
sales_mh = df[df['State'] == 'Maharashtra'].shape[0]
sales_ka = df[df['State'] == 'Karnataka'].shape[0]

# Top 3 occupations
top_3_occupations = df['Occupation'].value_counts().head(3).index.tolist()
amount_count_occupation1 = df[df['Occupation'] == top_3_occupations[0]]['Amount'].count()
amount_count_occupation2 = df[df['Occupation'] == top_3_occupations[1]]['Amount'].count()
amount_count_occupation3 = df[df['Occupation'] == top_3_occupations[2]]['Amount'].count()

# Product category counts
food_count = df[df['Product_Category'] == 'Food'].shape[0]
clothing_count = df[df['Product_Category'] == 'Clothing & Apparel'].shape[0]
electronics_count = df[df['Product_Category'] == 'Electronics & Gadgets'].shape[0]

# Data for bar chart
labels = [
    'Married Female 26-35', 'Sales in Uttar Pradesh', 'Sales in Maharashtra', 'Sales in Karnataka',
    'Working in IT', 'Working in Healthcare', 'Working in Aviation',
    'Product Category - Food', 'Product Category - Clothing & Apparel', 'Product Category - Electronics & Gadgets'
]
sizes = [
    female_count, sales_up, sales_mh, sales_ka, 
    amount_count_occupation1, amount_count_occupation2, amount_count_occupation3, 
    food_count, clothing_count, electronics_count
]

# Create the bar chart using Plotly Express
fig = px.bar(x=labels, y=sizes, title="Data Analysis - Top 3 Insights", 
             labels={'x': 'Insights', 'y': 'Count'}, 
             color=labels)


# Displaying the bar chart in Streamlit
st.plotly_chart(fig)
import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('DiwaliSalesCleaned.csv')
st.title(":orange[Diwali Sales] :green[Analysis] 🪔")

# Sidebar Filters
st.sidebar.header("Filters")

# Filter by Gender

gender_filter = st.sidebar.multiselect(
    'Select Gender', 
    df['Gender'].unique(), 
    
)
if not gender_filter:
    gender_filter = df['Gender'].unique()  # Default to all options
filtered_data = df[df['Gender'].isin(gender_filter)]

# Filter by Age Group
age_group_filter = st.sidebar.multiselect(
    'Select Age Group', 
    filtered_data['Age Group'].sort_values().unique()
)
if not age_group_filter:
    age_group_filter = filtered_data['Age Group'].unique()  # Default to all options
filtered_data = filtered_data[filtered_data['Age Group'].isin(age_group_filter)]

# Filter by Age
age_filter = st.sidebar.multiselect(
    'Select Age', 
    filtered_data['Age'].sort_values().unique()
)
if not age_filter:
    age_filter = filtered_data['Age'].unique()  # Default to all options
filtered_data = filtered_data[filtered_data['Age'].isin(age_filter)]

# Filter by State
state_filter = st.sidebar.multiselect(
    'Select State', 
    filtered_data['State'].sort_values().unique()
)
if not state_filter:
    state_filter = filtered_data['State'].unique()  # Default to all options
filtered_data = filtered_data[filtered_data['State'].isin(state_filter)]

# Filter by Marital Status
marital_status_filter = st.sidebar.multiselect(
    'Select Marital Status', 
    filtered_data['Marital_Status'].unique()
)
if not marital_status_filter:
    marital_status_filter = filtered_data['Marital_Status'].unique()  # Default to all options
filtered_data = filtered_data[filtered_data['Marital_Status'].isin(marital_status_filter)]

# Filter by Product Category
Product_Category_filter = st.sidebar.multiselect(
    'Select Product Category', 
    filtered_data['Product_Category'].sort_values().unique()
)
if not Product_Category_filter:
    Product_Category_filter = filtered_data['Product_Category'].unique()  # Default to all options
filtered_data = filtered_data[filtered_data['Product_Category'].isin(Product_Category_filter)]

# Filter by Occupation
occupation_filter = st.sidebar.multiselect(
    'Select Occupation', 
    filtered_data['Occupation'].sort_values().unique()
)
if not occupation_filter:
    occupation_filter = filtered_data['Occupation'].unique()  # Default to all options
filtered_data = filtered_data[filtered_data['Occupation'].isin(occupation_filter)]



# Display Filtered Dataset
st.success('This is cleaned data with filters applied')
st.write(filtered_data)

# Charts Section
st.write("### Data Visualizations")

import plotly.express as px
import streamlit as st
import pandas as pd

# Assuming df is your DataFrame

# Streamlit Title
st.title('Sales Analysis Dashboard')

# 1. Gender Distribution
st.info(f'Gender Distribution: **{filtered_data["Gender"].value_counts().to_dict()}**')
gender_dist = px.histogram(filtered_data, x='Gender', color='Gender', title="Distribution of Gender")
gender_dist.update_layout(bargap=0.2)
st.plotly_chart(gender_dist)

# 2. Gender vs Total Amount
st.info(f'Total Amount by Gender: **{filtered_data.groupby("Gender")["Amount"].sum().sort_values(ascending=False).to_dict()}**')
sales_gen = filtered_data.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
gender_amount = px.bar(sales_gen, x='Gender', y='Amount', color='Gender', title="Amount & Gender graph")
st.plotly_chart(gender_amount)

# 3. Age Group vs Gender
st.info(f'Age Group Distribution: **{filtered_data["Age Group"].value_counts().to_dict()}**')
age_gender = px.histogram(filtered_data, x='Age Group', color='Gender', title="Age & Gender Distribution")
st.plotly_chart(age_gender)

# 4. Total Amount vs Age Group
st.info(f'Age Group Selected : **{len(filtered_data["Age Group"].value_counts().sort_values(ascending=False).head(10))}**')
sales_age = filtered_data.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
age_amount = px.bar(sales_age, x='Age Group', y='Amount', color='Age Group', title="Age & Amount graph")
st.plotly_chart(age_amount)

# 5. Total Orders from Top 10 States
st.info(f'Total Orders Top **{len(filtered_data["State"].value_counts().sort_values(ascending=False).head(10))}** State')
sales_state_orders = filtered_data.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
state_orders = px.bar(sales_state_orders, x='State', y='Orders', title="Orders & State graph")
st.plotly_chart(state_orders)

# 6. Total Amount/Sales from Top 10 States
st.info(f'Total Amount Top **{len(filtered_data["State"].value_counts().sort_values(ascending=False).head(10))}** State')
sales_state_amount = filtered_data.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
state_amount = px.bar(sales_state_amount, x='State', y='Amount', title="Amount & State graph")
st.plotly_chart(state_amount)

# 7. Marital Status vs Gender (Amount)
st.info(f'Total Amount by Marital Status & Gender: **{filtered_data.groupby(["Marital_Status", "Gender"])["Amount"].sum().sort_values(ascending=False).to_dict()}**')
sales_marital_gender = filtered_data.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
marital_gender_amount = px.bar(sales_marital_gender, x='Marital_Status', y='Amount', color='Gender', title="Marital Status & Gender vs Amount")
st.plotly_chart(marital_gender_amount)

# 8. Total Amount by Occupation
st.info(f'Occupation Selected : **{len(filtered_data["Occupation"].value_counts().sort_values(ascending=False).head(10))}**')
sales_occupation = filtered_data.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
occupation_amount = px.bar(sales_occupation, x='Occupation', y='Amount', title="Amount & Occupation graph")
st.plotly_chart(occupation_amount)

# 9. Total Orders by Product Category
st.info(f'Product Category Selected for Orders : **{len(filtered_data["Product_Category"].value_counts().sort_values(ascending=False).head(10))}**')
sales_product_category_orders = filtered_data.groupby(['Product_Category'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
product_category_orders = px.bar(sales_product_category_orders, x='Product_Category', y='Orders', title="Orders & Product Category graph")
st.plotly_chart(product_category_orders)

# 10. Total Amount by Product Category
st.info(f'Product Category Selected for Amount : **{len(filtered_data["Product_Category"].value_counts().sort_values(ascending=False).head(10))}**')
sales_product_category_amount = filtered_data.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
product_category_amount = px.bar(sales_product_category_amount, x='Product_Category', y='Amount', title="Amount & Product Category graph")
st.plotly_chart(product_category_amount)


# Dynamic Conclusion
dynamic_conclusion = f"""
### :green[Insights From Diwali Sales] 🪔
Based on the applied filters:
- The dataset contains **{filtered_data.shape[0]} records**.
- The total orders are **{filtered_data['Orders'].sum()}**, amounting to ₹**{filtered_data['Amount'].sum():,.2f}**.
- The most common product category is **{filtered_data['Product_Category'].value_counts().idxmax()}**.
- The age group with the highest orders is **{filtered_data.groupby('Age Group')['Orders'].sum().idxmax()}**.
- The Age with the highest sales is **{filtered_data.groupby('Age')['Amount'].sum().idxmax()}**.
- The state with the highest spending is **{filtered_data.groupby('State')['Amount'].sum().idxmax()}**.
- The most popular occupation is **{filtered_data['Occupation'].value_counts().idxmax()}**.
- The most common gender is **{filtered_data['Gender'].value_counts().idxmax()}**.
- Amount and Product Category graph shows that **{filtered_data.groupby('Product_Category')['Amount'].sum().idxmax()}** has the highest sales.
- Orders and Product Category graph shows that **{filtered_data.groupby('Product_Category')['Orders'].sum().idxmax()}** has the highest orders.
"""
st.info(dynamic_conclusion)
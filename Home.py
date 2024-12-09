import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Diwali Sales Analysis 🪔")

st.info("This is Great Indian Diwali sales data analysis.")

st.success("Go to Dashboard page from the sidebar for visualization and Conclusion page for insights.")

st.image("https://res.cloudinary.com/dgwuwwqom/image/upload/v1716891083/Github/project%20photos/Diwali%20sales%20analysis.jpg" , width=500)


df = pd.read_csv("Diwali Sales Data.csv",encoding='latin1')

st.info("**Raw Dataset**")
st.dataframe(df)


# Dataset Summary
st.success(f"""
### Dataset Summary
- **Total Records**: {df.shape[0]}
- **Total Columns**: {df.shape[1]}

""")
st.warning(f"""
- Total Products: {df['Product_ID'].nunique()}
- {df['Product_Category'].unique()}
            """)




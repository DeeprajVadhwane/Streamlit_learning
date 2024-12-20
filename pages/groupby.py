import streamlit as st
import pandas as pd

# Load dataset
st.title("GroupBy in Streamlit Example")
st.write("This app demonstrates how to use pandas `groupby` in a Streamlit app.")

# Upload file or load default data
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    # Default data
    df = pd.read_csv('map_trans.csv')
# Show the data
st.subheader("Dataset")
st.dataframe(df)



# year_groupby = df.groupby('Year')['Transaction_amount'].sum().reset_index()

# # st.write(year_groupby)
# # st.dataframe(year_groupby)
# # st.table(year_groupby)

# st.sidebar.header("Filter Options")

# group_column = st.selectbox("Select a column to group by:", options=df.columns)
# agg_column = st.selectbox("Select a column to aggregate:", options=df.columns)

# # # # Aggregation method
# aggregation = st.selectbox("Select an aggregation method:", ["sum", "mean", "count"])

# # # Perform GroupBy
# if st.button("Group Data"):
#     if aggregation == "sum":
#         grouped_data = df.groupby(group_column)[agg_column].sum().reset_index()
#         st.dataframe(grouped_data)

        
#     elif aggregation == "mean":
#         grouped_data = df.groupby(group_column)[agg_column].mean().reset_index()
#     elif aggregation == "count":
#         grouped_data = df.groupby(group_column)[agg_column].count().reset_index()

#     # Display grouped data
#     st.subheader("Grouped Data")
#     st.dataframe(grouped_data)

state_filter = st.sidebar.multiselect('Select State(s)', options=df['State'].unique(), default=df['State'].unique())
st.write(state_filter)
year_filter = st.sidebar.slider('Select Year Range', ()), int(df['Year'].int(df['Year'].minmax()), (2020, 2021))

df_filtered = df[(df['State'].isin(state_filter)) & (df['Year'] >= year_filter[0]) & (df['Year'] <= year_filter[1])]
group_column = st.selectbox("Select a column to group by:", options=data.columns)

# GroupBy options
group_column = st.selectbox("Select a column to group by:", options=data.columns)
agg_column = st.selectbox("Select a column to aggregate:", options=data.columns)





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv("map_trans.csv")
    return data

data = load_data()
st.dataframe(data, use_container_width=True)

# Set up the Streamlit app
st.title("Visualization Dashboard with Code and Plots")
st.write("This app displays the code first followed by the visualization to help you learn and teach plotting in Python.")

# Sidebar for navigation
plot_type = st.sidebar.selectbox("Select Plot Type", ["Univariate", "Bivariate"])

# Function to display code and plot
def display_code_and_plot(code, plot_func):
    st.subheader("Code:")
    st.code(code, language='python')
    st.subheader("Visualization:")
    plot_func()

# Univariate Plots
if plot_type == "Univariate":
    library = st.sidebar.selectbox("Select Library", ["Pandas", "Matplotlib", "Seaborn", "Plotly"])
    data_type = st.sidebar.selectbox("Select Data Type", ["Numeric", "Discrete"])

    st.header(f"Univariate Plots with {library}")

    if data_type == 'Numeric':
        column = st.selectbox("Select Column for Univariate Analysis", data.select_dtypes(include=['number']).columns)
        
        if library == "Pandas":
            code = f"""
fig, ax = plt.subplots()
data['{column}'].hist(ax=ax, grid=False, bins=20, edgecolor='black')
ax.set_title('Histogram of {column}')
ax.set_xlabel('{column}')
ax.set_ylabel('Frequency')
st.pyplot(fig)
"""

            def plot_func():
                fig, ax = plt.subplots()
                data[column].hist(ax=ax, grid=False, bins=20, edgecolor='black')
                ax.set_title(f'Histogram of {column}')
                ax.set_xlabel(f'{column}')
                ax.set_ylabel('Frequency')
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Matplotlib":
            code = f"""
fig, ax = plt.subplots()
ax.hist(data['{column}'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('Histogram of {column}')
ax.set_xlabel('{column}')
ax.set_ylabel('Frequency')
st.pyplot(fig)
"""
            def plot_func():
                fig, ax = plt.subplots()
                ax.hist(data[column], bins=20, color='skyblue', edgecolor='black')
                ax.set_title(f"Histogram of {column}")
                ax.set_xlabel(column)
                ax.set_ylabel("Frequency")
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Seaborn":
            code = f"""
fig, ax = plt.subplots()
sns.histplot(data['{column}'], kde=True, ax=ax)
ax.set_title('Histogram and KDE of {column}')
st.pyplot(fig)
"""
            def plot_func():
                fig, ax = plt.subplots()
                sns.histplot(data[column], kde=True, ax=ax)
                ax.set_title(f"Histogram and KDE of {column}")
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Plotly":
            code = f"""
fig = px.histogram(data, x='{column}', nbins=20, title='Histogram of {column}')
st.plotly_chart(fig)
"""
            def plot_func():
                fig = px.histogram(data, x=column, nbins=20, title=f"Histogram of {column}")
                st.plotly_chart(fig)
            display_code_and_plot(code, plot_func)

    else:
        column = st.selectbox("Select Column for Univariate Analysis", data.select_dtypes(include=['object']).columns)
        
        if library == "Pandas":
            code = f"""
fig, ax = plt.subplots()
data['{column}'].value_counts().plot(kind='bar', ax=ax)
ax.set_title('Frequency Count of {column}')
ax.set_xlabel('{column}')
ax.set_ylabel('Count')
st.pyplot(fig)
"""
            def plot_func():
                fig, ax = plt.subplots()
                data[column].value_counts().plot(kind='bar', ax=ax)
                ax.set_title(f"Frequency Count of {column}")
                ax.set_xlabel(column)
                ax.set_ylabel("Count")
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Matplotlib":
            code = f"""
fig, ax = plt.subplots()
sizes = data['{column}'].value_counts()
ax.bar(sizes.index, sizes.values, color='skyblue', edgecolor='black')
ax.set_title('Frequency Count of {column}')
ax.set_xlabel('{column}')
ax.set_ylabel('Count')
plt.xticks(rotation=45)
st.pyplot(fig)
"""
            def plot_func():
                fig, ax = plt.subplots()
                sizes = data[column].value_counts()
                ax.bar(sizes.index, sizes.values, color='skyblue', edgecolor='black')
                ax.set_title(f"Frequency Count of {column}")
                ax.set_xlabel(column)
                ax.set_ylabel("Count")
                plt.xticks(rotation=45)
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Seaborn":
            code = f"""
fig, ax = plt.subplots()
sns.countplot(x=data['{column}'], ax=ax)
ax.set_title('Count Plot of {column}')
ax.set_xlabel('{column}')
st.pyplot(fig)
"""
            def plot_func():
                fig, ax = plt.subplots()
                sns.countplot(x=data[column], ax=ax)
                ax.set_title(f"Count Plot of {column}")
                ax.set_xlabel(column)
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Plotly":
            code = f"""
fig = px.bar(data, x='{column}', title='Frequency Count of {column}')
st.plotly_chart(fig)
"""
            def plot_func():
                fig = px.bar(data, x=column, title=f"Frequency Count of {column}")
                st.plotly_chart(fig)
            display_code_and_plot(code, plot_func)

# Bivariate Plots
if plot_type == "Bivariate":
    plot_types = st.sidebar.selectbox("Select Plot Type", ["Numerical vs Numerical", "Categorical vs Numerical", "Categorical vs Categorical"])
    library = st.sidebar.selectbox("Select Library", ["Matplotlib", "Seaborn", "Plotly"])

    if plot_types == "Numerical vs Numerical":
        st.header(f"Numerical vs Numerical Plots with {library}")
        x_col = st.selectbox("Select X-Axis Column", data.select_dtypes(include=['number']).columns)
        y_col = st.selectbox("Select Y-Axis Column", data.select_dtypes(include=['number']).columns)
        
        if library == "Matplotlib":
            code = f"""
fig, ax = plt.subplots()
ax.scatter(data['{x_col}'], data['{y_col}'], color='skyblue')
ax.set_title('Scatter Plot of {x_col} vs {y_col}')
ax.set_xlabel('{x_col}')
ax.set_ylabel('{y_col}')
st.pyplot(fig)
"""
            def plot_func():
                fig, ax = plt.subplots()
                ax.scatter(data[x_col], data[y_col], color='skyblue')
                ax.set_title(f'Scatter Plot of {x_col} vs {y_col}')
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Seaborn":
            code = f"""
fig, ax = plt.subplots()
sns.scatterplot(x=data['{x_col}'], y=data['{y_col}'], ax=ax)
ax.set_title('Scatter Plot of {x_col} vs {y_col}')
st.pyplot(fig)
"""
            def plot_func():
                fig, ax = plt.subplots()
                sns.scatterplot(x=data[x_col], y=data[y_col], ax=ax)
                ax.set_title(f'Scatter Plot of {x_col} vs {y_col}')
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Plotly":
            code = f"""
fig = px.scatter(data, x='{x_col}', y='{y_col}', title='Scatter Plot of {x_col} vs {y_col}')
st.plotly_chart(fig)
"""
            def plot_func():
                fig = px.scatter(data, x=x_col, y=y_col, title=f'Scatter Plot of {x_col} vs {y_col}')
                st.plotly_chart(fig)
            display_code_and_plot(code, plot_func)

    elif plot_types == "Categorical vs Numerical":
        st.header(f"Categorical vs Numerical Plots with {library}")
        cat_col = st.selectbox("Select Categorical Column", data.select_dtypes(include=['object', 'category']).columns)
        num_col = st.selectbox("Select Numerical Column", data.select_dtypes(include=['number']).columns)
        
        if library == "Matplotlib":
            code = f"""
fig, ax = plt.subplots()
data.groupby('{cat_col}')[{num_col}].mean().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
ax.set_title('Mean {num_col} by {cat_col}')
ax.set_xlabel('{cat_col}')
ax.set_ylabel('Mean {num_col}')
st.pyplot(fig)
"""
            def plot_func():
                fig, ax = plt.subplots()
                data.groupby(cat_col)[num_col].mean().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
                ax.set_title(f'Mean {num_col} by {cat_col}')
                ax.set_xlabel(cat_col)
                ax.set_ylabel(f'Mean {num_col}')
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Seaborn":
            code = f"""
fig, ax = plt.subplots()
sns.barplot(x='{cat_col}', y='{num_col}', data=data, ax=ax)
ax.set_title('Bar Plot of {num_col} by {cat_col}')
st.pyplot(fig)
"""
            def plot_func():
                fig, ax = plt.subplots()
                sns.barplot(x=cat_col, y=num_col, data=data, ax=ax)
                ax.set_title(f'Bar Plot of {num_col} by {cat_col}')
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Plotly":
            code = f"""
fig = px.bar(data, x='{cat_col}', y='{num_col}', title='Bar Plot of {num_col} by {cat_col}')
st.plotly_chart(fig)
"""
            def plot_func():
                fig = px.bar(data, x=cat_col, y=num_col, title=f'Bar Plot of {num_col} by {cat_col}')
                st.plotly_chart(fig)
            display_code_and_plot(code, plot_func)

    elif plot_types == "Categorical vs Categorical":
        st.header(f"Categorical vs Categorical Plots with {library}")
        cat_col1 = st.selectbox("Select First Categorical Column", data.select_dtypes(include=['object', 'category']).columns)
        cat_col2 = st.selectbox("Select Second Categorical Column", data.select_dtypes(include=['object', 'category']).columns)
        
        if library == "Matplotlib":
            code = f"""
                cross_tab = pd.crosstab(data['{cat_col1}'], data['{cat_col2}'])
                fig, ax = plt.subplots()
                cross_tab.plot(kind='bar', ax=ax, stacked=True)
                ax.set_title('Stacked Bar Plot of {cat_col1} vs {cat_col2}')
                ax.set_xlabel('{cat_col1}')
                ax.set_ylabel('Count')
                st.pyplot(fig)
                """
            def plot_func():
                cross_tab = pd.crosstab(data[cat_col1], data[cat_col2])
                fig, ax = plt.subplots()
                cross_tab.plot(kind='bar', ax=ax, stacked=True)
                ax.set_title(f'Stacked Bar Plot of {cat_col1} vs {cat_col2}')
                ax.set_xlabel(cat_col1)
                ax.set_ylabel('Count')
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Seaborn":
            code = f"""
            fig, ax = plt.subplots()
            sns.heatmap(pd.crosstab(data['{cat_col1}'], data['{cat_col2}']), annot=True, fmt='d', cmap='Blues', ax=ax)
            ax.set_title('Heatmap of {cat_col1} vs {cat_col2}')
            st.pyplot(fig)
            """
            def plot_func():
                fig, ax = plt.subplots()
                sns.heatmap(pd.crosstab(data[cat_col1], data[cat_col2]), annot=True, fmt='d', cmap='Blues', ax=ax)
                ax.set_title(f'Heatmap of {cat_col1} vs {cat_col2}')
                st.pyplot(fig)
            display_code_and_plot(code, plot_func)

        elif library == "Plotly":
            code = f"""
                fig = px.histogram(data, x='{cat_col1}', color='{cat_col2}', barmode='stack', title='Stacked Bar Plot of {cat_col1} vs {cat_col2}')
                st.plotly_chart(fig)
                """
            def plot_func():
                fig = px.histogram(data, x=cat_col1, color=cat_col2, barmode='stack', title=f'Stacked Bar Plot of {cat_col1} vs {cat_col2}')
                st.plotly_chart(fig)
            display_code_and_plot(code, plot_func)

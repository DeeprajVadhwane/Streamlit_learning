import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib as plt
# title
# pip install streamlit

st.title("Welcome to Streamlit sessions")

# Title of the App
st.title("What is Streamlit?")

# Introduction to Streamlit
st.header("Introduction")
st.write("""
Streamlit is an open-source Python library that allows you to quickly build and share data applications 
and interactive web dashboards. It is designed to make the creation of web apps easy for data analysis 
and Data scientists without requiring extensive web development knowledge.
""")

# Key Features
st.header("Key Features of Streamlit")

st.subheader("1. Simplicity")
st.write("""
- Streamlit turns Python scripts into web apps by adding a few Streamlit commands.
- It’s easy to use; you don’t need HTML, CSS, or JavaScript to create interactive applications.
""")

st.subheader("2. Interactive Widgets")
st.write("""
- Streamlit provides a wide range of widgets such as sliders, buttons, text inputs, and select boxes, 
  which allow users to interact with the data and visualizations in real-time.
""")
# Example of a Widget
user_input = st.text_input("Try typing your name:")
if user_input:
    st.write(f"Hello, {user_input}!")

st.subheader("3. Real-time Data Updates")
st.write("""
- As you tweak your Python code, the app automatically updates, allowing for quick iteration and development.
- Streamlit retuns the script from top to bottom whenever the user interacts with the app, ensuring that the app 
  always reflects the latest data and logic.
""")

st.subheader("4. Data Visualization Integration")
st.write("""
- Streamlit seamlessly integrates with popular data visualization libraries such as Matplotlib, Seaborn, Plotly, and Altair.
- You can easily create charts, plots, and maps and display them directly in the app.
""")
# Example of a Simple Plot
import matplotlib.pyplot as plt
import numpy as np

st.write("Example of a Plot:")
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

st.subheader("5. Deployment")
st.write("""
- Streamlit apps can be deployed quickly using Streamlit Cloud or other cloud services.
- Deployment is simple, and once deployed, your app can be shared with others via a URL.
""")

st.subheader("6. Caching for Performance")
st.write("""
- Streamlit includes caching mechanisms to speed up apps by avoiding redundant computations, 
  making your app faster and more efficient.
""")
@st.cache
def expensive_computation(x):
    return x * 2

st.write("Cached computation example (computing 2 * 10):", expensive_computation(10))

# Why Use Streamlit
st.header("Why Use Streamlit?")
st.write("""
- **Ease of Use**: Ideal for data analyst and data scientist who want to build web apps without getting into 
  the complexities of web development.
- **Rapid Prototyping**: Allows for quick iteration and prototyping of data-driven apps.
- **Community and Ecosystem**: It has a growing community and a rich ecosystem of tutorials, plugins, and extensions.
""")

# Example Use Cases
st.header("Example Use Cases")
st.write("""
- **Data Exploration**: Building interactive dashboards to explore datasets.
- **Machine Learning**: Creating apps to visualize model predictions and performance.
- **Prototyping**: Quickly developing prototypes of web apps to test ideas or present to stakeholders.
""")

# Summary
st.write("""
Streamlit is a powerful tool for anyone looking to turn their Python scripts into interactive, 
shareable web applications with minimal effort.
""")

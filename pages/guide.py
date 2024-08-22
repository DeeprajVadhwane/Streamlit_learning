import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Title of the App
st.title("Comprehensive Guide to Streamlit")

# Introduction
st.header("Introduction to Streamlit")
st.write("""
Streamlit is an open-source Python library that allows you to build interactive web applications quickly and easily. 
It's particularly popular among data scientists for creating data-driven dashboards without needing to know web development.
""")

# Installation
st.subheader("Installation")
st.code("pip install streamlit", language="bash")

# Running a Streamlit App
st.subheader("Running a Streamlit App")
st.write("To run a Streamlit app, use the following command:")
st.code("streamlit run your_script.py", language="bash")

# Basic Streamlit App Structure
st.header("Basic Streamlit App Structure")
st.write("A basic Streamlit app might look like this:")
basic_code = """
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, welcome to Streamlit!")
"""
st.code(basic_code, language="python")

# Widgets in Streamlit
st.header("Widgets in Streamlit")
st.write("""
Streamlit provides a variety of widgets to create interactive applications. Here are some examples:
""")

# Text Inputs and Outputs
st.subheader("Text Inputs and Outputs")
st.write("Streamlit provides text input widgets that allow users to enter and display text data.")

# st.text_input()
text_input_code = """
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")
"""
st.code(text_input_code, language="python")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# st.text_area()
text_area_code = """
bio = st.text_area("Enter a short bio:")
st.write(f"Your bio: {bio}")
"""
st.code(text_area_code, language="python")
bio = st.text_area("Enter a short bio:")
if bio:
    st.write(f"Your bio: {bio}")

# Buttons and Interactivity
st.subheader("Buttons and Interactivity")
st.write("You can add interactivity to your app using buttons, radio buttons, and select boxes.")

# st.button()
button_code = """
if st.button('Click me'):
    st.write('Button clicked!')
else:
    st.write('Button not clicked yet.')
"""
st.code(button_code, language="python")
if st.button('Click me'):
    st.write('Button clicked!')
else:
    st.write('Button not clicked yet.')

# st.radio()
radio_code = """
option = st.radio("Choose your favorite color:", ["Red", "Green", "Blue"])
st.write(f"You selected: {option}")
"""
st.code(radio_code, language="python")
option = st.radio("Choose your favorite color:", ["Red", "Green", "Blue"])
st.write(f"You selected: {option}")

# st.selectbox()
selectbox_code = """
option = st.selectbox("Pick a fruit:", ["Apple", "Banana", "Cherry"])
st.write(f"You picked: {option}")
"""
st.code(selectbox_code, language="python")
option = st.selectbox("Pick a fruit:", ["Apple", "Banana", "Cherry"])
st.write(f"You picked: {option}")

# Sliders and Number Inputs
st.subheader("Sliders and Number Inputs")
st.write("Streamlit provides sliders and number inputs to select numerical values.")

# st.slider()
slider_code = """
age = st.slider('Select your age:', 0, 100, 25)
st.write(f'Your age is {age}.')
"""
st.code(slider_code, language="python")
age = st.slider('Select your age:', 0, 100, 25)
st.write(f'Your age is {age}.')

# st.number_input()
number_input_code = """
number = st.number_input('Insert a number:', min_value=0, max_value=100, value=50)
st.write(f'The number you entered is {number}.')
"""
st.code(number_input_code, language="python")
number = st.number_input('Insert a number:', min_value=0, max_value=100, value=50)
st.write(f'The number you entered is {number}.')

# Displaying Data
st.header("Displaying Data in Streamlit")
st.write("You can easily display data in tables, charts, and more.")

# DataFrame
st.subheader("1. DataFrame")
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
st.write("You can display DataFrames like this:")
st.code("""
st.write(df)
""", language="python")
st.write(df)

# Plotting with Matplotlib
st.subheader("2. Plotting with Matplotlib")
plot_code = """
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
"""
st.code(plot_code, language="python")
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# Plotting with Seaborn
st.subheader("3. Plotting with Seaborn")
seaborn_code = """
sns.set(style="darkgrid")
iris = sns.load_dataset('iris')
fig, ax = plt.subplots()
sns.histplot(iris['species'], kde=False, ax=ax)
st.pyplot(fig)
"""
st.code(seaborn_code, language="python")
sns.set(style="darkgrid")
iris = sns.load_dataset('iris')
fig, ax = plt.subplots()
sns.histplot(iris['species'], kde=False, ax=ax)
st.pyplot(fig)

# Layouts in Streamlit
st.header("Layouts in Streamlit")
st.write("Streamlit offers various ways to organize the layout of your app.")

# Columns
st.subheader("1. Columns")
columns_code = """
col1, col2 = st.columns(2)

with col1:
    st.write("This is column 1")
with col2:
    st.write("This is column 2")
"""
st.code(columns_code, language="python")
col1, col2 = st.columns(2)

with col1:
    st.write("This is column 1")
with col2:
    st.write("This is column 2")

# Sidebar
st.subheader("2. Sidebar")
sidebar_code = """
st.sidebar.title("Sidebar Title")
selected_option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected {selected_option}")
"""
st.code(sidebar_code, language="python")
st.sidebar.title("Sidebar Title")
selected_option = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected {selected_option}")

# Caching in Streamlit
st.header("Caching in Streamlit")
st.write("""
Streamlit provides caching to improve the performance of your app by storing the results of expensive computations.
""")
caching_code = """
@st.cache
def expensive_computation(x):
    return x * 2

result = expensive_computation(10)
st.write(f"Result of expensive computation: {result}")
"""
st.code(caching_code, language="python")
@st.cache
def expensive_computation(x):
    return x * 2

result = expensive_computation(10)
st.write(f"Result of expensive computation: {result}")

# Advanced Features
st.header("Advanced Features")

# Custom Themes
st.subheader("1. Custom Themes")
st.write("""
You can customize the appearance of your Streamlit app by modifying the `.streamlit/config.toml` file.
Here's an example configuration:
""")
st.code("""
[theme]
primaryColor = "#F39C12"
backgroundColor = "#2E4053"
secondaryBackgroundColor = "#1C2833"
textColor = "#EAECEE"
font = "sans serif"
""", language="toml")

# Session State
st.subheader("2. Session State")
st.write("""
Streamlit's session state allows you to store information that persists across user interactions.
""")
session_state_code = """
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write(f'Count: {st.session_state.count}')
"""
st.code(session_state_code, language="python")
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write(f'Count: {st.session_state.count}')

# Conclusion
st.header("Conclusion")
st.write("""
This comprehensive guide has covered the basics of Streamlit, including its widgets, layout options, 
data display methods, and advanced features like caching and session state. 
Streamlit is a powerful tool for quickly building interactive and data-driven web applications.
""")

st.write("Happy Streamlit-ing!")

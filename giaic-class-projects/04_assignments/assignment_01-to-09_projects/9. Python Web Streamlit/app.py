import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="My Streamlit Website", page_icon="🚀")
st.title("Welcome to My First Streamlit Website! 🌍")

st.header("A Simple Data Science Portfolio Website")
st.write("""
This is a basic Streamlit website demonstrating various features:
- Text elements
- Interactive widgets
- Data visualization
- Layout organization
""")

st.divider()

with st.sidebar:
    st.header("Configuration ⚙️")
    user_name = st.text_input("Enter your name")
    age = st.slider("Select your age", 0, 100, 25)
    favorite_color = st.selectbox(
        "Choose your favorite color",
        ("Red", "Green", "Blue", "Yellow")
    )

col1, col2 = st.columns(2)

with col1:
    st.subheader("Interactive Demo")
    if st.button("Click me!"):
        st.success(f"Hello {user_name}! You clicked the button!")
    st.write(f"""
    Selected Parameters:
    - Name: {user_name}
    - Age: {age}
    - Favorite Color: {favorite_color}
    """)

with col2:
    st.subheader("Data Visualization")
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    st.line_chart(chart_data)

st.divider()
st.subheader("Geographical Visualization")
map_data = pd.DataFrame({
    'lat': [37.76, 37.77, 37.78],
    'lon': [-122.4, -122.41, -122.42]
})
st.map(map_data)

with st.expander("Show Explanation"):
    st.write("""
    This website demonstrates various Streamlit features:
    - Interactive widgets in the sidebar
    - Column-based layout
    - Real-time data visualization
    - Map integration
    - Expandable sections
    """)
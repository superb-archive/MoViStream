import streamlit as st
import pandas as pd
import plotly.express as px

# set page layout
st.set_page_config(
    page_title="Streamlit Map",
    page_icon="🚘",
    # layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Streamlit Map")

st.sidebar.subheader("weather")
weather_sunny = st.sidebar.checkbox("sunny")
weather_rainiy = st.sidebar.checkbox("rainy")
weather_foggy = st.sidebar.checkbox("foggy")

# data
df = pd.DataFrame(
    {
        "latitude": [37.77, 37.77, 37.77, 37.77],
        "longitude": [
            -122.42,
            -122.42,
            -122.42,
            -122.42,
        ],
        "weather": ["sunny", "rainy", "foggy", "sunny"],
        "cateogry": ["car", "car", "turck", "human"],
        "count": [1, 2, 3, 4],
    }
)

# Plot the GPS coordinates on the map
st.map(df)

st.subheader("label info")
if weather_sunny:
    condition = df["weather"] == "sunny"
    df = df[condition]
if weather_foggy:
    condition = df["weather"] == "foggy"
    df = df[condition]
if weather_rainiy:
    condition = df["weather"] == "rainy"
    df = df[condition]

fig = px.pie(df, values="count", names="cateogry")
st.write(fig)

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

sample_datas = [
    {
        "header": {
            "queryId": "query_1655548648091",
            "schema": "`CATEGORY` STRING KEY, `TOTAL` BIGINT",
        }
    },
    {"row": {"columns": ["a", 0]}},
    {"row": {"columns": ["b", 0]}},
    {"row": {"columns": ["bike", 67]}},
    {"row": {"columns": ["bus", 93]}},
    {"row": {"columns": ["c", 0]}},
    {"row": {"columns": ["car", 85]}},
    {"row": {"columns": ["d", 0]}},
    {"row": {"columns": ["drivable area", 96]}},
    {"row": {"columns": ["e", 0]}},
    {"row": {"columns": ["lane", 72]}},
    {"row": {"columns": ["motor", 77]}},
    {"row": {"columns": ["person", 91]}},
    {"row": {"columns": ["rider", 85]}},
    {"row": {"columns": ["traffic light", 86]}},
    {"row": {"columns": ["traffic sign", 88]}},
    {"row": {"columns": ["train", 81]}},
    {"row": {"columns": ["truck", 79]}},
]


df = pd.DataFrame()
for data in sample_datas:
    if data.get("row"):
        row = data["row"]["columns"]
        df = df.append(
            pd.DataFrame([row], columns=["category", "total"]),
            ignore_index=True,
        )
# set page layout
st.set_page_config(
    page_title="Streamlit Map",
    page_icon="🚘",
    # layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Streamlit Map")

# st.sidebar.subheader("weather")
# weather_sunny = st.sidebar.checkbox("sunny", value=True)
# weather_rainiy = st.sidebar.checkbox("rainy", value=True)
# weather_foggy = st.sidebar.checkbox("foggy", value=True)

# # Plot the GPS coordinates on the map
# # st.map(df)

# st.subheader("label info")
# if weather_sunny:
#     condition = df["weather"] == "partly cloudy"
# if weather_foggy:
#     condition = df["weather"] == "foggy"
# if weather_rainiy:
#     condition = df["weather"] == "rainy"
# df = df[condition]


fig = px.pie(df, values="total", names="category")
st.write(fig)

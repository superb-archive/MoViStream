import time
import warnings

from labels import (
    get_category_index,
    get_gps_index,
    get_scene_index,
    get_timeofday_index,
    get_weather_index,
)

warnings.simplefilter(action="ignore", category=FutureWarning)

import pandas as pd
import plotly.express as px

import streamlit as st

# set page layout
st.set_page_config(
    page_title="Autonomous Vehicle Intelligence",
    page_icon="🚘",
    # layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Autonomous Vehicle Intelligence")

# set sidebar
# set selectbox for choose data
st.sidebar.subheader("Select a filter")
kind_of_data = st.sidebar.selectbox(
    "",
    ["category", "weather", "scene", "timeofday"],
    index=0,
)
print(kind_of_data)
# draw map
map_df = pd.DataFrame()
print(len(get_gps_index()))
for data in get_gps_index():
    if data.get("row"):
        row = data["row"]["columns"]
        map_df = map_df.append(
            pd.DataFrame([row], columns=["longitude", "latitude"]),
            ignore_index=True,
        )
st.map(map_df)


# draw pie chart
placeholder = st.empty()
with placeholder.container():
    if kind_of_data == "category":
        category_df = pd.DataFrame()
        for data in get_category_index():
            if data.get("row"):
                row = data["row"]["columns"]
                category_df = category_df.append(
                    pd.DataFrame([row], columns=["category", "total"]),
                    ignore_index=True,
                )
        fig = px.pie(category_df, values="total", names="category")
    elif kind_of_data == "weather":
        weather_df = pd.DataFrame()
        for data in get_weather_index():
            if data.get("row"):
                row = data["row"]["columns"]
                weather_df = weather_df.append(
                    pd.DataFrame([row], columns=["weather", "total"]),
                    ignore_index=True,
                )
        fig = px.pie(weather_df, values="total", names="weather")
    elif kind_of_data == "scene":
        scene_df = pd.DataFrame()
        for data in get_scene_index():
            if data.get("row"):
                row = data["row"]["columns"]
                scene_df = scene_df.append(
                    pd.DataFrame([row], columns=["scene", "total"]),
                    ignore_index=True,
                )
        fig = px.pie(scene_df, values="total", names="scene")
    elif kind_of_data == "timeofday":
        timeofday_df = pd.DataFrame()
        for data in get_timeofday_index():
            if data.get("row"):
                row = data["row"]["columns"]
                timeofday_df = timeofday_df.append(
                    pd.DataFrame([row], columns=["timeofday", "total"]),
                    ignore_index=True,
                )
        fig = px.pie(timeofday_df, values="total", names="timeofday")

    st.plotly_chart(fig)

time.sleep(5)

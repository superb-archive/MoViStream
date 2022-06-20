import time
import warnings

from labels import (
    get_category_index,
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
    page_title="Streamlit App",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.title("Streamlit App")

if "real_time" not in st.session_state:
    st.session_state["real_time"] = True


def switch_realtime():
    st.session_state["real_time"] = not st.session_state["real_time"]


st.button("Real Time / Stop", on_click=switch_realtime)


placeholder = st.empty()


while "real_time" in st.session_state and st.session_state["real_time"]:
    with placeholder.container():
        category_df = pd.DataFrame()
        for data in get_category_index():
            if data.get("row"):
                row = data["row"]["columns"]
                category_df = category_df.append(
                    pd.DataFrame([row], columns=["category", "total"]),
                    ignore_index=True,
                )
        category_fig = px.pie(category_df, values="total", names="category")

        weather_df = pd.DataFrame()
        for data in get_weather_index():
            if data.get("row"):
                row = data["row"]["columns"]
                weather_df = weather_df.append(
                    pd.DataFrame([row], columns=["weather", "total"]),
                    ignore_index=True,
                )
        weather_fig = px.pie(weather_df, values="total", names="weather")

        scene_df = pd.DataFrame()
        for data in get_scene_index():
            if data.get("row"):
                row = data["row"]["columns"]
                scene_df = scene_df.append(
                    pd.DataFrame([row], columns=["scene", "total"]),
                    ignore_index=True,
                )
        scene_fig = px.pie(scene_df, values="total", names="scene")

        timeofday_df = pd.DataFrame()
        for data in get_timeofday_index():
            if data.get("row"):
                row = data["row"]["columns"]
                timeofday_df = timeofday_df.append(
                    pd.DataFrame([row], columns=["timeofday", "total"]),
                    ignore_index=True,
                )
        timeofday_fig = px.pie(timeofday_df, values="total", names="timeofday")

        fig_col1, fig_col2 = st.columns(2)

        with fig_col1:
            st.plotly_chart(category_fig, use_container_width=True)
            st.plotly_chart(scene_fig, use_container_width=True)

        with fig_col2:
            st.plotly_chart(weather_fig, use_container_width=True)
            st.plotly_chart(timeofday_fig, use_container_width=True)

    time.sleep(1)

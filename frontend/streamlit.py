import warnings

import pandas as pd
import plotly.express as px
import pydeck as pdk
from streamlit_autorefresh import st_autorefresh

import streamlit as st
from labels import (
    get_category_index,
    get_gps_index,
    get_scene_index,
    get_timeofday_index,
    get_weather_index,
)

warnings.simplefilter(action="ignore", category=FutureWarning)


st.title("Autonomous Vehicle Intelligence")

# ========================== SIDEBAR ==========================

st.sidebar.header("Configurations")
st.sidebar.subheader("General")
# refresh interval
is_live_mode = st.sidebar.checkbox("live mode", False)
if is_live_mode:
    refresh_interval = 3
else:
    refresh_interval = st.sidebar.number_input(
        "refresh interval (seconds)", 1, None, 10
    )
# st.set_page_config(
#     page_title="Autonomous Vehicle Intelligence",
#     page_icon="🚘",
#     # layout="wide",
#     initial_sidebar_state="expanded",
# )
st_autorefresh(interval=refresh_interval * 1000, limit=100, key="autorefresh_key")

st.sidebar.subheader("Map")
# locations
region = st.sidebar.selectbox(
    "filter gps to",
    ["US West", "US East", "Israel"],
    index=0,
)
init_location = {
    "US West": {"lat": 37.4275, "lon": -122.168861},
    "US East": {"lat": 40.7128, "lon": -74.0060},
    "Israel": {"lat": 31.0461, "lon": 34.8516},
}
dot_radius = st.sidebar.number_input("dot radius", 10, 1000, 500)

st.sidebar.subheader("Labels")
# labels
label_filter = st.sidebar.selectbox(
    "filter labels by",
    ["category", "weather", "scene", "timeofday"],
    index=0,
)
# ========================== SIDEBAR ==========================

col1, col2 = st.columns([1, 1])
# ============================ MAP ============================

with col1:
    map_df = pd.DataFrame()
    for data in get_gps_index():
        if data.get("row"):
            row = data["row"]["columns"]
            map_df = map_df.append(
                pd.DataFrame([row], columns=["lon", "lat"]),
                ignore_index=True,
            )
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(
                latitude=init_location[region]["lat"],
                longitude=init_location[region]["lon"],
                zoom=12,
            ),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=map_df,
                    get_position="[lon, lat]",
                    get_color="[200, 30, 0, 160]",
                    get_radius=dot_radius,
                ),
            ],
        )
    )
# ============================ MAP ============================


# ========================= PIE CHART =========================
with col2:
    placeholder = st.empty()
    with placeholder.container():
        label_distribution = pd.DataFrame()

        if label_filter == "category":
            data_table = get_category_index()
        elif label_filter == "weather":
            data_table = get_weather_index()
        elif label_filter == "scene":
            data_table = get_scene_index()
        elif label_filter == "timeofday":
            data_table = get_timeofday_index()
        for data in data_table:
            if data.get("row"):
                row = data["row"]["columns"]
                label_distribution = label_distribution.append(
                    pd.DataFrame([row], columns=[label_filter, "total"]),
                    ignore_index=True,
                )
        fig = px.pie(label_distribution, values="total", names=label_filter)

        st.plotly_chart(fig)
# ========================= PIE CHART =========================

import warnings

import pandas as pd
import plotly.express as px
import pydeck as pdk
from streamlit_autorefresh import st_autorefresh

import streamlit as st
from apis import (
    get_accelerometer_index,
    get_category_index,
    get_gps_index,
    get_random_10_vehicles,
    get_scene_index,
    get_timeofday_index,
    get_weather_index,
)

warnings.simplefilter(action="ignore", category=FutureWarning)


st.title("MoViStream")
st.subheader("Autonomous Vehicle Intelligence Platform")

# ========================== SIDEBAR ==========================

st.sidebar.header("Configurations")
st.sidebar.subheader("General")

# random_tracking_mode
random_vehicles = get_random_10_vehicles()
vehicle_list = [
    None,
]
for data in random_vehicles:
    if data.get("row"):
        row = data["row"]["columns"]
        vehicle, label_count = row
        vehicle_list.append(vehicle)
vehicle_to_track = st.sidebar.selectbox("track a random vehicle", vehicle_list, index=0)
if vehicle_to_track is None:
    filter_query = ""
else:
    filter_query = f" where image_id = '{vehicle_to_track}'"

# refresh interval
if vehicle_to_track is None:
    refresh_interval = st.sidebar.number_input(
        "refresh interval (seconds)", 3, None, 10
    )
else:
    refresh_interval = 3
# st.set_page_config(
#     page_title="Autonomous Vehicle Intelligence",
#     page_icon="🚘",
#     # layout="wide",
#     initial_sidebar_state="expanded",
# )
st_autorefresh(interval=refresh_interval * 1000, limit=100)

st.sidebar.subheader("Map")
# locations
region = st.sidebar.selectbox(
    "choose region",
    ["US West", "US East", "ME Asia"],
    index=0,
)
init_locations = {
    "US West": {"lat": 37.4275, "lon": -122.168861},
    "US East": {"lat": 40.7128, "lon": -74.0060},
    "Israel": {"lat": 31.0461, "lon": 34.8516},
}
dot_radius = st.sidebar.number_input("dot radius", 10, 1000, 100)

st.sidebar.subheader("Labels")
# labels
label_filter = st.sidebar.selectbox(
    "filter labels by",
    ["category", "weather", "scene", "timeofday"],
    index=0,
)
# ========================== SIDEBAR ==========================


# ============================ MAP ============================
map_df = pd.DataFrame()
for data in get_gps_index(filter_query=filter_query):
    if data.get("row"):
        row = data["row"]["columns"]
        map_df = map_df.append(
            pd.DataFrame([row], columns=["lon", "lat"]),
            ignore_index=True,
        )

if vehicle_to_track is None:
    init_location = init_locations[region]
    init_zoom = 12
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(
                latitude=init_location["lat"],
                longitude=init_location["lon"],
                zoom=init_zoom,
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
else:
    col1, col2 = st.columns([1, 1])
    with col1:
        try:
            init_location = {"lat": map_df["lat"][0], "lon": map_df["lon"][0]}
        except Exception:
            "the vehicle has no trajectory"
            init_location = init_locations[region]
        init_zoom = 15
        dot_radius = 10
        if "trajectory_end_index" not in st.session_state:
            st.session_state["trajectory_end_index"] = 0
        st.session_state["trajectory_end_index"] += 3
        if len(map_df):
            st.session_state["trajectory_end_index"] %= len(map_df)
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state=pdk.ViewState(
                    latitude=init_location["lat"],
                    longitude=init_location["lon"],
                    zoom=init_zoom,
                ),
                layers=[
                    pdk.Layer(
                        "ScatterplotLayer",
                        data=map_df[: st.session_state["trajectory_end_index"]],
                        get_position="[lon, lat]",
                        get_color="[200, 30, 0, 160]",
                        get_radius=dot_radius,
                    ),
                ],
            )
        )
    with col2:
        accel_df = pd.DataFrame(columns=["X", "Y", "Z"])
        for data in get_accelerometer_index(filter_query=filter_query):
            if data.get("row"):
                row = data["row"]["columns"]
                accel_df = accel_df.append(
                    pd.DataFrame([row], columns=["X", "Y", "Z"]),
                    ignore_index=True,
                )
        if "accelerometer_end_index" not in st.session_state:
            st.session_state["accelerometer_end_index"] = 0
        st.session_state["accelerometer_end_index"] += 3
        if len(accel_df):
            st.session_state["accelerometer_end_index"] %= len(accel_df)
        else:
            accel_df = accel_df.append(
                pd.DataFrame(
                    [
                        [0, 0, 0],
                    ],
                    columns=["X", "Y", "Z"],
                ),
                ignore_index=True,
            )
            "the vehicle has no IMU records"
        st.line_chart(accel_df)

# ============================ MAP ============================


# ============================ IMU ============================

# ============================ IMU ============================


# ========================== LABELS ===========================
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
# ========================== LABELS ===========================

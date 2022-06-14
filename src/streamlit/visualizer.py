import streamlit as st
import numpy as np
import pandas as pd


dataframe = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
dataframe
st.write("This is a line_chart.")
st.line_chart(dataframe)

st.write("This is a area_chart.")
st.area_chart(dataframe)

st.write("This is a bar_chart.")
st.bar_chart(dataframe)


st.write("Map data")
data_of_map = pd.DataFrame(
    np.random.randn(1000, 2) / [60, 60] + [36.66, -121.6],
    columns=["latitude", "longitude"],
)
st.map(data_of_map)

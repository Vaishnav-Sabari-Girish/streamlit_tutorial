import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50]
    + [
        12.7892523,
        77.5085674,
    ],
    columns=["lat", "lon"],
)

st.map(map_data)

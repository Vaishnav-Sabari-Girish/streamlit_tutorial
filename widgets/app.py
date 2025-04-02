import streamlit as st
import pandas as pd
import numpy as np
import time

st.write("""
         # Widgets
""")

st.write("""
         ## Slider 
""")

x = st.slider("x")
st.write(f"{x} squared is {x * x}")

st.write(""" 
         ## Text Input
""")

st.text_input("Your name: ", key="name")
# To access it, we will use st.session_state.name

st.write(f"Hi there, {st.session_state.name}")

st.write("""
         ## Checkboxes
""")

if st.checkbox("Show Dataframe"):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    chart_data

st.write("""
         ## Selectbox
""")

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

option = st.selectbox("What is your favorite number ? ", df["first column"])

st.write(f"Your selected: {option}")

st.write("""
         ## Layouts 
         """)

st.sidebar.write("""
         ### Sidebar using `st.sidebar`
         """)

# Adding selectbox to sidebar

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted ?", ("Email", "Phone", "Telegram")
)

# Adding slider to sidebar

add_slider = st.sidebar.slider("Select a rang of values", 0.0, 100.0, (25.0, 75.0))

st.write("## Columns using `st.columns`")

left, right = st.columns(2)

left.button("Hi there")
right.slider("Right slider")

with right:
    chosen = st.radio(
        "Sorting Hat", ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin")
    )
    st.write(f"You are in {chosen} house")

st.write("## Progress Bar")

"Starting 100 iterations......."

placeholder = st.empty()

bar = st.progress(0)


for i in range(100):
    placeholder.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"We are done finally"

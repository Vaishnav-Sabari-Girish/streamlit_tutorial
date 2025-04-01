import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

st.write("""
         ## Table using `st.write()`
""")
st.write(df)


st.write("""\n
         ## Table color highlighting
         ### Table created using `st.dataframe` method
""")
dataframe = pd.DataFrame(
    np.random.randn(10, 20), columns=("col %d" % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("""\n 
         ## Table using `st.table()`
""")
st.table(dataframe)

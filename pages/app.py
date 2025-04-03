import streamlit as st

main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
page_2 = st.Page("page_2.py", title="Second Page", icon="❄️")
page_3 = st.Page("page_3.py", title="Third Page", icon="🎉")

pg = st.navigation([main_page, page_2, page_3])

pg.run()

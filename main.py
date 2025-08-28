import streamlit as st

from common import *

# page configuration

st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")


def page_2():
    st.title("Page 2")


# sidebar for inputs
nav = st.navigation(
    [
        st.Page("plot.py", title="Demo"),
        st.Page("explanation.py", title="Technical Details"),
    ]
)
nav.run()

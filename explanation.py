import streamlit as st

from common import *

title = "Technical Details"
st.set_page_config(page_title=title, layout="centered")

st.title(title)

with open("explanation.md", "r") as f:
    lines = f.read()
    st.markdown(lines)

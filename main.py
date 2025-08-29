import streamlit as st
from common import *

# page configuration

st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")


def page_2():
    st.title("Page 2")


st.sidebar.title(page_icon + " " + page_title)
st.sidebar.text("Created by: ")
linkedin_url = "https://www.linkedin.com/in/andrei-lazer/"
linkedin_logo_url = "https://cdn-icons-png.flaticon.com/512/174/174857.png"
st.sidebar.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="{linkedin_logo_url}" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">Andrei Lazer</a>', unsafe_allow_html=True)


# sidebar for inputs
nav = st.navigation(
    [
        st.Page("plot.py", title="Demo"),
        st.Page("explanation.py", title="Technical Details"),
    ]
)
nav.run()

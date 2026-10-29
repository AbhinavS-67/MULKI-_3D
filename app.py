from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sustainable Mulki 3D",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's header, footer and padding so the 3D scene fills the page
st.markdown(
    """
    <style>
      header, footer, #MainMenu {visibility: hidden; height: 0;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: 0; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=860, scrolling=False)

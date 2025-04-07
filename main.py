import streamlit as st
from streamlit_homepage import run_homepage
from multi_tab_launcher import run_ui as run_multi_tab

# Sidebar navigation
st.sidebar.title("🚀 Modular Assistant OS")
selection = st.sidebar.radio("Go to", ["🏠 Homepage", "🛠️ Multi-Tab Launcher"])

if selection == "🏠 Homepage":
    run_homepage()
elif selection == "🛠️ Multi-Tab Launcher":
    run_multi_tab()

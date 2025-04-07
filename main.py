
import streamlit as st

st.set_page_config(page_title="Modular Assistant OS", layout="wide")

st.sidebar.title("🔧 Navigation")
section = st.sidebar.radio("Jump to Section", ["🚀 Launcher", "🧠 DAG Visualizer", "📘 System Info"])

if section == "🚀 Launcher":
    st.markdown("### Modular Assistant Launcher")
    st.markdown("Run `streamlit run launcher.py` to launch the full assistant interface.")

elif section == "🧠 DAG Visualizer":
    st.markdown("### Assistant DAG Visualizer")
    st.markdown("Run `streamlit run dag_visual_launcher.py` to view DAG nodes by team.")
    st.json({
        "DAG File": "merged_dag_teams_abcdefghijk_preview.json",
        "Total Teams": 11,
        "Assistants": 100
    })

elif section == "📘 System Info":
    st.markdown("""### Assistant System Summary
- 100 Modular Assistants
- 10 Specialized Teams + 1 Meta Layer (Team K)
- DAG-ready, Streamlit-deployable
""")

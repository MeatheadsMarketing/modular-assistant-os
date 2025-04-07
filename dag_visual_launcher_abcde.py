
import streamlit as st
import json
import os

# Load merged DAG
DAG_PATH = "merged_dag_teams_abcde_preview.json"

@st.cache_data
def load_dag():
    with open(DAG_PATH, "r") as f:
        return json.load(f)

st.set_page_config(page_title="Assistant DAG Visualizer", layout="wide")
st.title("🔗 Modular Assistant DAG Visualizer (Teams A–E)")

# Load and display DAG
dag = load_dag()
st.markdown(f"### 🧠 {dag['team']}")
st.markdown("---")

nodes = dag.get("nodes", [])

# Display graph preview manually in Streamlit layout
cols = st.columns(5)
for i, node in enumerate(nodes):
    with cols[i % 5]:
        st.markdown(f"**{node['id']}**")
        st.markdown(f"🔹 `{node['label']}`")
        st.markdown(f"*{node.get('description', '')}*")
        st.markdown(f"**Position:** x={node['position']['x']}, y={node['position']['y']}")
        st.markdown("---")

st.success(f"Loaded {len(nodes)} assistant nodes.")

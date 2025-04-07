
import streamlit as st
import json
import os
import importlib.util

# Load Team A manifest
MANIFEST_PATH = "TeamA/manifest_team_a.json"
DAG_CONFIG_PATH = "TeamA/dag_node_config_team_a.json"

# Helper to dynamically import and run assistant .py files
def run_assistant(filepath):
    if os.path.isfile(filepath):
        spec = importlib.util.spec_from_file_location("assistant", filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "run_ui"):
            module.run_ui()
        else:
            st.error("Assistant missing run_ui() method.")
    else:
        st.error("Assistant file not found.")

# Load manifest
def load_manifest():
    with open(MANIFEST_PATH) as f:
        return json.load(f)

# Load DAG config
def load_dag():
    with open(DAG_CONFIG_PATH) as f:
        return json.load(f)

# Streamlit layout
st.set_page_config(page_title="Modular Assistant Launcher - Team A", layout="wide")
st.title("🚀 Team A: Vault Intelligence Launcher")

# Sidebar: Team metadata
manifest = load_manifest()
st.sidebar.markdown(f"### 🧠 {manifest['team']}")
st.sidebar.markdown("---")

# Filter options
gpt_only = st.sidebar.checkbox("🧠 Show only GPT-Compatible")
dag_only = st.sidebar.checkbox("🔗 Show only DAG Nodes")

# Load DAG for DAG node filtering
dag_node_ids = set(node["id"] for node in load_dag()["nodes"]) if dag_only else None

# Main UI
cols = st.columns(2)
for i, assistant in enumerate(manifest['assistants']):
    if gpt_only and not assistant["gpt_compatible"]:
        continue
    if dag_only and assistant["id"] not in dag_node_ids:
        continue

    with cols[i % 2]:
        st.markdown(f"#### `{assistant['id']}` - {assistant['name']}")
        st.markdown(f"*{assistant['description']}*")
        st.markdown(f"**Category:** {assistant['category']}  |  **Trigger:** `{assistant['trigger']}`")
        st.markdown(f"**GPT-Compatible:** {'✅' if assistant['gpt_compatible'] else '❌'}")
        st.markdown(f"**Export-Ready:** {'✅' if assistant['export_ready'] else '❌'}")
        if st.button(f"▶️ Launch {assistant['name']}", key=assistant['id']):
            run_assistant(assistant['file_path'])


import streamlit as st
import json
import os
import importlib.util

# Manifest and DAG map (Teams A–K)
TEAM_MANIFESTS = {
    "Team A": "TeamA/manifest_team_a.json",
    "Team B": "TeamB/manifest_team_b.json",
    "Team C": "TeamC/manifest_team_c.json",
    "Team D": "TeamD/manifest_team_d.json",
    "Team E": "TeamE/manifest_team_e.json",
    "Team F": "TeamF/manifest_team_f.json",
    "Team G": "TeamG/manifest_team_g.json",
    "Team H": "TeamH/manifest_team_h.json",
    "Team I": "TeamI/manifest_team_i.json",
    "Team J": "TeamJ/manifest_team_j.json",
    "Team K": "TeamK/manifest_team_k.json"
}

# Load manifest
@st.cache_data
def load_manifest(path):
    with open(path) as f:
        return json.load(f)

# Launcher logic
st.set_page_config(layout="wide", page_title="Modular Assistant Launcher")
st.title("🚀 Modular Assistant Launcher")
selected_team = st.selectbox("Choose a team:", list(TEAM_MANIFESTS.keys()))
manifest = load_manifest(TEAM_MANIFESTS[selected_team])

# Sidebar filters
gpt_only = st.sidebar.checkbox("🧠 Show only GPT-Compatible")
display_dag_id = st.sidebar.text_input("🔍 Filter by Assistant ID (optional):")

# Main columns
cols = st.columns(2)
for i, a in enumerate(manifest['assistants']):
    if gpt_only and not a.get("gpt_compatible"):
        continue
    if display_dag_id and display_dag_id not in a["id"]:
        continue

    with cols[i % 2]:
        st.markdown(f"#### `{a['id']}` - {a['name']}")
        st.markdown(f"*{a['description']}*")
        st.markdown(f"**Category:** {a['category']}  |  **Trigger:** `{a['trigger']}`")
        st.markdown(f"**GPT-Compatible:** {'✅' if a['gpt_compatible'] else '❌'}")
        st.markdown(f"**Export-Ready:** {'✅' if a['export_ready'] else '❌'}")
        if st.button(f"▶️ Launch {a['name']}", key=a['id']):
            file_path = a['file_path']
            if os.path.isfile(file_path):
                spec = importlib.util.spec_from_file_location("assistant", file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, "run_ui"):
                    module.run_ui()
                else:
                    st.error("run_ui() not found in file.")
            else:
                st.error(f"File not found: {file_path}")

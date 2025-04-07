
import streamlit as st
import json
import uuid

st.set_page_config(page_title="Multi-Agent Chain Designer")
st.title("🤖 Multi-Agent Chain Designer")

st.markdown("Design a custom sequence of assistant agents by assigning roles and chaining logic.")

# Step 1: Collect roles and agents
roles = st.multiselect("Select Roles for Agents:", ["Researcher", "Critic", "Summarizer", "Planner", "Executor"])

agents = {}
for role in roles:
    agent_name = st.text_input(f"Name of agent for role: {role}", key=role)
    agent_tool = st.text_input(f"Which assistant/tool does {agent_name or role} use?", key=role + "_tool")
    if agent_name and agent_tool:
        agents[role] = {
            "agent_id": str(uuid.uuid4()),
            "name": agent_name,
            "tool": agent_tool,
            "role": role
        }

# Step 2: Define flow logic between agents
st.markdown("---")
st.subheader("🧠 Define Chaining Logic")

flow = []
if len(roles) >= 2:
    for i in range(len(roles) - 1):
        flow.append({"from": roles[i], "to": roles[i+1]})
    st.json(flow)
else:
    st.info("Add at least two roles to configure chaining.")

# Step 3: Export chain configuration
if st.button("💾 Export Chain JSON") and agents:
    export_config = {
        "chain_id": str(uuid.uuid4()),
        "agents": agents,
        "flow": flow
    }
    st.download_button("Download Chain Config", json.dumps(export_config, indent=2), file_name="multi_agent_chain.json")

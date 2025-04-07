
import streamlit as st
import json
import uuid

st.set_page_config(page_title="Agent Roundtable Simulator")
st.title("🧠 Agent Roundtable Simulator")

st.markdown("Simulate a multi-agent discussion where each role contributes to the final decision.")

# Step 1: Define the core question/topic
core_prompt = st.text_area("📝 Central Topic or Question for Discussion:",
    placeholder="e.g., Should we launch the new assistant now or wait for validation results?")

# Step 2: Define agent participants
agent_roles = st.multiselect("🤖 Select Roles in the Roundtable:",
    ["Strategist", "Analyst", "Critic", "Innovator", "Integrator"])

agent_inputs = {}
for role in agent_roles:
    agent_prompt = st.text_area(f"💬 {role}'s Input:", placeholder=f"What would a {role} say?", key=f"input_{role}")
    if agent_prompt:
        agent_inputs[role] = {
            "role": role,
            "input": agent_prompt
        }

# Step 3: Generate a GPT-style roundtable summary
if st.button("🧠 Simulate Roundtable Output") and core_prompt and agent_inputs:
    st.subheader("📣 Synthesized Group Consensus")
    synthesized_output = f"Based on the discussion around: '{core_prompt}', here are the contributions:\n\n"
    for role, entry in agent_inputs.items():
        synthesized_output += f"- **{role}**: {entry['input']}\n"

    synthesized_output += "\n🤖 **Final Insight**: A consensus is forming around integrating multiple perspectives before acting."
    st.text_area("🧠 Roundtable Summary:", value=synthesized_output, height=250)

    st.download_button(
        label="📦 Download Roundtable Report",
        file_name="agent_roundtable_summary.json",
        mime="application/json",
        data=json.dumps({
            "roundtable_id": str(uuid.uuid4()),
            "prompt": core_prompt,
            "inputs": agent_inputs,
            "summary": synthesized_output
        }, indent=2)
    )

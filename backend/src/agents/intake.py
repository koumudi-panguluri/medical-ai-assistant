"""Intake Agent — gathers and structures patient information."""

from langchain_core.messages import SystemMessage

from src.config import get_llm
from src.state import PatientState
from src.tools.patient_records import get_patient_record, search_patient_records

INTAKE_SYSTEM_PROMPT = """\
You are a Medical Intake Agent. Your role is to:

1. Process the incoming patient input (which may be a patient ID, a name,
   a free-text description of symptoms, or a combination).
2. Use the available tools to retrieve the patient's medical record.
3. Produce a structured intake summary that includes:
   - Patient demographics (name, age, sex)
   - Chief complaint or reason for the current encounter
   - Active medical conditions
   - Current medications
   - Known allergies
   - Relevant recent lab results
   - Brief visit history summary

If the input does not reference a specific patient, create a summary from
the free-text information provided.

Be thorough but concise. Output ONLY the structured summary — no
conversational filler.
"""

TOOLS = [get_patient_record, search_patient_records]


def run_intake(state: PatientState) -> dict:
    """Execute the intake agent node."""
    llm = get_llm().bind_tools(TOOLS)
    messages = [
        SystemMessage(content=INTAKE_SYSTEM_PROMPT),
    ]

    patient_input = state.get("patient_input", "")
    from langchain_core.messages import HumanMessage
    messages.append(HumanMessage(content=f"Process intake for: {patient_input}"))

    # Agentic tool-use loop
    patient_history = ""
    for _ in range(6):  # max iterations to prevent infinite loops
        response = llm.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            break

        from langchain_core.messages import ToolMessage
        for tool_call in response.tool_calls:
            tool_fn = {t.name: t for t in TOOLS}[tool_call["name"]]
            result = tool_fn.invoke(tool_call["args"])
            if tool_call["name"] == "get_patient_record":
                patient_history = result
            messages.append(
                ToolMessage(content=result, tool_call_id=tool_call["id"])
            )

    intake_summary = response.content if response.content else "Intake could not be completed."

    return {
        "intake_summary": intake_summary,
        "patient_history": patient_history or intake_summary,
        "messages": [f"[Intake Agent] Completed intake processing."],
    }

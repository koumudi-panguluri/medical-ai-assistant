"""Diagnosis Reasoning Agent — analyzes symptoms and evidence to produce diagnostic assessment."""

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

from src.config import get_llm
from src.state import PatientState
from src.tools.drug_interactions import check_drug_interactions, lookup_drug_info
from src.tools.medical_search import search_medical_literature

DIAGNOSIS_SYSTEM_PROMPT = """\
You are a Medical Diagnosis Reasoning Agent. You receive a structured intake
summary and patient history. Your role is to:

1. Identify the key clinical problems and prioritize them.
2. Search medical literature to find relevant evidence and guidelines.
3. Check the patient's current medications for interactions and safety concerns.
4. Look up relevant drug information as needed.
5. Formulate a differential diagnosis or clinical assessment, including:
   - Primary assessment for each active problem
   - Supporting evidence from the patient's data (labs, vitals, history)
   - Relevant findings from medical literature
   - Any medication concerns (interactions, contraindications)
   - Risk stratification where applicable

IMPORTANT: This is for educational/simulation purposes only. Always note that
real clinical decisions require a licensed healthcare provider.

Be systematic and evidence-based. Use a problem-oriented approach.
Output ONLY the diagnostic assessment — no conversational filler.
"""

TOOLS = [search_medical_literature, lookup_drug_info, check_drug_interactions]


def run_diagnosis(state: PatientState) -> dict:
    """Execute the diagnosis reasoning agent node."""
    llm = get_llm().bind_tools(TOOLS)

    intake_summary = state.get("intake_summary", "No intake summary available.")
    patient_history = state.get("patient_history", "")

    context = f"INTAKE SUMMARY:\n{intake_summary}"
    if patient_history and patient_history != intake_summary:
        context += f"\n\nPATIENT HISTORY:\n{patient_history}"

    messages = [
        SystemMessage(content=DIAGNOSIS_SYSTEM_PROMPT),
        HumanMessage(content=f"Analyze the following patient case:\n\n{context}"),
    ]

    # Agentic tool-use loop
    search_results_parts = []
    drug_interaction_parts = []

    for _ in range(8):  # max iterations
        response = llm.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            break

        for tool_call in response.tool_calls:
            tool_fn = {t.name: t for t in TOOLS}[tool_call["name"]]
            result = tool_fn.invoke(tool_call["args"])

            if tool_call["name"] == "search_medical_literature":
                search_results_parts.append(result)
            elif tool_call["name"] == "check_drug_interactions":
                drug_interaction_parts.append(result)

            messages.append(
                ToolMessage(content=result, tool_call_id=tool_call["id"])
            )

    diagnosis = response.content if response.content else "Diagnosis reasoning could not be completed."

    return {
        "diagnosis": diagnosis,
        "search_results": "\n---\n".join(search_results_parts) if search_results_parts else "",
        "drug_interactions": "\n".join(drug_interaction_parts) if drug_interaction_parts else "",
        "messages": [f"[Diagnosis Agent] Completed diagnostic assessment."],
    }

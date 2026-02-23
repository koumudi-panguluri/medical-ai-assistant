"""Care Plan Agent — generates an actionable care plan based on diagnosis."""

from langchain_core.messages import HumanMessage, SystemMessage

from src.config import get_llm
from src.state import PatientState

CARE_PLAN_SYSTEM_PROMPT = """\
You are a Medical Care Plan Agent. You receive a diagnostic assessment along
with the patient's intake summary, history, and any identified drug
interactions. Your role is to generate a comprehensive, actionable care plan.

Your care plan must include:

1. **Problem List** — Numbered list of active clinical problems.
2. **Medication Plan** — For each problem:
   - Continue, adjust, or discontinue current medications (with rationale).
   - New medication recommendations if warranted.
   - Flag any interactions or contraindications identified.
3. **Monitoring & Labs** — Specific tests to order and follow-up intervals.
4. **Lifestyle & Patient Education** — Diet, exercise, and self-management
   recommendations tailored to the patient's conditions.
5. **Referrals** — Specialist referrals if needed.
6. **Follow-Up** — Recommended follow-up timeline and what to reassess.
7. **Red Flags** — Warning signs that should prompt the patient to seek
   immediate medical attention.

IMPORTANT DISCLAIMER: Include a note that this care plan is generated for
educational/simulation purposes and all clinical decisions must be made by
a licensed healthcare provider.

Be specific and actionable. Avoid vague advice. Tailor recommendations to
the patient's specific data.
"""


def run_care_plan(state: PatientState) -> dict:
    """Execute the care plan generation agent node."""
    llm = get_llm()

    intake_summary = state.get("intake_summary", "")
    diagnosis = state.get("diagnosis", "")
    drug_interactions = state.get("drug_interactions", "")

    context_parts = [f"INTAKE SUMMARY:\n{intake_summary}"]

    if diagnosis:
        context_parts.append(f"DIAGNOSTIC ASSESSMENT:\n{diagnosis}")
    if drug_interactions:
        context_parts.append(f"DRUG INTERACTION ALERTS:\n{drug_interactions}")

    context = "\n\n".join(context_parts)

    messages = [
        SystemMessage(content=CARE_PLAN_SYSTEM_PROMPT),
        HumanMessage(
            content=f"Generate a care plan for the following patient:\n\n{context}"
        ),
    ]

    response = llm.invoke(messages)

    care_plan = response.content if response.content else "Care plan could not be generated."

    return {
        "care_plan": care_plan,
        "messages": [f"[Care Plan Agent] Completed care plan generation."],
    }

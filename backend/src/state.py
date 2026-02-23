"""Shared state definition for the multi-agent medical graph."""

from __future__ import annotations

import operator
from typing import Annotated, TypedDict


class PatientState(TypedDict, total=False):
    """State that flows through the LangGraph medical pipeline.

    Attributes:
        patient_input: Raw intake text from the patient or clinician.
        intake_summary: Structured summary produced by the Intake agent.
        patient_history: Retrieved patient history records.
        search_results: Results from medical database searches.
        drug_interactions: Drug interaction check results.
        diagnosis: Diagnostic reasoning produced by the Diagnosis agent.
        care_plan: Final care plan produced by the Care Plan agent.
        messages: Append-only message log for traceability.
    """

    patient_input: str
    intake_summary: str
    patient_history: str
    search_results: str
    drug_interactions: str
    diagnosis: str
    care_plan: str
    messages: Annotated[list[str], operator.add]

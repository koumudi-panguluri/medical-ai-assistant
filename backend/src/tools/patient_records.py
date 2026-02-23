"""Tools for accessing simulated patient records."""

import json

from langchain_core.tools import tool

from src.data.patient_database import get_patient, list_all_patient_ids, search_patients


@tool
def get_patient_record(patient_id: str) -> str:
    """Retrieve a patient's full medical record by their ID.

    Returns demographics, conditions, medications, allergies, recent labs,
    and visit history.

    Args:
        patient_id: The patient identifier (e.g. "P-1001").
    """
    patient = get_patient(patient_id)
    if patient is None:
        available = ", ".join(list_all_patient_ids())
        return f"Patient '{patient_id}' not found. Available IDs: {available}"

    labs = "\n".join(f"    {k}: {v}" for k, v in patient["recent_labs"].items())
    visits = "\n".join(
        f"    [{v['date']}] {v['reason']} — {v['notes']}"
        for v in patient["visit_history"]
    )

    return (
        f"Patient: {patient['name']} (ID: {patient['id']})\n"
        f"Age: {patient['age']} | Sex: {patient['sex']}\n"
        f"Conditions: {', '.join(patient['conditions'])}\n"
        f"Medications: {', '.join(patient['medications'])}\n"
        f"Allergies: {', '.join(patient['allergies']) or 'None known'}\n"
        f"Recent Labs:\n{labs}\n"
        f"Visit History:\n{visits}\n"
    )


@tool
def search_patient_records(query: str) -> str:
    """Search patient records by name or condition.

    Args:
        query: Patient name or condition to search for (e.g. "Garcia", "Diabetes").
    """
    results = search_patients(query)
    if not results:
        available = ", ".join(list_all_patient_ids())
        return f"No patients found matching '{query}'. Available IDs: {available}"

    output_parts = []
    for p in results:
        output_parts.append(
            f"  {p['id']}: {p['name']} (Age {p['age']}, {p['sex']}) — {', '.join(p['conditions'])}"
        )
    return "Matching patients:\n" + "\n".join(output_parts)

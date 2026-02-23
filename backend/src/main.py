"""Main entry point for the Medical Multi-Agent System.

Usage:
    python -m src.main "P-1001"
    python -m src.main "Patient Maria Garcia, complaining of increased thirst and frequent urination"
    python -m src.main  # interactive mode
"""

from __future__ import annotations

import sys

from src.graph import build_medical_graph


def format_output(result: dict) -> str:
    """Format the final pipeline output for display."""
    sections = []

    sections.append("=" * 70)
    sections.append("MEDICAL MULTI-AGENT SYSTEM — REPORT")
    sections.append("=" * 70)

    if result.get("intake_summary"):
        sections.append("\n── INTAKE SUMMARY ──")
        sections.append(result["intake_summary"])

    if result.get("drug_interactions"):
        sections.append("\n── DRUG INTERACTION ALERTS ──")
        sections.append(result["drug_interactions"])

    if result.get("diagnosis"):
        sections.append("\n── DIAGNOSTIC ASSESSMENT ──")
        sections.append(result["diagnosis"])

    if result.get("care_plan"):
        sections.append("\n── CARE PLAN ──")
        sections.append(result["care_plan"])

    if result.get("messages"):
        sections.append("\n── AGENT LOG ──")
        for msg in result["messages"]:
            sections.append(f"  {msg}")

    sections.append("\n" + "=" * 70)
    sections.append(
        "DISCLAIMER: This output is generated for educational and simulation "
        "purposes only. All clinical decisions must be made by a licensed "
        "healthcare provider."
    )
    sections.append("=" * 70)

    return "\n".join(sections)


def run(patient_input: str) -> dict:
    """Run the full medical pipeline and return raw results."""
    graph = build_medical_graph()
    result = graph.invoke({"patient_input": patient_input, "messages": []})
    return result


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) > 1:
        patient_input = " ".join(sys.argv[1:])
    else:
        print("Medical Multi-Agent System")
        print("-" * 40)
        print("Enter patient ID (e.g. P-1001) or describe the patient case.")
        print("Available sample patients: P-1001, P-1002, P-1003, P-1004")
        print()
        patient_input = input("Patient input: ").strip()
        if not patient_input:
            print("No input provided. Exiting.")
            sys.exit(1)

    print(f"\nProcessing: {patient_input}")
    print("Running agents: Intake → Diagnosis → Care Plan ...\n")

    result = run(patient_input)
    print(format_output(result))


if __name__ == "__main__":
    main()

"""Simulated patient records database."""

PATIENTS: dict[str, dict] = {
    "P-1001": {
        "id": "P-1001",
        "name": "Maria Garcia",
        "age": 62,
        "sex": "Female",
        "conditions": ["Type 2 Diabetes Mellitus", "Hypertension", "Hyperlipidemia"],
        "medications": ["metformin 1000mg BID", "lisinopril 20mg daily", "atorvastatin 40mg daily"],
        "allergies": ["Penicillin"],
        "recent_labs": {
            "HbA1c": "7.8%",
            "fasting_glucose": "156 mg/dL",
            "eGFR": "68 mL/min/1.73m2",
            "LDL": "112 mg/dL",
            "blood_pressure": "142/88 mmHg",
        },
        "visit_history": [
            {"date": "2025-11-15", "reason": "Routine diabetes follow-up", "notes": "HbA1c rising; discussed diet adherence."},
            {"date": "2025-08-20", "reason": "Hypertension check", "notes": "BP slightly above target; continue current regimen."},
            {"date": "2025-05-10", "reason": "Annual physical", "notes": "Labs ordered; renal function stable."},
        ],
    },
    "P-1002": {
        "id": "P-1002",
        "name": "James Chen",
        "age": 45,
        "sex": "Male",
        "conditions": ["Major Depressive Disorder", "Chronic Migraine"],
        "medications": ["sertraline 100mg daily", "sumatriptan 50mg PRN"],
        "allergies": [],
        "recent_labs": {
            "CBC": "Within normal limits",
            "TSH": "2.1 mIU/L",
            "metabolic_panel": "Normal",
        },
        "visit_history": [
            {"date": "2025-12-01", "reason": "Depression follow-up", "notes": "Mood improving on sertraline. Migraines still 3-4x/month."},
            {"date": "2025-09-15", "reason": "Migraine evaluation", "notes": "Considering preventive therapy; CGRP inhibitor discussed."},
        ],
    },
    "P-1003": {
        "id": "P-1003",
        "name": "Aisha Johnson",
        "age": 34,
        "sex": "Female",
        "conditions": ["Asthma (moderate persistent)"],
        "medications": ["fluticasone/salmeterol 250/50 BID", "albuterol PRN"],
        "allergies": ["Sulfonamides"],
        "recent_labs": {
            "spirometry_FEV1": "72% predicted",
            "peak_flow": "380 L/min",
            "eosinophils": "420 cells/uL",
        },
        "visit_history": [
            {"date": "2025-10-10", "reason": "Asthma exacerbation", "notes": "Increased rescue inhaler use. Oral prednisone taper prescribed."},
            {"date": "2025-07-22", "reason": "Routine asthma check", "notes": "Partially controlled on current regimen."},
        ],
    },
    "P-1004": {
        "id": "P-1004",
        "name": "Robert Williams",
        "age": 71,
        "sex": "Male",
        "conditions": ["Atrial Fibrillation", "Hypertension", "Chronic Kidney Disease Stage 3a"],
        "medications": ["warfarin 5mg daily", "amlodipine 10mg daily", "aspirin 81mg daily"],
        "allergies": ["ACE Inhibitors (cough)"],
        "recent_labs": {
            "INR": "2.8",
            "eGFR": "52 mL/min/1.73m2",
            "creatinine": "1.4 mg/dL",
            "blood_pressure": "138/82 mmHg",
            "potassium": "4.8 mEq/L",
        },
        "visit_history": [
            {"date": "2025-11-28", "reason": "INR check", "notes": "INR slightly above range; reduce warfarin to 4mg and recheck in 1 week."},
            {"date": "2025-10-05", "reason": "CKD monitoring", "notes": "eGFR stable. Avoid nephrotoxic agents."},
        ],
    },
}


def get_patient(patient_id: str) -> dict | None:
    """Retrieve a patient record by ID."""
    return PATIENTS.get(patient_id)


def search_patients(query: str) -> list[dict]:
    """Search patients by name or condition (case-insensitive)."""
    query_lower = query.lower()
    results = []
    for patient in PATIENTS.values():
        if query_lower in patient["name"].lower():
            results.append(patient)
            continue
        if any(query_lower in c.lower() for c in patient["conditions"]):
            results.append(patient)
    return results


def list_all_patient_ids() -> list[str]:
    """Return all available patient IDs."""
    return list(PATIENTS.keys())

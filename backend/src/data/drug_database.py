"""Simulated drug interaction database."""

DRUGS: dict[str, dict] = {
    "metformin": {
        "class": "Biguanide",
        "indications": ["Type 2 Diabetes Mellitus"],
        "common_side_effects": ["nausea", "diarrhea", "abdominal pain"],
        "serious_warnings": ["lactic acidosis (rare)", "contraindicated in severe renal impairment (eGFR <30)"],
    },
    "lisinopril": {
        "class": "ACE Inhibitor",
        "indications": ["Hypertension", "Heart Failure", "Diabetic Nephropathy"],
        "common_side_effects": ["dry cough", "dizziness", "hyperkalemia"],
        "serious_warnings": ["angioedema", "contraindicated in pregnancy"],
    },
    "amlodipine": {
        "class": "Calcium Channel Blocker",
        "indications": ["Hypertension", "Angina"],
        "common_side_effects": ["peripheral edema", "headache", "flushing"],
        "serious_warnings": ["hypotension"],
    },
    "atorvastatin": {
        "class": "HMG-CoA Reductase Inhibitor (Statin)",
        "indications": ["Hyperlipidemia", "Cardiovascular risk reduction"],
        "common_side_effects": ["myalgia", "elevated liver enzymes", "GI upset"],
        "serious_warnings": ["rhabdomyolysis (rare)", "hepatotoxicity"],
    },
    "aspirin": {
        "class": "NSAID / Antiplatelet",
        "indications": ["Pain", "Fever", "Cardiovascular prophylaxis"],
        "common_side_effects": ["GI bleeding", "dyspepsia"],
        "serious_warnings": ["GI hemorrhage", "Reye syndrome in children"],
    },
    "sertraline": {
        "class": "SSRI",
        "indications": ["Major Depressive Disorder", "Anxiety Disorders", "PTSD", "OCD"],
        "common_side_effects": ["nausea", "insomnia", "sexual dysfunction", "diarrhea"],
        "serious_warnings": ["serotonin syndrome", "suicidal ideation in young adults"],
    },
    "amoxicillin": {
        "class": "Aminopenicillin",
        "indications": ["Community-Acquired Pneumonia", "Otitis Media", "UTI"],
        "common_side_effects": ["diarrhea", "rash", "nausea"],
        "serious_warnings": ["anaphylaxis", "C. difficile colitis"],
    },
    "albuterol": {
        "class": "Short-Acting Beta-2 Agonist (SABA)",
        "indications": ["Asthma (rescue)", "Bronchospasm", "COPD"],
        "common_side_effects": ["tremor", "tachycardia", "headache"],
        "serious_warnings": ["paradoxical bronchospasm"],
    },
    "sumatriptan": {
        "class": "Triptan (5-HT1B/1D Agonist)",
        "indications": ["Migraine", "Cluster Headache"],
        "common_side_effects": ["tingling", "chest tightness", "dizziness"],
        "serious_warnings": ["coronary vasospasm", "serotonin syndrome with SSRIs"],
    },
    "warfarin": {
        "class": "Vitamin K Antagonist",
        "indications": ["Atrial Fibrillation", "DVT/PE", "Mechanical Heart Valve"],
        "common_side_effects": ["bleeding", "bruising"],
        "serious_warnings": ["major hemorrhage", "teratogenic", "numerous drug interactions"],
    },
}

INTERACTIONS: list[dict] = [
    {
        "drug_a": "warfarin",
        "drug_b": "aspirin",
        "severity": "Major",
        "description": "Increased risk of bleeding. Concurrent use requires close INR monitoring and clinical justification.",
    },
    {
        "drug_a": "sertraline",
        "drug_b": "sumatriptan",
        "severity": "Major",
        "description": "Risk of serotonin syndrome. Use with caution; monitor for agitation, hyperthermia, and clonus.",
    },
    {
        "drug_a": "lisinopril",
        "drug_b": "metformin",
        "severity": "Minor",
        "description": "ACE inhibitors may enhance the hypoglycemic effect of metformin. Monitor blood glucose.",
    },
    {
        "drug_a": "atorvastatin",
        "drug_b": "warfarin",
        "severity": "Moderate",
        "description": "Statins may increase warfarin effect. Monitor INR when initiating or changing statin dose.",
    },
    {
        "drug_a": "aspirin",
        "drug_b": "sertraline",
        "severity": "Moderate",
        "description": "SSRIs may increase the antiplatelet effect of aspirin, raising bleeding risk.",
    },
]


def lookup_drug(name: str) -> dict | None:
    """Look up a drug by name (case-insensitive)."""
    return DRUGS.get(name.lower())


def check_interactions(drug_names: list[str]) -> list[dict]:
    """Check for known interactions among a list of drug names."""
    normalized = [d.lower() for d in drug_names]
    found = []
    for interaction in INTERACTIONS:
        if interaction["drug_a"] in normalized and interaction["drug_b"] in normalized:
            found.append(interaction)
    return found

"""Simulated medical literature database (PubMed-style)."""

ARTICLES: list[dict] = [
    {
        "id": "PMID-10001",
        "title": "Management of Type 2 Diabetes Mellitus in Adults",
        "abstract": (
            "Type 2 diabetes mellitus (T2DM) is a chronic metabolic disorder characterized "
            "by hyperglycemia resulting from insulin resistance and relative insulin "
            "deficiency. First-line treatment includes lifestyle modifications and "
            "metformin therapy. Second-line agents include SGLT2 inhibitors, GLP-1 "
            "receptor agonists, and DPP-4 inhibitors. Individualized treatment plans "
            "should consider cardiovascular risk, renal function, and patient preference."
        ),
        "keywords": ["diabetes", "metformin", "hyperglycemia", "insulin", "SGLT2", "GLP-1"],
        "year": 2024,
    },
    {
        "id": "PMID-10002",
        "title": "Diagnosis and Treatment of Community-Acquired Pneumonia",
        "abstract": (
            "Community-acquired pneumonia (CAP) remains a leading cause of morbidity and "
            "mortality worldwide. Diagnosis is based on clinical presentation (cough, "
            "fever, dyspnea) supported by chest radiography. Empiric antibiotic therapy "
            "should cover typical and atypical pathogens. Outpatient treatment with "
            "amoxicillin or doxycycline is appropriate for low-risk patients. Hospitalized "
            "patients should receive beta-lactam plus macrolide or respiratory fluoroquinolone."
        ),
        "keywords": ["pneumonia", "CAP", "antibiotic", "cough", "fever", "respiratory"],
        "year": 2023,
    },
    {
        "id": "PMID-10003",
        "title": "Hypertension: Current Evidence and Clinical Practice",
        "abstract": (
            "Hypertension affects approximately 1.3 billion people globally and is a "
            "major risk factor for cardiovascular disease, stroke, and chronic kidney "
            "disease. Current guidelines recommend a target blood pressure of <130/80 "
            "mmHg for most adults. First-line pharmacotherapy includes ACE inhibitors, "
            "ARBs, calcium channel blockers, and thiazide diuretics. Combination therapy "
            "is often required. Lifestyle modifications including sodium reduction, "
            "regular exercise, and weight management are essential."
        ),
        "keywords": ["hypertension", "blood pressure", "ACE inhibitor", "ARB", "cardiovascular"],
        "year": 2024,
    },
    {
        "id": "PMID-10004",
        "title": "Acute Myocardial Infarction: Rapid Assessment and Management",
        "abstract": (
            "Acute myocardial infarction (MI) requires immediate recognition and "
            "treatment. Presenting symptoms include chest pain, dyspnea, diaphoresis, "
            "and nausea. ECG and cardiac troponin levels are essential for diagnosis. "
            "STEMI patients require emergent percutaneous coronary intervention (PCI) "
            "within 90 minutes of first medical contact. Dual antiplatelet therapy, "
            "anticoagulation, beta-blockers, and statins are cornerstone treatments."
        ),
        "keywords": ["myocardial infarction", "heart attack", "chest pain", "STEMI", "troponin", "PCI"],
        "year": 2024,
    },
    {
        "id": "PMID-10005",
        "title": "Asthma Management in Adults: A Comprehensive Review",
        "abstract": (
            "Asthma is a chronic inflammatory airway disease affecting over 300 million "
            "people worldwide. Diagnosis is based on variable respiratory symptoms and "
            "expiratory airflow limitation. Inhaled corticosteroids (ICS) are the "
            "cornerstone of maintenance therapy. Step-up therapy includes addition of "
            "long-acting beta-agonists (LABA), leukotriene receptor antagonists, or "
            "biologic agents for severe asthma. Patients should have a written asthma "
            "action plan and regular follow-up."
        ),
        "keywords": ["asthma", "inhaler", "corticosteroid", "LABA", "wheezing", "respiratory"],
        "year": 2023,
    },
    {
        "id": "PMID-10006",
        "title": "Major Depressive Disorder: Pharmacological and Non-Pharmacological Approaches",
        "abstract": (
            "Major depressive disorder (MDD) is characterized by persistent low mood, "
            "anhedonia, and functional impairment. First-line pharmacotherapy includes "
            "SSRIs and SNRIs. Cognitive behavioral therapy (CBT) is effective as "
            "monotherapy for mild-moderate depression and as adjunct for severe cases. "
            "Treatment-resistant depression may benefit from augmentation strategies, "
            "ketamine-based therapies, or electroconvulsive therapy (ECT)."
        ),
        "keywords": ["depression", "SSRI", "SNRI", "CBT", "mental health", "mood"],
        "year": 2024,
    },
    {
        "id": "PMID-10007",
        "title": "Chronic Kidney Disease: Detection and Management",
        "abstract": (
            "Chronic kidney disease (CKD) is defined by decreased kidney function "
            "(eGFR <60 mL/min/1.73m2) or kidney damage persisting for >3 months. "
            "Common causes include diabetes and hypertension. Management focuses on "
            "slowing progression through blood pressure control, RAAS inhibition, "
            "SGLT2 inhibitors, and dietary modifications. Patients with eGFR <30 should "
            "be referred to nephrology for renal replacement planning."
        ),
        "keywords": ["kidney", "CKD", "eGFR", "nephrology", "dialysis", "renal"],
        "year": 2024,
    },
    {
        "id": "PMID-10008",
        "title": "Migraine: Pathophysiology and Modern Treatment Strategies",
        "abstract": (
            "Migraine is a neurovascular disorder characterized by recurrent episodes "
            "of headache, often unilateral and throbbing, associated with nausea, "
            "photophobia, and phonophobia. Acute treatment includes triptans and NSAIDs. "
            "Preventive therapies include beta-blockers, topiramate, amitriptyline, and "
            "newer CGRP monoclonal antibodies (erenumab, fremanezumab, galcanezumab). "
            "CGRP antagonists have shown significant efficacy with favorable safety profiles."
        ),
        "keywords": ["migraine", "headache", "triptan", "CGRP", "neurology"],
        "year": 2024,
    },
]


def search_articles(query: str) -> list[dict]:
    """Search the simulated medical literature by keyword matching."""
    query_terms = query.lower().split()
    results = []
    for article in ARTICLES:
        searchable = (
            article["title"].lower()
            + " "
            + article["abstract"].lower()
            + " "
            + " ".join(article["keywords"]).lower()
        )
        if any(term in searchable for term in query_terms):
            results.append(article)
    return results

# Medical Multi-Agent System

A LangGraph-based multi-agent system that processes patient cases through three
specialized agents: **Intake**, **Diagnosis Reasoning**, and **Care Plan Generation**.

## Architecture

```
Patient Input
     │
     ▼
┌──────────┐    ┌─────────────┐    ┌────────────┐
│  Intake  │───▶│  Diagnosis  │───▶│  Care Plan │
│  Agent   │    │   Agent     │    │   Agent    │
└──────────┘    └─────────────┘    └────────────┘
     │                │
     ▼                ▼
 Patient Records   Medical Literature
 (tool)            Drug Interactions
                   (tools)
```

**Intake Agent** — Retrieves patient records, structures demographics, conditions,
medications, allergies, and visit history into a standardized summary.

**Diagnosis Agent** — Searches medical literature, checks drug interactions, and
produces an evidence-based diagnostic assessment using a problem-oriented approach.

**Care Plan Agent** — Generates an actionable care plan with medication adjustments,
monitoring, lifestyle recommendations, referrals, and follow-up timelines.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Usage

```bash
# With a patient ID
python -m src.main "P-1001"

# With a free-text description
python -m src.main "45-year-old male with worsening migraines and depression"

# Interactive mode
python -m src.main
```

### Sample patients

| ID     | Name             | Conditions                                    |
|--------|------------------|-----------------------------------------------|
| P-1001 | Maria Garcia     | Type 2 Diabetes, Hypertension, Hyperlipidemia |
| P-1002 | James Chen       | Major Depressive Disorder, Chronic Migraine   |
| P-1003 | Aisha Johnson    | Asthma (moderate persistent)                  |
| P-1004 | Robert Williams  | Atrial Fibrillation, Hypertension, CKD 3a     |

## Project Structure

```
src/
├── main.py              # CLI entry point
├── config.py            # LLM configuration
├── state.py             # Shared PatientState definition
├── graph.py             # LangGraph orchestrator
├── agents/
│   ├── intake.py        # Intake Agent
│   ├── diagnosis.py     # Diagnosis Reasoning Agent
│   └── care_plan.py     # Care Plan Agent
├── tools/
│   ├── medical_search.py      # Medical literature search tool
│   ├── drug_interactions.py   # Drug lookup & interaction checker
│   └── patient_records.py     # Patient record retrieval tools
└── data/
    ├── medical_articles.py    # Simulated PubMed-style articles
    ├── drug_database.py       # Simulated drug & interaction data
    └── patient_database.py    # Simulated patient records
```

## Disclaimer

This system is for **educational and simulation purposes only**. All clinical
decisions must be made by a licensed healthcare provider.

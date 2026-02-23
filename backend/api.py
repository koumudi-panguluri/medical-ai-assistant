from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import time
import sys
import os

sys.path.append(os.path.dirname(__file__))

from src.graph import build_medical_graph
from src.data.patient_database import PATIENTS, get_patient

app = FastAPI(
    title="Medical AI Assistant API",
    description="Multi-agent medical diagnosis system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PatientBasic(BaseModel):
    id: str
    name: str
    age: int
    sex: str
    conditions: List[str]

class PatientDetailed(BaseModel):
    id: str
    name: str
    age: int
    sex: str
    conditions: List[str]
    medications: List[str]
    allergies: List[str]
    recent_labs: dict
    visit_history: List[dict]

class AnalysisRequest(BaseModel):
    patient_id: str

class AnalysisResponse(BaseModel):
    patient_info: PatientDetailed
    intake_summary: str
    diagnosis: str
    care_plan: str
    drug_interactions: Optional[str] = None
    search_results: Optional[str] = None
    processing_time: float
    agent_logs: List[str]


@app.get("/")
def root():
    return {
        "message": "Medical AI Assistant API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/api/patients", response_model=List[PatientBasic])
def list_patients():
    patients = []
    for patient_data in PATIENTS.values():
        patients.append(PatientBasic(
            id=patient_data["id"],
            name=patient_data["name"],
            age=patient_data["age"],
            sex=patient_data["sex"],
            conditions=patient_data["conditions"]
        ))
    return patients

@app.get("/api/patient/{patient_id}", response_model=PatientDetailed)
def get_patient_details(patient_id: str):
    patient = get_patient(patient_id)
    
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found")
    
    return PatientDetailed(
        id=patient["id"],
        name=patient["name"],
        age=patient["age"],
        sex=patient["sex"],
        conditions=patient["conditions"],
        medications=patient["medications"],
        allergies=patient["allergies"],
        recent_labs=patient["recent_labs"],
        visit_history=patient["visit_history"]
    )

@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_patient(request: AnalysisRequest):
    start_time = time.time()
    
    try:
        patient = get_patient(request.patient_id)
        if not patient:
            raise HTTPException(
                status_code=404, 
                detail=f"Patient {request.patient_id} not found"
            )
        
        print(f"Starting analysis for patient {request.patient_id}...")
        graph = build_medical_graph()
        
        result = graph.invoke({
            "patient_input": request.patient_id,
            "messages": []
        })
        
        processing_time = time.time() - start_time
        print(f"Analysis complete in {processing_time:.2f}s")
        
        return AnalysisResponse(
            patient_info=PatientDetailed(
                id=patient["id"],
                name=patient["name"],
                age=patient["age"],
                sex=patient["sex"],
                conditions=patient["conditions"],
                medications=patient["medications"],
                allergies=patient["allergies"],
                recent_labs=patient["recent_labs"],
                visit_history=patient["visit_history"]
            ),
            intake_summary=result.get("intake_summary", ""),
            diagnosis=result.get("diagnosis", ""),
            care_plan=result.get("care_plan", ""),
            drug_interactions=result.get("drug_interactions"),
            search_results=result.get("search_results"),
            processing_time=processing_time,
            agent_logs=result.get("messages", [])
        )
    
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        raise HTTPException(
            status_code=500, 
            detail=f"Analysis failed: {str(e)}"
        )

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "patients_available": len(PATIENTS),
        "timestamp": time.time()
    }

if __name__ == "__main__":
    import uvicorn
    
    print("=" * 60)
    print("Starting Medical AI Assistant API")
    print("=" * 60)
    print("API Docs: http://localhost:8000/docs")
    print("Health Check: http://localhost:8000/api/health")
    print("=" * 60)
    
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        log_level="info"
    )
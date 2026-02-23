const API_BASE = process.env.REACT_APP_API_URL || "http://localhost:8000";

export interface Patient {
    id: string;
    name: string;
    age: number;
    sex: string;
    conditions: string[];
}

export interface PatientDetailed extends Patient {
    medications: string[];
    allergies: string[];
    recent_labs: {
        [key: string]: string | number;
    };
    visit_history: Array<{
        date: string;
        reason: string;
        notes: string;
    }>;
}

export interface AnalysisResult {
    patient_info: PatientDetailed;
    intake_summary: string;
    diagnosis: string;
    care_plan: string;
    drug_interactions?: string;
    search_results?: string;
    processing_time: number;
    agent_logs: string[];
}

export async function fetchPatients(): Promise<Patient[]> {
    try {
        const response = await fetch(`${API_BASE}/api/patients`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching patients:", error);
        throw error;
    }
}

export async function fetchPatientDetails(patientId: string): Promise<PatientDetailed> {
    try {
        const response = await fetch(`${API_BASE}/api/patient/${patientId}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching patient details:", error);
        throw error;
    }
}

export async function analyzePatient(patientId: string): Promise<AnalysisResult> {
    try {
        const response = await fetch(`${API_BASE}/api/analyze`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ patient_id: patientId }),
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || `HTTP error! status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error("Error analyzing patient:", error);
        throw error;
    }
}
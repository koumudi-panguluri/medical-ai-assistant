import React from 'react';
import { Patient } from '../api/client';

interface Props {
    patient: Patient;
    onAnalyze: (patientId: string) => void;
}

export const PatientCard: React.FC<Props> = ({ patient, onAnalyze }) => {
    return (
        <div className="patient-card">
            <div className="patient-icon">📋</div>
            <div className="patient-id">{patient.id}</div>
            <h3>{patient.name}</h3>
            <p className="patient-age">Age: {patient.age} | {patient.sex}</p>

            <div className="conditions">
                {patient.conditions.length > 0 ? (
                    patient.conditions.map((condition, idx) => (
                        <span key={idx} className="condition-badge">
                            {condition}
                        </span>
                    ))
                ) : (
                    <span className="condition-badge">No active conditions</span>
                )}
            </div>

            <button
                className="analyze-btn"
                onClick={() => onAnalyze(patient.id)}
            >
                Analyze Patient →
            </button>
        </div>
    );
};
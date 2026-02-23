import React from 'react';
import { PatientDetailed } from '../api/client';

interface Props {
    summary: string;
    patient: PatientDetailed;
}

export const IntakeSummary: React.FC<Props> = ({ summary, patient }) => {
    return (
        <div>
            <div className="section">
                <h3>📋 Patient Demographics</h3>
                <div className="section-content">
                    <div className="info-grid">
                        <div className="info-item">
                            <div className="info-label">Name</div>
                            <div className="info-value">{patient.name}</div>
                        </div>
                        <div className="info-item">
                            <div className="info-label">Age</div>
                            <div className="info-value">{patient.age}</div>
                        </div>
                        <div className="info-item">
                            <div className="info-label">Sex</div>
                            <div className="info-value">{patient.sex}</div>
                        </div>
                        <div className="info-item">
                            <div className="info-label">Patient ID</div>
                            <div className="info-value">{patient.id}</div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="section">
                <h3>🏥 Active Conditions</h3>
                <div className="list-section">
                    {patient.conditions.map((condition, idx) => (
                        <div key={idx} className="list-item">
                            <div className="list-item-icon">🔴</div>
                            <div className="list-item-text">{condition}</div>
                        </div>
                    ))}
                </div>
            </div>

            <div className="section">
                <h3>💊 Current Medications</h3>
                <div className="list-section">
                    {patient.medications.map((med, idx) => (
                        <div key={idx} className="list-item">
                            <div className="list-item-icon">💊</div>
                            <div className="list-item-text">{med}</div>
                        </div>
                    ))}
                </div>
            </div>

            <div className="section">
                <h3>⚠️ Allergies</h3>
                <div className="list-section">
                    {patient.allergies.map((allergy, idx) => (
                        <div key={idx} className="list-item">
                            <div className="list-item-icon">⚠️</div>
                            <div className="list-item-text">{allergy}</div>
                        </div>
                    ))}
                </div>
            </div>

            <div className="section">
                <h3>🧪 Recent Labs</h3>
                <div className="info-grid">
                    {Object.entries(patient.recent_labs).map(([key, value]) => (
                        <div key={key} className="info-item">
                            <div className="info-label">{key}</div>
                            <div className="info-value">{value}</div>
                        </div>
                    ))}
                </div>
            </div>

            <div className="disclaimer">
                <strong>⚠️ IMPORTANT DISCLAIMER:</strong> This output is generated for educational
                and simulation purposes only. All clinical decisions must be made by a licensed
                healthcare provider.
            </div>
        </div>
    );
};
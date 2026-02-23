import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { PatientCard } from '../components/PatientCard';
import { fetchPatients, Patient } from '../api/client';

export const PatientSelection: React.FC = () => {
    const [patients, setPatients] = useState<Patient[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const navigate = useNavigate();

    useEffect(() => {
        fetchPatients()
            .then(setPatients)
            .catch(err => {
                console.error('Failed to load patients:', err);
                setError('Failed to load patients. Is the backend running?');
            })
            .finally(() => setLoading(false));
    }, []);

    const handleAnalyze = (patientId: string) => {
        navigate(`/analyze/${patientId}`);
    };

    if (loading) {
        return (
            <div className="loading">
                <div className="loading-spinner"></div>
                <p>Loading patients...</p>
            </div>
        );
    }

    if (error) {
        return (
            <div className="loading">
                <div style={{ color: '#DC2626', fontSize: '1.25rem' }}>WRONG {error}</div>
                <p style={{ marginTop: '1rem', color: '#6B7280' }}>
                    Make sure the backend is running on http://localhost:8000
                </p>
            </div>
        );
    }

    return (
        <div className="patient-selection">
            <header>
                <h1>Medical AI Assistant</h1>
                <p>Select a patient for AI-powered multi-agent analysis</p>
            </header>

            <div className="patient-grid">
                {patients.map(patient => (
                    <PatientCard
                        key={patient.id}
                        patient={patient}
                        onAnalyze={handleAnalyze}
                    />
                ))}
            </div>
        </div>
    );
};
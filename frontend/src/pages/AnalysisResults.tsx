import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { analyzePatient, AnalysisResult } from '../api/client';
import { AnalysisProgress } from '../components/AnalysisProgress';
import { IntakeSummary } from '../components/IntakeSummary';
import { DiagnosisView } from '../components/DiagnosisView';
import { CarePlanView } from '../components/CarePlanView';

type Tab = 'intake' | 'diagnosis' | 'care-plan';

export const AnalysisResults: React.FC = () => {
    const { patientId } = useParams<{ patientId: string }>();
    const navigate = useNavigate();
    const [result, setResult] = useState<AnalysisResult | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [activeTab, setActiveTab] = useState<Tab>('intake');

    useEffect(() => {
        if (patientId) {
            analyzePatient(patientId)
                .then(setResult)
                .catch(err => {
                    console.error('Analysis failed:', err);
                    setError(err.message || 'Analysis failed');
                })
                .finally(() => setLoading(false));
        }
    }, [patientId]);

    if (loading) {
        return <AnalysisProgress />;
    }

    if (error) {
        return (
            <div className="loading">
                <div style={{ color: '#DC2626', fontSize: '1.25rem' }}>
                    Analysis Failed
                </div>
                <p style={{ marginTop: '1rem', color: '#6B7280' }}>{error}</p>
                <button
                    onClick={() => navigate('/')}
                    style={{ marginTop: '2rem' }}
                    className="analyze-btn"
                >
                    ← Back to Patient Selection
                </button>
            </div>
        );
    }

    if (!result) {
        return <div className="loading">No results available</div>;
    }

    return (
        <div className="analysis-results">
            <button className="back-button" onClick={() => navigate('/')}>
                ← Back to Patients
            </button>

            <header>
                <h1>{result.patient_info.name} ({result.patient_info.id})</h1>
                <p style={{ color: '#6B7280', marginTop: '0.5rem' }}>
                    Analysis completed in {result.processing_time.toFixed(2)}s
                </p>
            </header>

            <div className="tabs">
                <button
                    className={activeTab === 'intake' ? 'active' : ''}
                    onClick={() => setActiveTab('intake')}
                >
                    Intake Summary
                </button>
                <button
                    className={activeTab === 'diagnosis' ? 'active' : ''}
                    onClick={() => setActiveTab('diagnosis')}
                >
                    Diagnosis
                </button>
                <button
                    className={activeTab === 'care-plan' ? 'active' : ''}
                    onClick={() => setActiveTab('care-plan')}
                >
                    Care Plan
                </button>
            </div>

            <div className="tab-content">
                {activeTab === 'intake' && (
                    <IntakeSummary
                        summary={result.intake_summary}
                        patient={result.patient_info}
                    />
                )}
                {activeTab === 'diagnosis' && (
                    <DiagnosisView
                        diagnosis={result.diagnosis}
                        interactions={result.drug_interactions}
                    />
                )}
                {activeTab === 'care-plan' && (
                    <CarePlanView
                        carePlan={result.care_plan}
                    />
                )}
            </div>
        </div>
    );
};
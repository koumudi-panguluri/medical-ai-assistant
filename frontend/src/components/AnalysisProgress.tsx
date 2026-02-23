import React from 'react';

export const AnalysisProgress: React.FC = () => {
    return (
        <div className="analysis-progress">
            <h2>Analyzing Patient...</h2>

            <div className="progress-steps">
                <div className="step completed">
                    Intake Agent - Retrieving patient record
                </div>
                <div className="step active">
                    Diagnosis Agent - Searching medical literature
                </div>
                <div className="step waiting">
                    Care Plan Agent - Waiting to start
                </div>
            </div>

            <div className="loading mt-4">
                <div className="loading-spinner"></div>
                <p>This may take 20-30 seconds...</p>
            </div>
        </div>
    );
};
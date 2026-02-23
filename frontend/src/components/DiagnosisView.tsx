import React from 'react';

interface Props {
    diagnosis: string;
    interactions?: string;
}

export const DiagnosisView: React.FC<Props> = ({ diagnosis, interactions }) => {
    // Parse diagnosis text (simplified - you can enhance this)
    const sections = diagnosis.split('\n\n');

    return (
        <div>
            <div className="section">
                <h3>🔬 Clinical Assessment</h3>
                <div className="section-content">
                    <div style={{ whiteSpace: 'pre-wrap', lineHeight: '1.8' }}>
                        {diagnosis}
                    </div>
                </div>
            </div>

            {interactions && (
                <div className="section">
                    <h3>⚠️ Drug Interactions</h3>
                    <div className="alert">
                        <div className="alert-title">
                            <span>⚠️</span>
                            <span>Potential Drug Interaction Detected</span>
                        </div>
                        <div className="alert-content">
                            {interactions}
                        </div>
                    </div>
                </div>
            )}

            <div className="disclaimer">
                <strong>⚠️ IMPORTANT DISCLAIMER:</strong> This assessment is for educational
                purposes only. Clinical decisions require licensed healthcare provider oversight.
            </div>
        </div>
    );
};